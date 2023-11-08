#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Daniel Platero-Rochart [daniel.platero-rochart@medunigraz.at]
"""

upto = 100
primes = []

for value in range(2, upto + 1):
    is_prime = True
    for divisor in range(2, value):
        if value % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(value)

print(primes)

