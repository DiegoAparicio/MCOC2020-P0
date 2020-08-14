# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:13:38 2020

@author: 56977
"""

from time import perf_counter
import numpy as np
from numpy import zeros, float32
from numpy.linalg import inv, solve

Ns = [2,4,5,10,15,20,25,30,40,50,60,70,80,90,100,125,150,175,200,300,400,500,650,800,1000,2000,5000,10000]

def matriz_laplaciana(N, dtype=float32):
    A= zeros((N,N),dtype=dtype)
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i + 1 == j:
                A[i,j] = -1
            if i - 1 == j:   
                A[i,j] = -1
    return A

Ncorridas = 10

names = ["A_invB_inv.txt","A_invB_npSolve.txt"]

files = [open(name,"w") for name in names]

for N in Ns:
    dts = np.zeros((Ncorridas, len(files)))
    print(f"N = {N}")
    
    for i in range(Ncorridas):
        
        #invirtiendo y multiplicando
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][0] = dt
        #
        
        # Ocupando np.linalg.solve(A,B)
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][1] = dt
        #
    
    print("dts: ", dts)
    
    dts_mean = np.mean(dts, axis=0) 
    
    print("dts_mean: ", dts_mean)
    
    #Escribiendo en los archivos de texto
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()
    
    
    
    
    
    
    
    
    
    
    
    