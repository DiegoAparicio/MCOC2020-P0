# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 09:54:09 2020

@author: 56977
"""


import numpy as np

def mimatmul(A,B,result):
    
    # iterate through rows of X
    for i in range(len(A)):
       # iterate through columns of Y
       for j in range(len(B[0])):
           # iterate through rows of Y
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
               
    return result       

