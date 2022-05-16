# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:58:18 2022

@author: snaima
"""

import numpy as np

def FAC2ord (phi, ht):
    """
    FAC2ord - 2nd order free-air correction
    phi = latitude, degrees 
    ht = height, meters
    
    """
    sinphi = np.sin(np.deg2rad(phi));

    s2phi = sinphi ** 2;

    FAC = -((0.3087691- 0.0004398*s2phi) * ht) + 7.2125e-8 * (ht * ht);
    
    return FAC