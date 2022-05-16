# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:20:39 2022

@author: 25479
"""

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

from at1a_module.eotvos import calc_eotvos

from at1a_module.dialog import eotvos_dialog


import geosoft.gxapi as gxapi

gxpy = gx.gx()

def rungx():
           
    lat,lon,height,Outch =eotvos_dialog(title="Calculate Eotvos", lat='Latitude', 
                                        lon='Longitude', height='ElipsoidalHeight', Outch='eotvos')    

    db = gxdb.Geosoft_gdb.open() 
    Eotvos_chan = gxdb.Channel.new(db, Outch, replace=True)
    # read data from the line.
    for line in db.list_lines():
        lat, fid = db.read_channel(line, lat)
        lon, fid = db.read_channel(line, lon)
        ht, fid = db.read_channel(line, height)
        

    Eotvos = calc_eotvos(lat, lon, ht, 10)
    gxapi.GXSYS.progress(1)
    gxapi.GXSYS.prog_name('Calculating eotvos',0)
    gxapi.GXSYS.prog_update_l(19, 20)
    #Save Eotvos to the database
    db.write_channel(line, Eotvos_chan, Eotvos, fid)
    
    DB = gxapi.GXEDB.current()
             
    DB.un_lock() 
            
    DB.load_chan(Outch)
    