# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:27:29 2022

@author: snaima
"""

from at1a_module.filter import gaussianfilter

import numpy as np

from at1a_module.dialog import GSfilter_dialog

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxapi as gxapi

gxpy = gx.gx()


def rungx():
    
    inchan,output,fs,filterlen,passes =GSfilter_dialog(title="Gaussian Filter", inchan='', output='',
                                                     fs='10', filterlen='',passes='3') 
    
    db = gxdb.Geosoft_gdb.open() 
        # read data from the line.
        
    filtered_chan = gxdb.Channel.new(db, output, replace=True)
    for line in db.list_lines():
        chan, fid = db.read_channel(line, inchan)
        
        filtered_output=gaussianfilter(chan,passes,fs,filterlen)
        
        s=filterlen*10
        
        filtered_output[0:s]=np.nan
        filtered_output[(-1-s):]=np.nan
    
        db.write_channel(line, filtered_chan, filtered_output, fid)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(output)