# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:16:09 2022

@author: snaima
"""
import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb
gxpy = gx.gx()

from at1a_module.dialog import level_input

from at1a_module.level import Tilterrorandcorrection

import geosoft.gxapi as gxapi


def rungx():
    
    # read data from the line.   
    gps_ac,gps_al,meter_ac,meter_al,ecross,elong,levelcomp =level_input(title='Tilt correction',gps_ac='gps_crossacc',gps_al='gps_longacc',meter_ac='cross_accel',meter_al='long_accel',ecross='ecross',elong='elong',levelcomp='levelcomp')
    db = gxdb.Geosoft_gdb.open()
    
    ecross_chan = gxdb.Channel.new(db, ecross, replace=True)
    elong_chan = gxdb.Channel.new(db, elong, replace=True)
    levelcomp_chan = gxdb.Channel.new(db, levelcomp, replace=True)
    
    gxapi.GXSYS.progress(1)
    gxapi.GXSYS.prog_name('Calculating level correction',0)
    gxapi.GXSYS.prog_update_l(5, 20)
    
    gxapi.GXSYS.prog_update_l(17, 20)
        
    for line in db.list_lines():
        gps_ac_, fid = db.read_channel(line, gps_ac)
        gps_al_, fid = db.read_channel(line, gps_al)
        meter_ac_, fid = db.read_channel(line, meter_ac)
        meter_al_, fid = db.read_channel(line, meter_al)

        errorcross, errorlong, levelcomp_=Tilterrorandcorrection(gps_ac_, gps_al_, meter_ac_, meter_al_)
        
        db.write_channel(line, ecross_chan, errorcross, fid)
        db.write_channel(line, elong_chan, errorlong, fid)
        db.write_channel(line, levelcomp_chan, levelcomp_, fid)
        
    gxapi.GXSYS.prog_update_l(20, 20)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(ecross)
    DB.load_chan(elong)
    DB.load_chan(levelcomp)