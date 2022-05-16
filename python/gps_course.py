# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:40:32 2022

@author: snaima
"""

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb
gxpy = gx.gx()

from at1a_module.dialog import crse_input

from at1a_module.gps import gps_course

import geosoft.gxapi as gxapi


def rungx():
    
    # read data from the line.   
    East_vel,North_vel, course, course_vel=crse_input(title='GPS Velocity',East_vel='gps_evel',North_vel='gps_nvel',course='course', course_vel='course_vel')
    db = gxdb.Geosoft_gdb.open()
    
    crse_chan = gxdb.Channel.new(db, course, replace=True)
    crse_vel_chan = gxdb.Channel.new(db, course_vel, replace=True)
        
    for line in db.list_lines():
        ve, fid = db.read_channel(line, East_vel)
        vn, fid = db.read_channel(line, North_vel)

        crse, vel =gps_course(ve,vn)
        
        db.write_channel(line, crse_chan, crse, fid)
        db.write_channel(line, crse_vel_chan, vel, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(course)
    DB.load_chan(course_vel)