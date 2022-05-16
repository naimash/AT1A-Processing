# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:31:23 2022

@author: snaima
"""

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb
gxpy = gx.gx()

from at1a_module.dialog import gpsacc_input

from at1a_module.gps import gps_acceleration

import geosoft.gxapi as gxapi


def rungx():
    
    # read data from the line.   
    East_vel,North_vel,Vert_vel,fs, gpseacc, gpsnacc,gpsvacc=gpsacc_input(title='GPS Acceleration',East_vel='gps_evel',North_vel='gps_nvel',Vert_vel='gps_vvel', fs='10', gpseacc='gps_eacc', gpsnacc='gps_nacc', gpsacc='gps_vacc')
    db = gxdb.Geosoft_gdb.open()
    
    acce_chan = gxdb.Channel.new(db, gpseacc, replace=True)
    accn_chan = gxdb.Channel.new(db, gpsnacc, replace=True)
    acc_chan = gxdb.Channel.new(db, gpsvacc, replace=True)
        
    for line in db.list_lines():
        ve, fid = db.read_channel(line, East_vel)
        vn, fid = db.read_channel(line, North_vel)
        vu, fid=db.read_channel(line, Vert_vel)

        gpsacc, acce, accn =gps_acceleration(ve,vn,vu,fs)
        
        db.write_channel(line, acce_chan, acce, fid)
        db.write_channel(line, accn_chan, accn, fid)
        db.write_channel(line, acc_chan, gpsacc, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(gpseacc)
    DB.load_chan(gpsnacc)
    DB.load_chan(gpsvacc)