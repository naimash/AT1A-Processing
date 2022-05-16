# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:50:38 2022

@author: snaima
"""



import pandas as pd

from at1a_module.dialog import tide_input

from at1a_module.time_utils import datenum

from at1a_module.time_utils import calculate_julian_century

from at1a_module.tide import solve_longman_tide

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi



gpsleap=18

gxpy = gx.gx()

def rungx():
    
    # read data from the line.   
    GPStime,lon,lat,alt,outg0=tide_input(title='Tide correction', GPStime='gps_timestamp',lon='Longitude',lat='Latitude',alt='ElipsoidalHeight',  outg0='tidecorr')
    db = gxdb.Geosoft_gdb.open()
    g0_chan = gxdb.Channel.new(db, outg0, replace=True)

    
        
    for line in db.list_lines():  
        gps_timestamp, fid = db.read_channel(line, GPStime)
        lon_, fid = db.read_channel(line, lon)
        lat_, fid = db.read_channel(line, lat)
        alt_, fid=db.read_channel(line, alt)
        
        x=pd.Series(gps_timestamp)
        tgps=((datenum(x))*24*3600)-gpsleap
    
        T, t0= calculate_julian_century(tgps,gps_timestamp)

    
        gm,gs,g0=solve_longman_tide(lat_, lon_, alt_, T,t0)
    
        db.write_channel(line, g0_chan, g0, fid)
        
    DB = gxapi.GXEDB.current()
     
    DB.un_lock() 
    
    DB.load_chan(outg0)
    

































