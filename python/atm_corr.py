# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:26:36 2022

@author: snaima
"""

from at1a_module.atmcorr import AC

from at1a_module.dialog import AC_dialog

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi

gxpy = gx.gx()


def rungx():
    
    height, output =AC_dialog(title="Atmospheric correction", height='ElipsoidalHeight',
                                                     output='atmcorr') 
    
    db = gxdb.Geosoft_gdb.open()
    atmcorr_chan = gxdb.Channel.new(db, output, replace=True)
        # read data from the line.
    for line in db.list_lines():
        ht, fid = db.read_channel(line, height)
            
        atmcorr_=AC(ht)
    
    #Save atmospheric correction to the database
        
        db.write_channel(line, atmcorr_chan, atmcorr_, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(output)

