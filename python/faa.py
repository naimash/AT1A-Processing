# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:37:23 2022

@author: snaima
"""

from at1a_module.dialog import FAA_dialog

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi

import geosoft.gxapi.GXEDB 


gxpy = gx.gx()


def rungx():
    
    grav,eotvos,tide,latc,fac,faa =FAA_dialog(title="Free air anomaly", grav='fgrav', eotvos='eotvos',
                                                     tide='tidecorr', latc='latcorr',fac='facorr',faa='faa') 
    
    db = gxdb.Geosoft_gdb.open()
    freeairanom_chan = gxdb.Channel.new(db, faa, replace=True)
        # read data from the line.
    for line in db.list_lines():
        grav_, fid = db.read_channel(line, grav)
        eotvos_, fid = db.read_channel(line, eotvos)
        tide_, fid = db.read_channel(line, tide)
        latc_, fid = db.read_channel(line, latc)
        fac_, fid = db.read_channel(line, fac)
            
        freeairanom=(grav_)+(eotvos_)+(tide_)-(latc_)-(fac_)
    
    #Save free air anomaly to the database
        
        db.write_channel(line, freeairanom_chan, freeairanom, fid)
        
    
    DB = gxapi.GXEDB.current()
     
    DB.un_lock() 
    
    DB.load_chan(faa)