# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:09:10 2022

@author: snaima
"""

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb
gxpy = gx.gx()

from at1a_module.dialog import ROT_input

from at1a_module.gps import RotAccENtoCL

import geosoft.gxapi as gxapi


def rungx():
    
    # read data from the line.   
    crse,Eacc, Nacc, gps_ac, gps_al =ROT_input(title='Rotate accelerations from E-N to C-L',crse='course',Eacc='gps_eacc', Nacc='gps_nacc', gps_ac='gps_crossacc', gps_al='gps_longacc')
    db = gxdb.Geosoft_gdb.open()
    
    gps_ac_chan = gxdb.Channel.new(db, gps_ac, replace=True)
    gps_al_chan = gxdb.Channel.new(db, gps_al, replace=True)
        
    for line in db.list_lines():
        alpha, fid = db.read_channel(line, crse)
        acce, fid = db.read_channel(line, Eacc)
        accn, fid = db.read_channel(line, Nacc)

        ac,al =RotAccENtoCL(alpha, acce, accn)
        
        db.write_channel(line, gps_ac_chan, ac, fid)
        db.write_channel(line, gps_al_chan, al, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(gps_ac)
    DB.load_chan(gps_al)