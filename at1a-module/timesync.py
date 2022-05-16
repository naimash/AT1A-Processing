# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:10:56 2022

@author: snaima
"""

import numpy as np
import scipy
from scipy import signal
import geosoft.gxapi.GXSYS
import geosoft.gxapi as gxapi

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
        
        gxapi.GXSYS.display_message('Time shift finder','high resolution shift finder')


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

def time_Shift_array(s1: np.array,timeshift, datarate: int):
    
    t = np.linspace(0, len(s1)/datarate, len(s1))+timeshift
    
    not_nan = np.logical_not(np.isnan(s1))
    
    f = scipy.interpolate.interp1d(t[not_nan],s1[not_nan], kind='cubic')

    # only generate data in the range of t2

   # newt = t - timeshift*datarate

    newt = t-timeshift

    for x in range(0, len(t)):

        if newt[x] < t[0]:

            newt[x] = t[0]

        if newt[x] > t[-1]:

            newt[x] = t[-1]

    s2 = f(newt)

    return s2