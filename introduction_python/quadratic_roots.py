#!/bin/python
# -*- coding: utf-8 -*-
"""
@author: Daniel Platero-Rochart [daniel.platero-rochart@medunigraz.at]
"""

a = 5
b = 6
c = 1

# Calculate the determinant
determinant = b**2 - 4*a*c

if determinant < 0:
    print('The function does not have any real root')

elif determinant == 0:
    root = -b/(2*a)
    print(f'The function has only one real root: {root}')

else:
    root1 = (-b + (determinant)**(1/2))/(2*a)
    root2 = (-b - (determinant)**(1/2))/(2*a)
    print(f'The function has two real roots: {root1} and {root2}')























