#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Daniel Platero-Rochart [daniel.platero-rochart@medunigraz.at]
"""

x = 9 

guess = x/2
threshold = abs((guess*guess) - x)

while threshold > 10e-12:
    guess = (guess + x/guess)/2
    threshold = abs((guess*guess) - x)
print(f'Square root of {x} is {guess}')
