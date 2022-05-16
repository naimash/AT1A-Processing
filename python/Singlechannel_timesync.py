# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:37:22 2022

@author: snaima
"""

import geosoft.gxpy.gx as gx

import geosoft.gxapi as gxapi

import geosoft.gxpy.gdb as gxdb

from at1a_module.timesync import find_time_delay

from at1a_module.timesync import time_Shift_array

from at1a_module.dialog import timesyncchan_input


gxpy = gx.gx()

def rungx():

    db = gxdb.Geosoft_gdb.open() 
    
    eotvos, gravity,inch,outch =timesyncchan_input(title="Time Synchronization", eotvos='', gravity='', inch='',outch='')
    
    gxapi.GXSYS.progress(1)
    gxapi.GXSYS.prog_name('Time Synchronization',0)
    gxapi.GXSYS.prog_update_l(5, 20)
    
    out_chan = gxdb.Channel.new(db, outch, replace=True)
    # read data from the line.
    for line in db.list_lines():
       
        Eotvos, fid = db.read_channel(line, eotvos)
        gravity, fid = db.read_channel(line, gravity)
        in_chan, fid = db.read_channel(line, inch)

        time = find_time_delay(Eotvos, -gravity, 10,resolution=1)
    
        timeshift=str(time)
        gxapi.GXSYS.prog_update_l(10, 20)
        gxapi.GXSYS.display_message('Time shift',timeshift)
    
        output = time_Shift_array(in_chan, -time, 10)

        #Save timeshifted channel to the database
        db.write_channel(line, out_chan, output, fid)
        gxapi.GXSYS.prog_update_l(20, 20)
        
    DB = gxapi.GXEDB.current()
         
    DB.un_lock() 
        
    DB.load_chan(outch)
    
    
    
    
    
    
    
    
    
    