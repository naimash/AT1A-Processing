# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:21:25 2022

@author: snaima
"""

import numpy as np

from at1a_module.filter import blackmanfilter

from at1a_module.filter import gaussianfilter

from sklearn.linear_model import LinearRegression


def Tilterrorandcorrection(gps_ac,gps_al,meter_ac,meter_al):
    """ 
    Peters & Brozena Trigonometric 
    
    """
    NaN=np.isnan(gps_al)

    gps_al[NaN]=0
    
    NaN=np.isnan(gps_ac)

    gps_ac[NaN]=0
    
    NaN=np.isnan(meter_ac)

    meter_ac[NaN]=0
    
    NaN=np.isnan(meter_al)

    meter_al[NaN]=0
    
    sampling= 10
    longcal=1.0
    crosscal=1.0
    
    filtertime=240
    filterlen=filtertime
    
    #y1a=signal.filtfilt(b,a,gps_al)
    y1a=blackmanfilter(gps_al,sampling,filterlen)
    #y1a=gaussianfilter(gps_al,3,sampling,filterlen)
    
    #yma=signal.filtfilt(b,1,1000*longcal*meter_al)
    yma=blackmanfilter(1000*longcal*meter_al,sampling,filterlen)
    #yma=gaussianfilter(1000*longcal*meter_al,3,sampling,filterlen)
    
    y1a=y1a.reshape(len(y1a),1)
    
    yma=yma.reshape(len(yma),1)
    
    coefa=LinearRegression(fit_intercept=False).fit(yma, -y1a).coef_

    yma=coefa*yma
    
    yma=-yma
    
    g0 = 981000
    
    anglon=(-g0+np.sqrt((g0**2)+(2*y1a*(y1a-yma))))/y1a
    
    anglon=anglon.reshape(len(anglon),)
    
    errorlong=-(anglon*gps_al-(g0*((anglon**2)/2)))
    
    
    #y1b=signal.filtfilt(b,a,gps_ac)
    y1b=blackmanfilter(gps_ac,sampling,filterlen)
    #y1b=gaussianfilter(gps_ac,3,sampling,filterlen)
    
    #ymb=signal.filtfilt(b,1,1000*crosscal*meter_ac)
    ymb=blackmanfilter(1000*crosscal*meter_ac,sampling,filterlen)
    #ymb=gaussianfilter(1000*crosscal*meter_ac,3,sampling,filterlen)
    
    y1b=y1b.reshape(len(y1b),1)
    
    ymb=ymb.reshape(len(ymb),1)
    
    coefb=LinearRegression(fit_intercept=False).fit(ymb, -y1b).coef_

    ymb=coefb*ymb
    
    ymb=-ymb
    
    g0 = 981000
    
    angcross=(-g0+np.sqrt((g0**2)+(2*y1b*(y1b-ymb))))/y1b
    
    angcross=angcross.reshape(len(angcross),)
    
    errorcross=-(angcross*gps_ac-(g0*((angcross**2)/2)))
    
    Levelcomp=errorlong+errorcross
    
    #fLevelcomp=signal.filtfilt(b,a,Levelcomp)
        
    return errorcross, errorlong, Levelcomp
