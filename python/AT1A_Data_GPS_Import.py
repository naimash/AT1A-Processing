# -*- coding: utf-8 -*-

"""

Created on Mon Mar  7 16:29:42 2022



@author: Naima Shariff

"""

#from IPython.display import Image

import numpy as np

from at1a_module.time_utils import convert_gps_time

from at1a_module.unpack_bits import _unpack_bits

from at1a_module.dialog import at1a_import

import geosoft.gxapi as gxapi

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi.GXSYS

import geosoft.gxapi.GXEDB

gxpy = gx.gx()

import pandas as pd



def rungx():
            
    AT1A_Gravity_data, GPS_data, db_name =at1a_import(title="AT1A Import", AT1A_Gravity_data='', GPS_data='', db_name='')
    
    gxapi.GXSYS.progress(1)
    gxapi.GXSYS.prog_name('Importing data',0)
    gxapi.GXSYS.prog_update_l(5, 20)


    at1a_data=open(AT1A_Gravity_data)

    channel_names1 =  ['gravity', 'long_accel', 'cross_accel', 'beam',

                          'temp', 'status', 'pressure', 'Etemp', 'gps_week',

                          'gps_sow','Hz1_Counter']
    
    channel_names2 =  ['gravity', 'long_accel', 'cross_accel', 'beam',

                          'temp', 'status', 'pressure', 'Etemp', 'gps_week',

                          'gps_sow']

    at1a_df = pd.read_csv(at1a_data, header=None)
    
    if len(at1a_df.columns) > 10:
        
        at1a_df.columns =channel_names1
        
    else:
        at1a_df.columns =channel_names2

    # expand status field

    data = np.flipud(_unpack_bits(at1a_df['status']))

    df = pd.DataFrame(np.column_stack(list(zip(*data))))

    columns = ['clamp', 'unclamp', 'gps_sync', 'feedback',

                          'reserved1', 'reserved2', 'ad_lock', 'cmd_rcvd',

                          'nav_mode_1', 'nav_mode_2', 'free',

                          'SensCom', 'GPStime', 'ADsat', 'Datavalid',

                          'PlatCom']
    
    # remove fields from the end if not named

    if len(columns) < len(df.columns):

        df.drop(df.columns[range(len(columns), len(df.columns))], axis=1, inplace=True)

        df.columns = columns

    elif len(columns) > len(df.columns):

        df.columns = columns[:len(df.columns)]

    else:

        df.columns = columns


    at1a_df = pd.concat([at1a_df, df], axis=1)

    at1a_df.pop('status');

    gxapi.GXSYS.prog_update_l(5, 20)

   # create datetime index

   #Truncate intitial start of data where gps time is zero

    df1= at1a_df.loc[at1a_df['gps_week'] == 0]
    
    if len(df1>0):

        at1a_df=at1a_df.truncate(before=((df1.index[-1]+1)))

        
    #Find time jumps or discontinuity in time 

    unixtime = (convert_gps_time(at1a_df['gps_week'], at1a_df['gps_sow'], format='unix'))
    
    gxapi.GXSYS.prog_update_l(10, 20)
    
    #Calculate a second order difference in the unix time
    diff1 = (np.diff((np.array(unixtime)),n=2)).round(5)
    
    diff1=np.pad(diff1, (1, 1), 'edge')
    
    diff1=pd.DataFrame(diff1)
    
    diff1.columns=['diff1']
    
    diff1.index=unixtime.index
    
    #locate index where the absolute value of the second order difference is greater than zero
    
    diff1_= diff1.loc[abs(diff1['diff1'])> 0]
    
    gxapi.GXSYS.prog_update_l(15, 20)
    #unixtime[diff1_.index]=np.nan
    
    at1a_df['unixtime']=unixtime
    
    if len(diff1_>0) and at1a_df['gps_sow'][(diff1_.index[0]+1)]>at1a_df['gps_sow'][(diff1_.index[0]+2)]:

         at1a_df=at1a_df.truncate(before=(diff1_.index[0+1]+1))
        
    #Create datetime index
    dt = convert_gps_time(at1a_df['gps_week'], at1a_df['gps_sow'], format='datetime')

    at1a_df.index = dt
    
    at1a_df=at1a_df.drop_duplicates(subset =['unixtime']);

    interval = '100000U'

    index = pd.date_range(at1a_df.index[0], at1a_df.index[-1], freq=interval)

    at1a_df = at1a_df.reindex(index)
    
    #Import GPS data

    gps_data=open(GPS_data)

    gps_df = pd.read_csv(gps_data, skiprows=1,header=None, date_parser=[0])
    

        
    gps_channel_names1=['GPSDate','GPSTime','Latitude','Longitude','OrthometricHeight',

                       'ElipsoidalHeight','Numofsatelites','PDOP']

    gps_channel_names2=['GPSDate','GPSTime','Latitude','Longitude','OrthometricHeight',

                       'ElipsoidalHeight','Numofsatelites','PDOP','speed']
    
    if len(gps_df.columns) > 8:
        
        gps_df.columns =gps_channel_names2
        
    else:
        gps_df.columns =gps_channel_names1
        
        
    gps_df['DateTime'] = pd.to_datetime(gps_df.pop('GPSDate')) + pd.to_timedelta(gps_df.pop('GPSTime'))

    gps_timestamp=(gps_df.DateTime -pd.to_datetime('1970-1-1')).dt.total_seconds()
    
    gps_timestamp=gps_timestamp.round(1)

    dateindex=pd.to_datetime('1970-1-1') + pd.to_timedelta(gps_timestamp * 1e9)
    
    gps_df['gps_timestamp']=gps_timestamp

    gps_df.pop('DateTime');

    gps_df.index = dateindex

   

    if (at1a_df.index[0] >= gps_df.index[0]):        

        start = at1a_df.index[0]

    else:

        start = gps_df.index[0]



    if (at1a_df.index[-1] >= gps_df.index[-1]):

        end = gps_df.index[-1]

    else:

        end = at1a_df.index[-1]

        

    at1a_df = at1a_df[start: end]

    gps_df = gps_df[start: end]

    at1a_df=at1a_df.reset_index(drop=True)

    gps_df=gps_df.reset_index(drop=True)

#Merge and import all data to geosoft

    pd_data=pd.concat([at1a_df, gps_df],axis=1)   

#create a new database from list of channels and numpy data. All data is stored in a single line.

    channel_names=pd_data.columns    

    data = pd_data.to_numpy()

    #geo_db_name=simpledialog.askstring('create_database','New Database Name')
   
    with gxdb.Geosoft_gdb.new(db_name, overwrite=True) as db:

        db.write_line('L0', data, channel_names,fid=(0.0,0.1))
        
        
    gxapi.GXSYS.prog_update_l(20, 20)
    geosoft.gxapi.GXEDB.load_new(db_name)
    

  # create a valid line name for line 0 type random, and write all the data to this line



  