#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Daniel Platero-Rochart [daniel.platero-rochart@medunigraz.at]
"""

x = 330

factor=2

if x < 2:
    print('Error!!! values is less than 2')
else:
    while factor <= x:
        if x % factor == 0:
            print(factor)
            x = x // factor
        else:
            factor += 1 
