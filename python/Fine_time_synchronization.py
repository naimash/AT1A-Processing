# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 05:07:37 2022

@author: 25479
"""
from at1a_module.timesync import find_time_delay

from at1a_module.timesync import time_Shift_array

import geosoft.gxpy.gx as gx

import geosoft.gxapi as gxapi

import geosoft.gxpy.gdb as gxdb


from at1a_module.dialog import timesync_input



gxpy = gx.gx()



def rungx():
    
    proceed=gxapi.GXSYS.display_question('NOTE:','This process will replace all meter data channels after applying a timeshift. Do yo want to proceed?')
    
    if proceed==1:

        db = gxdb.Geosoft_gdb.open() 
        
        eotvos, meterg,fgrav =timesync_input(title="Time Synchronization", eotvos='eotvos', meterg='meterg', fgrav='fgrav')
        
        gxapi.GXSYS.progress(1)
        gxapi.GXSYS.prog_name('Time Synchronization',0)
        gxapi.GXSYS.prog_update_l(5, 20)
        
        #Createchannels
        metergs_chan = gxdb.Channel.new(db, 'metergs', dup='gravity', replace=True)
        gravity_chan='gravity'
        fgrav_chan=fgrav
        long_accel_chan='long_accel'
        cross_accel_chan='cross_accel'
        beam_chan='beam'
        temp_chan='temp'
        pressure_chan='pressure'
        Etemp_chan='Etemp'
        gps_week_chan='gps_week'
        gps_sow_chan='gps_sow'
        clamp_chan='clamp'
        unclamp_chan='unclamp'
        gps_sync_chan='gps_sync'
        feedback_chan='feedback'
        reserved1_chan='reserved1'
        reserved2_chan='reserved2'
        ad_lock_chan='ad_lock'
        cmd_rcvd_chan='cmd_rcvd'
        nav_mode_1_chan='nav_mode_1'
        nav_mode_2_chan='nav_mode_2'
        free_chan='free'
        SensCom_chan='SensCom'
        GPStime_chan='GPStime'
        ADsat_chan='ADsat'
        Datavalid_chan='Datavalid'
        PlatCom_chan='PlatCom'
        
        
        # read data from the line.
        for line in db.list_lines():
           
            Eotvos, fid = db.read_channel(line, eotvos)
            meterg, fid = db.read_channel(line, meterg)
            gravity, fid = db.read_channel(line, 'gravity')
            fgrav, fid = db.read_channel(line, fgrav)
            long_accel, fid = db.read_channel(line, 'long_accel')
            cross_accel, fid = db.read_channel(line, 'cross_accel')
            beam, fid = db.read_channel(line, 'beam')
            temp, fid = db.read_channel(line, 'temp')
            pressure, fid = db.read_channel(line, 'pressure')
            Etemp, fid = db.read_channel(line, 'Etemp')
            gps_week, fid = db.read_channel(line, 'gps_week')
            gps_sow, fid = db.read_channel(line, 'gps_sow')
            clamp, fid = db.read_channel(line, 'clamp')
            unclamp, fid = db.read_channel(line, 'unclamp')
            gps_sync, fid = db.read_channel(line, 'gps_sync')
            feedback, fid = db.read_channel(line, 'feedback')
            reserved1, fid = db.read_channel(line, 'reserved1')
            reserved2, fid = db.read_channel(line, 'reserved2')
            ad_lock, fid = db.read_channel(line, 'ad_lock')
            cmd_rcvd, fid = db.read_channel(line, 'cmd_rcvd')
            nav_mode_1, fid = db.read_channel(line, 'nav_mode_1')
            nav_mode_2, fid = db.read_channel(line, 'nav_mode_2')
            free, fid = db.read_channel(line, 'free')
            SensCom, fid = db.read_channel(line, 'SensCom')
            GPStime, fid = db.read_channel(line, 'GPStime')
            ADsat, fid = db.read_channel(line, 'ADsat')
            Datavalid, fid = db.read_channel(line, 'Datavalid')
            PlatCom, fid = db.read_channel(line, 'PlatCom')
        

            time1 = find_time_delay(Eotvos, -meterg, 10,resolution=1)
        
            initialtimeshift=str(time1)
            gxapi.GXSYS.prog_update_l(10, 20)
            gxapi.GXSYS.display_message('Initial time shift',initialtimeshift)
        
            #Time shift all meter data
            metergs = time_Shift_array(meterg, -time1, 10)
            gravity = time_Shift_array(gravity, -time1, 10)
            fgrav = time_Shift_array(fgrav, -time1, 10)
            long_accel = time_Shift_array(long_accel, -time1, 10)
            cross_accel = time_Shift_array(cross_accel, -time1, 10)
            beam = time_Shift_array(beam, -time1, 10)
            temp = time_Shift_array(temp, -time1, 10)
            pressure = time_Shift_array(pressure, -time1, 10)
            Etemp = time_Shift_array(Etemp, -time1, 10)
            gps_week = time_Shift_array(gps_week, -time1, 10)
            gps_sow = time_Shift_array(gps_sow, -time1, 10)
            clamp = time_Shift_array(clamp, -time1, 10)
            unclamp = time_Shift_array(unclamp, -time1, 10)
            gps_sync = time_Shift_array(gps_sync, -time1, 10)
            feedback = time_Shift_array(feedback, -time1, 10)
            reserved1 = time_Shift_array(reserved1, -time1, 10)
            reserved2 = time_Shift_array(reserved2, -time1, 10)
            ad_lock = time_Shift_array(ad_lock, -time1, 10)
            cmd_rcvd = time_Shift_array(cmd_rcvd, -time1, 10)
            nav_mode_1 = time_Shift_array(nav_mode_1, -time1, 10)
            nav_mode_2 = time_Shift_array(nav_mode_2, -time1, 10)
            free = time_Shift_array(free, -time1, 10)
            SensCom = time_Shift_array(SensCom, -time1, 10)
            GPStime = time_Shift_array(GPStime, -time1, 10)
            ADsat = time_Shift_array(ADsat, -time1, 10)
            Datavalid = time_Shift_array(Datavalid, -time1, 10)
            PlatCom = time_Shift_array(PlatCom, -time1, 10)

            time2 = find_time_delay(Eotvos, -metergs, 10,resolution=1)
        
            Finaltimeshift=str(time2)
        
            gxapi.GXSYS.display_message('Final time shift',Finaltimeshift)
        
        
        
        #Save timeshifted channels to the database
            db.write_channel(line, metergs_chan, metergs, fid)
            db.write_channel(line, gravity_chan, gravity, fid)
            db.write_channel(line, fgrav_chan, fgrav, fid)
            db.write_channel(line, long_accel_chan, long_accel, fid)
            db.write_channel(line, cross_accel_chan, cross_accel, fid)
            db.write_channel(line, beam_chan, beam, fid)
            db.write_channel(line, temp_chan, temp, fid)
            db.write_channel(line, pressure_chan, pressure, fid)
            db.write_channel(line, Etemp_chan, Etemp, fid)
            db.write_channel(line, gps_week_chan, gps_week, fid)
            db.write_channel(line, gps_sow_chan, gps_sow, fid)
            db.write_channel(line, clamp_chan, clamp, fid)
            db.write_channel(line, unclamp_chan, unclamp, fid)
            db.write_channel(line, gps_sync_chan, gps_sync, fid)
            db.write_channel(line, feedback_chan, feedback, fid)
            db.write_channel(line, reserved1_chan, reserved1, fid)
            db.write_channel(line, reserved2_chan, reserved2, fid)
            db.write_channel(line, ad_lock_chan, ad_lock, fid)
            db.write_channel(line, cmd_rcvd_chan, cmd_rcvd, fid)
            db.write_channel(line, nav_mode_1_chan, nav_mode_1, fid)
            db.write_channel(line, nav_mode_2_chan, nav_mode_2, fid)
            db.write_channel(line, free_chan, free, fid)
            db.write_channel(line, SensCom_chan, SensCom, fid)
            db.write_channel(line, GPStime_chan, GPStime, fid)
            db.write_channel(line, ADsat_chan, ADsat, fid)
            db.write_channel(line, Datavalid_chan, Datavalid, fid)
            db.write_channel(line, PlatCom_chan, PlatCom, fid)
        
        gxapi.GXSYS.prog_update_l(20, 20)
        
        
        
        
    
    