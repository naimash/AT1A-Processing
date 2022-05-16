# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:10:27 2022

@author: snaima
"""
from scipy import signal

import numpy as np


def blackmanfilter(chan,fs,filterlen):
   
    a = 1.0
    numtaps = (2*filterlen*fs)+1  # Taps=2*filterlength*sampling;
    nyq_rate = fs / 2

    fc = 1/filterlen  # frequecy stop  #freq=1/filtertime;
    Nfc = fc / nyq_rate  # normaliced cutt of frequency  ==wn
        
    b = signal.firwin(numtaps, Nfc, window='blackman')
    
    chan=np.pad(chan,(filterlen*10,filterlen*10),'reflect')
    
    f = signal.filtfilt(b, a, chan)
    
    f=f[filterlen*10:-filterlen*10]
    
    return f
        
        
def convn(chan,b):  
    y=np.convolve(chan,b,'same')
    return y


def gaussianfilter(chan,n,fs,filterlen):
    
    numtaps=filterlen*fs     #filterlen*sampling
    sd= 2*filterlen
    
    if np.mod(numtaps,2)==0:  #
        numtaps=numtaps+1  #window len must be an odd integer
        
    b = signal.windows.gaussian(numtaps,sd)
    b=b/np.sum(b)
    
    chan=np.pad(chan,(filterlen*10,filterlen*10),'reflect')
    
    n=n+1
    n=np.arange(1,n,1)
        
    for i in n:
        f=convn(chan,b)
        chan=f
    
    f=f[filterlen*10:-filterlen*10]
    
    
    return f
    