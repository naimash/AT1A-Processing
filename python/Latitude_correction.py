# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:38:43 2022

@author: snaima
"""
from at1a_module.latcorr import latcorr

from at1a_module.dialog import latcorr_dialog

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi

gxpy = gx.gx()


def rungx():
    
    lat,output1=latcorr_dialog(title="Latitude correction", lat='Latitude',
                                             output1='latcorr') 
    
    db = gxdb.Geosoft_gdb.open()
    latcorr_chan = gxdb.Channel.new(db, output1, replace=True)
    
        
    # read data from the line.
    for line in db.list_lines():
        lat_, fid = db.read_channel(line, lat)
            
        Latcorr=latcorr(lat_)
    
        #Save latitude correction to the database
        db.write_channel(line, latcorr_chan, Latcorr, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(output1)

