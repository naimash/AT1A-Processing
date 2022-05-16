# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:00:46 2022

@author: snaima
"""


import pandas as pd

from datetime import datetime as dt

def convert_gps_time(gpsweek, gpsweekseconds, format='unix'):

    gps_delta = 315964800.0

    gpsweek_cf = 604800

    gps_ticks = gpsweek*gpsweek_cf+gpsweekseconds

    timestamp = (gps_delta + gps_ticks).round(1)

    if format == 'unix':

        return timestamp

    elif format == 'datetime':

        return pd.to_datetime('1970-1-1') + pd.to_timedelta(timestamp * 1e9)

    elif format == 'Gtm_sec':

        DateTime=pd.to_datetime(timestamp,unit='s')

        date=pd.to_datetime(DateTime[DateTime.index[0]]).date()

        Gtm_sec=(DateTime-pd.to_datetime(date)).dt.total_seconds()

        return Gtm_sec
    
    
def datenum(x='pd.Series of gps_timestamp'):
        
        time=pd.to_datetime(x,unit='s')
    
        d = (time.apply(pd.Timestamp.toordinal))
    
        y=366+d+(time-(d.apply(pd.Timestamp.fromordinal))).dt.total_seconds()/(24*60*60)
        return y
    
def calculate_julian_century(tgps,gpstime='gps_timestamp array'):
    """
    Calculate the decimal Julian century and floating point hour, as referenced from
    1899, December 31 at 12:00:00
    Parameters
    ----------
    
    tgps: (datenum*24*3600-gpsleap): A serial date number represents the whole and fractional 
    number of days from a fixed, preset date (January 0, 0000) in the proleptic ISO calendar.
    time : gps datetime array(no. of secods from 1970-1-1)

    Returns
    -------
    T:    Number of Julian centuries (36525 days) from GMT Noon on
           December 31, 1899
    t0 : Greenwich civil dates measured in hours
    """
    # dref is Dec. 31, 1899 12:00:00
    ref=dt.strptime('1899-12-31 12:00:00', '%Y-%m-%d %H:%M:%S')
    
    dref=366 + ref.toordinal() + (ref - dt.fromordinal(ref.toordinal())).total_seconds()/(24*60*60)

    #Compute number of julian centuries
    T=((tgps/24/3600)-dref)/36525
    
    time=pd.to_datetime(gpstime,unit='s')
    
    t0 = time.hour + time.minute / 60. + time.second / 3600.

    return pd.Series(T), pd.Series(t0)