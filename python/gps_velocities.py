# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:36:05 2022

@author: snaima
"""

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb
gxpy = gx.gx()

from at1a_module.dialog import gpsvel_input

from at1a_module.gps import gps_velocities

import geosoft.gxapi as gxapi


def rungx():
    
    # read data from the line.   
    lat,lon,ht,fs,East_vel,North_vel,Vert_vel=gpsvel_input(title='GPS Velocity',lat='Latitude',lon='Longitude',ht='ElipsoidalHeight',fs='10',East_vel='gps_evel',North_vel='gps_nvel',Vert_vel='gps_vvel')
    db = gxdb.Geosoft_gdb.open()
    
    ve_chan = gxdb.Channel.new(db, East_vel, replace=True)
    vn_chan = gxdb.Channel.new(db, North_vel, replace=True)
    vu_chan = gxdb.Channel.new(db, Vert_vel, replace=True)
        
    for line in db.list_lines():
        lat_, fid = db.read_channel(line, lat)
        lon_, fid = db.read_channel(line, lon)
        alt_, fid=db.read_channel(line, ht)

        ve, vn, vu=gps_velocities(lat_,lon_,alt_,fs)
        
        db.write_channel(line, ve_chan, ve, fid)
        db.write_channel(line, vn_chan, vn, fid)
        db.write_channel(line, vu_chan, vu, fid)
        
        
    DB = gxapi.GXEDB.current()
     
    DB.un_lock() 
    
    DB.load_chan(East_vel)
    DB.load_chan(North_vel)
    DB.load_chan(Vert_vel)