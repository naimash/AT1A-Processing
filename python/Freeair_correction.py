# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:38:43 2022

@author: snaima
"""

from at1a_module.freeair import FAC2ord

from at1a_module.dialog import FAC_dialog

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi

gxpy = gx.gx()


def rungx():
    
    lat,height, output1 =FAC_dialog(title="Free air correction", lat='Latitude', height='ElipsoidalHeight',
                                                     output1='facorr') 
    
    db = gxdb.Geosoft_gdb.open()
    freeaircorr_chan = gxdb.Channel.new(db, output1, replace=True)
        # read data from the line.
    for line in db.list_lines():
        phi, fid = db.read_channel(line, lat)
        ht, fid = db.read_channel(line, height)
            
        freeaircorr=FAC2ord(phi, ht)
    
    #Save free air correction to the database
        
        db.write_channel(line, freeaircorr_chan, freeaircorr, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(output1)

