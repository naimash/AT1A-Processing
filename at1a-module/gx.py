# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:15:34 2022

@author: snaima
"""

import os

import geosoft.gxapi as gxapi

import geosoft.gxapi.GXSYS


def _at1aimport_gx():
    
#"""Resolve and run the at1aimport GX"""
    dir = os.path.split(__file__)[0]
    at1aimport = os.path.join(os.path.join(dir, 'gx'), 'at1aimport.gx')
    ret = gxapi.GXSYS.run_gx(at1aimport)
    if ret == -1:
        
        geosoft.gxapi.GXSYS.cancel_()
    return ret

def _process_gravity_gx():
    
#"""Resolve and run the Process_gravity GX"""
    dir = os.path.split(__file__)[0]
    process_gravity = os.path.join(os.path.join(dir, 'gx'), 'Process_gravity.gx')
    ret = gxapi.GXSYS.run_gx(process_gravity)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _cc_gx():
    
#"""Resolve and run the cc input GX"""
    dir = os.path.split(__file__)[0]
    cc = os.path.join(os.path.join(dir, 'gx'), 'cc.gx')
    ret = gxapi.GXSYS.run_gx(cc)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _eotvos_gx():
    
#"""Resolve and run the eotvos GX"""
    dir = os.path.split(__file__)[0]
    eotvos = os.path.join(os.path.join(dir, 'gx'), 'eotvos.gx')
    ret = gxapi.GXSYS.run_gx(eotvos)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _timesync_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    timesync = os.path.join(os.path.join(dir, 'gx'), 'timesync.gx')
    ret = gxapi.GXSYS.run_gx(timesync)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _timesyncchan_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    timesyncchan = os.path.join(os.path.join(dir, 'gx'), 'timesyncchan.gx')
    ret = gxapi.GXSYS.run_gx(timesyncchan)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _tide_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    tide = os.path.join(os.path.join(dir, 'gx'), 'tide.gx')
    ret = gxapi.GXSYS.run_gx(tide)
    if ret == -1:
        gxapi.GXSYS.cancel_()
    return ret

def _bmfilter_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    bmfilter = os.path.join(os.path.join(dir, 'gx'), 'bmfilter.gx')
    ret = gxapi.GXSYS.run_gx(bmfilter)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _gsfilter_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    gsfilter = os.path.join(os.path.join(dir, 'gx'), 'gsfilter.gx')
    ret = gxapi.GXSYS.run_gx(gsfilter)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _fac2ord_gx():
    
#"""Resolve and run the FAC2ORD GX"""
    dir = os.path.split(__file__)[0]
    fac2ord = os.path.join(os.path.join(dir, 'gx'), 'fac2ord.gx')
    ret = gxapi.GXSYS.run_gx(fac2ord)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _faa_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    faa = os.path.join(os.path.join(dir, 'gx'), 'faa.gx')
    ret = gxapi.GXSYS.run_gx(faa)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _latcorr_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    latcorr = os.path.join(os.path.join(dir, 'gx'), 'latcorr.gx')
    ret = gxapi.GXSYS.run_gx(latcorr)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _levelcomp_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    levelcomp = os.path.join(os.path.join(dir, 'gx'), 'levelcomp.gx')
    ret = gxapi.GXSYS.run_gx(levelcomp)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret


def _rotacc_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    rotacc = os.path.join(os.path.join(dir, 'gx'), 'rotacc.gx')
    ret = gxapi.GXSYS.run_gx(rotacc)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret


def _gpsvel_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    gpsvel = os.path.join(os.path.join(dir, 'gx'), 'gpsvel.gx')
    ret = gxapi.GXSYS.run_gx(gpsvel)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _gpsacc_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    gpsacc = os.path.join(os.path.join(dir, 'gx'), 'gpsacc.gx')
    ret = gxapi.GXSYS.run_gx(gpsacc)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _crse_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    crse = os.path.join(os.path.join(dir, 'gx'), 'crse.gx')
    ret = gxapi.GXSYS.run_gx(crse)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _batchproc_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    batchproc = os.path.join(os.path.join(dir, 'gx'), 'batchproc.gx')
    ret = gxapi.GXSYS.run_gx(batchproc)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _atmcor_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    atmcor = os.path.join(os.path.join(dir, 'gx'), 'atmcor.gx')
    ret = gxapi.GXSYS.run_gx(atmcor)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret

def _batchproc2_gx():
    
#"""Resolve and run the GX"""
    dir = os.path.split(__file__)[0]
    batchproc2 = os.path.join(os.path.join(dir, 'gx'), 'batchproc2.gx')
    ret = gxapi.GXSYS.run_gx(batchproc2)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret


def _process_gravity2_gx():
    
#"""Resolve and run the Process_gravity GX"""
    dir = os.path.split(__file__)[0]
    process_gravity2 = os.path.join(os.path.join(dir, 'gx'), 'Process_gravity2.gx')
    ret = gxapi.GXSYS.run_gx(process_gravity2)
    if ret == -1:
        
        gxapi.GXSYS.cancel_()
    return ret





























