# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 04:25:45 2022

@author: 25479
"""

import numpy as np

from scipy import signal

import geosoft.gxpy.utility

import geosoft.gxpy.gx as gx

import geosoft.gxpy.gdb as gxdb

import geosoft.gxpy.project

import geosoft.gxapi as gxapi
import geosoft.gxapi.GXSYS
import os


gxpy = gx.gx()

def rungx():
    
    def _t(s):
        return s
    
    class ProjectException(geosoft.GXRuntimeError):
        """
        Exceptions from :mod:`geosoft.gxpy.project`.
        .. versionadded:: 9.1
        """
        pass
    
    def _timeshift_gx():
        
    #"""Resolve and run the user_input GX"""
        dir = os.path.split(__file__)[0]
        timeshift = os.path.join(os.path.join(dir, 'gx'), 'timeshift.gx')
        ret = gxapi.GXSYS.run_gx(timeshift)
        if ret == -1:
            gxapi.GXSYS.cancel_()
        return ret
    
    
    def timeshift_input(title='', eotvos='', gravity=''):

        gxapi.GXSYS.filter_parm_group("USER_INPUT", 1)
        try:
            
            gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
            gxapi.GXSYS.set_string("USER_INPUT", "EOTVOS", str(eotvos))
            gxapi.GXSYS.set_string("USER_INPUT", "GRAV", str(gravity))

            ret =  _timeshift_gx()
            
            if ret == 0:
                
                eotvos= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "EOTVOS", eotvos)
                eotvos=eotvos.value
                
                gravity= gxapi.str_ref()
                gxapi.GXSYS.gt_string("USER_INPUT", "GRAV", gravity)
                gravity=gravity.value
        
                return eotvos,gravity
            
            raise ProjectException(_t('GX Error ({})').format(ret))
    
        finally:
            gxapi.GXSYS.filter_parm_group("USER_INPUT", 0)
    
    db = gxdb.Geosoft_gdb.open()
    
    eotvos,gravity=timeshift_input(title='Check timeshift', eotvos='', gravity='')
    # read data from the line.
    for line in db.list_lines():
        Eotvos, fid = db.read_channel(line, eotvos)
        gravity, fid = db.read_channel(line, gravity)
    
    def interpolate_1d_vector(vector: np.array, factor: int):
        
        x = np.arange(np.size(vector))
        
        not_nan = np.logical_not(np.isnan(vector))
        
        y = vector
        
        if factor==1:        
            
            y_interpolated = np.interp(x, x[not_nan], y[not_nan])
            
        elif factor>1:
            
            x_extended_by_factor = np.linspace(x[0], x[-1], np.size(x) * factor)
            
            y_interpolated = np.interp(x_extended_by_factor, x[not_nan], y[not_nan])

        return y_interpolated

    def find_time_delay(s1: np.array, s2: np.array, datarate: int, resolution: bool=None):
        
        lagwith = 400

        if not resolution:
            s1 = interpolate_1d_vector(s1, 1)
            
            s2 = interpolate_1d_vector(s2, 1)

            #c = np.correlate(s1, s2, mode=2)
            
            c = signal.correlate(s1,s2,mode='full')

            len_s1 = len(s1)
         
            scale = datarate

            print('low resolution shift finder')

        else:

            s1 = interpolate_1d_vector(s1, datarate)

            s2 = interpolate_1d_vector(s2, datarate)

           #numpy correlate too slow for high reolution shift finder
            #c = np.correlate(s1, s2, mode=2)
            
            c = signal.correlate(s1,s2,mode='full')

            len_s1 = len(s1)

            scale = datarate*10
            
            #gxc = gxpy.gx.GXpy()
            
            geosoft.gxpy.utility.display_message('Time shift finder','high resolution shift finder')


        shift = np.linspace(-lagwith, lagwith, 2 * lagwith + 1)

        # lags = np.arange(-lagwith, lagwith+1)

        corre = c[len_s1 - 1 - lagwith:len_s1 + lagwith]

        maxi = np.argmax(corre)

        dm1 = abs(corre[maxi] - corre[maxi - 1])

        dp1 = abs(corre[maxi] - corre[maxi + 1])

        if dm1 < dp1:

            z = np.polyfit(shift[maxi - 2:maxi + 1], corre[maxi - 2:maxi + 1], 2)

        else:

            z = np.polyfit(shift[maxi - 1:maxi + 2], corre[maxi - 1:maxi + 2], 2)



        dt1 = z[1] / (2 * z[0])



        # return time shift

        return dt1/scale
    
    time = find_time_delay(Eotvos, -gravity, 10,resolution=1)
    
    timeshift=str(time)
    
    geosoft.gxpy.utility.display_message('Time Shift',timeshift)