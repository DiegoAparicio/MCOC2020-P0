# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy as sp


N = 3
A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))

print(f"A = \n{A}")
print(f"B = \n{B}")

C = A*B

print (f"C = A*B = {C}")
