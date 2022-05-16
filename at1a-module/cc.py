# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:16:28 2022

@author: snaima
"""

from scipy import signal

import numpy as np

def cc(gravity,fgrav,beam,long_accel,cross_accel,ve_comp,al_comp,ax_comp,vcc_comp):
    
# calculate VMON monitor
#----------------------------------------------------
    vmonTap=600  

    #vmonB= fir1(vmonTap,1/vmonTap,blackman(vmonTap+1));
    vmonB= signal.firwin(vmonTap,1/vmonTap,window='blackman')
#--------------------------------------------------
    f60grav=signal.filtfilt(vmonB,1,gravity)   # filter to remove the mean

    d=gravity-f60grav

    nan = (np.isnan(d))

    d[nan]=0

    I=np.cumsum(d)

    I=I-np.mean(I[1100:(-1-1100)])

    vmo=abs((I)/1000)

    #ve=vmo

    #vcc=vmo # use the vmond monitor instead of al

    ve=1e-6*(gravity-f60grav*0)**2;    #ve

    #end vmon calculation

    vcc=1000*beam*long_accel

    lc=long_accel     # long acc coupling cross direction

    xc=cross_accel    # cross acc coupling

    al=1e-5*gravity*long_accel

    ax=1e-5*gravity*cross_accel

    fgrav=fgrav+ve_comp*ve+al_comp*al+ax_comp*ax+vcc_comp*vcc
    
    return fgrav