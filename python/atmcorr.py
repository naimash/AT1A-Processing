# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:18:06 2022

@author: snaima
"""


def AC (ht):
    """
    AC2ord - 2nd order atmospheric correction 
    ht = height, meters
    
    """

    AC = -((0.874-(9.9*(10**-5))*ht)+(3.56*(10**-9))*(ht**2));
    
    return AC
