# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 18:51:19 2020

@author: 56977
"""

from time import perf_counter
import numpy as np
from numpy import zeros, float32
from numpy.linalg import inv, solve
import scipy.linalg as linalg

Ns = [2,4,5,10,15,20,25,30,40,50,60,70,80,90,100,125,150,175,200,300,400,500,650,800,1000,2000,5000,10000,15000]

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

Ncorridas = 5

names = ["A_invB_inv.txt","A_invB_npSolve.txt", "A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt","A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"]

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
        
        # Ocupando sp.linalg.solve(A,B)
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][2] = dt
        #
        
        # Ocupando sp.linalg.solve (symmetric)
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = linalg.solve(A,B,assume_a="sym")
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][3] = dt
        #
        
         # Ocupando sp.linalg.solve (pos)
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = linalg.solve(A,B,assume_a="pos")
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][4] = dt
        #
        
         # Ocupando sp.linalg.solve (pos, overwrite = True)
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = linalg.solve(A,B,assume_a="pos", overwrite_a=True)
        t2 = perf_counter()
        dt = t2 - t1
        dts[i][5] = dt
        #
        
    print("dts: ", dts)
    
    dts_mean = np.mean(dts, axis=0) 
    
    print("dts_mean: ", dts_mean)
    
    #Escribiendo en los archivos de texto
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()