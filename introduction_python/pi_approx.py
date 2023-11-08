#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Daniel Platero-Rochart [daniel.platero-rochart@medunigraz.at]
"""

n = 30

pi = 3

for i in range(1, n+1):
    if i % 2 != 0:
        pi = pi + 4/(i*2*(i*2 + 1)*(i*2 + 2))
    elif  i % 2 == 0:
        pi = pi - 4/(i*2*(i*2 + 1)*(i*2 + 2))
    print(pi)



