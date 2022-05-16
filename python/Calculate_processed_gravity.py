# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:27:58 2022

@author: 25479
"""


import geosoft.gxpy.gx as gx

import geosoft.gxapi as gxapi

import geosoft.gxpy.gdb as gxdb

from at1a_module.dialog import get_user_input

from at1a_module.dialog import get_cc_input

from at1a_module.cc import cc

gxpy = gx.gx()

def rungx():
   
    (Inch,Outch1,Outch2,Meteroffset, kfactor, PreStill, PostStill,TieGrav) =get_user_input(title="Meter Configuration", Inch='gravity', 
                                                             Outch1='meterg',Outch2='fgrav', 
                                                             Meteroffset='10000', kfactor='0.996',  PreStill='8341.2', 
                                                             PostStill='8339.1', TieGrav='978055.0')
    PreTieReading=PreStill
    
    PreTieReading=(PreTieReading-Meteroffset)*kfactor
    
    PreTieReading=PreTieReading+Meteroffset
    
    offset=TieGrav-(PreTieReading-Meteroffset)
                    
                    
    gxapi.GXSYS.progress(1)
    gxapi.GXSYS.prog_name('Calculating Processed Gravity',0)
    gxapi.GXSYS.prog_update_l(10, 20)
    
    monitors_comp=gxapi.GXSYS.display_question('Cross Coupling','Apply Cross Coupling monitors')
    
 # read data from the line.   
    db = gxdb.Geosoft_gdb.open()  
    
    fgrav_chan = gxdb.Channel.new(db, Outch2, replace=True)
    
    for line in db.list_lines():
        gravity, fid = db.read_channel(line, Inch)
    
    
    ##calculate processed gravity
        meterg=gravity-Meteroffset;  #meter uncalibrated no offset no Kfactor
    
        meterg_chan = gxdb.Channel.new(db, Outch1, dup='gravity', replace=True)
        
        db.write_channel(line, meterg_chan, meterg, fid)
    
        fgrav=kfactor*(gravity-Meteroffset)+offset  # meter full field gravity kfactor corrected
    
    #monitors_comp=0 #if monitors=1 the gravity data will be compensated with cross coupling monitor
    #Buid the monitors for the cross coupling corrections if used
    
    
        if monitors_comp==0:
            fgrav=fgrav
            
            db.write_channel(line, fgrav_chan, fgrav, fid)
        
        elif monitors_comp==1:
            beam,long_accel,cross_accel,vcc, ve, al,ax =get_cc_input(title="Monitors",beam='beam',long_accel='long_accel',
                                                                     cross_accel='cross_accel', vcc='0', ve='0', al='0',  ax='0')
        
            vcc_comp=vcc  # optimun vcc comp monitor gain

            ve_comp=ve #optimun ve comp monitor gain

            al_comp=al

            ax_comp=ax
        
        
            for line in db.list_lines():
                beam, fid = db.read_channel(line, beam)
                long_accel, fid = db.read_channel(line, long_accel)
                cross_accel, fid = db.read_channel(line, cross_accel)
        
                fgrav=cc(gravity,fgrav,beam,long_accel,cross_accel,ve_comp,al_comp,ax_comp,vcc_comp)

                db.write_channel(line, fgrav_chan, fgrav, fid)
    
        gxapi.GXSYS.prog_update_l(20, 20)
        
    DB = gxapi.GXEDB.current()
             
    DB.un_lock() 
            
    DB.load_chan(Outch1)
    DB.load_chan(Outch2)
    
        

    