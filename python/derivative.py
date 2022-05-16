# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 12:06:37 2022

@author: snaima
"""
import numpy as np

from scipy.signal import convolve

def derivative(y, datarate, edge_order=None):

    if edge_order is None:

        d1 = derivative(y, 1, datarate)

        d2 = derivative(y, 2, datarate)

        return d1, d2

    if edge_order == 1:

        dy = (y[2:] - y[0:-2]) * (datarate / 2)

        return dy

    elif edge_order == 2:

        dy = ((y[0:-2] - 2 * y[1:-1]) + y[2:]) * (np.power(datarate, 2))

        return dy

    else:

        return ValueError('Invalid value for parameter n {1 or 2}')
    
    
def central_difference(data_in, n=1, dt=0.1):
    """ central difference differentiator """
        # first derivative
    if n == 1:
        dy = (data_in[2:] - data_in[0:-2]) / (2 * dt)
        # second derivative
    elif n == 2:
        dy = ((data_in[0:-2] - 2 * data_in[1:-1] + data_in[2:]) /
                 np.power(dt, 2))
    else:
        raise ValueError('Invalid value for parameter n {1 or 2}')

    return np.pad(dy, (1, 1), 'edge')

def taylor_fir(data_in, n=1, dt=0.1):
    """ 10th order Taylor series FIR differentiator """
    coeff = np.array([1 / 1260, -5 / 504, 5 / 84, -5 / 21, 5 / 6, 0, -5 / 6, 5 / 21, -5 / 84, 5 / 504, -1 / 1260])
    y = 0
    for _ in range(1, n + 1):
        y = convolve(data_in, coeff, mode='same')
    return y * (1 / dt) ** n