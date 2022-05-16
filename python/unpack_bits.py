# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:04:15 2022

@author: snaima
"""
import numpy as np

import struct

def _unpack_bits(n):

     x = np.array(list(struct.iter_unpack('4B', (struct.pack(">{}I".format(len(n)), *n)))), dtype=np.uint8)

     return np.flip(np.unpackbits(x, axis=1))