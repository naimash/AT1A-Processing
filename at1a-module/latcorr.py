# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:30:17 2022

@author: snaima
"""

import numpy as np


def latcorr(lat):
    
    sinlam = np.sin(np.deg2rad(lat));

    sinsqlam = sinlam ** 2;

    num = 1 + 0.00193185265241 * sinsqlam;

    den = np.sqrt(1 - 0.00669437999014 * sinsqlam);

    g = 978032.53359 * (num / den);
    
    return g