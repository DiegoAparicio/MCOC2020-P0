# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:10:40 2020

@author: 56977
"""

from time import perf_counter
import numpy as np
from numpy import  ones
from numpy.linalg import solve
import scipy.linalg as linalg
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv

def matriz_laplaciana_llena(N, dtype=np.double):
    A= np.identity(N,dtype)*2
    for i in range(N):
        for j in range(N):
            if i +1== j:
                A[i,j] = -1
            if i - 1 == j:   
                A[i,j] = -1
    return A

def matriz_laplaciana_dispersa(N, dtype=np.double):
    A= lil_matrix((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j]=2
            if i +1== j:
                A[i,j] = -1
            if i - 1 == j:   
                A[i,j] = -1
    return csc_matrix(A)

Ns = [2,4,8,10,20,40,80,100,200,400,800,1000,2000,4000,8000,10000]

Ncorridas = 5

for k in range(Ncorridas):
    
    names = [f"A_multB_matmul_llena{k}.txt",f"A_multB_matmul_dispersa{k}.txt",f"A_invB_Solve_llena{k}.txt",f"A_invB_Solve_dispersa{k}.txt", f"A_invB_inv_llena{k}.txt",f"A_invB_inv_dispersa{k}.txt"]
    
    files = [open(name,"w") for name in names]
    
    for N in Ns:
        dts1 = np.zeros((len(files)))
        dts2 = np.zeros((len(files)))
        print(f"N = {N}")
        
        
            
        # multiplicando A y B con matriz llena
        t1 = perf_counter()
        A = matriz_laplaciana_llena(N)
        B = matriz_laplaciana_llena(N)
        t2 = perf_counter()
        
        A_multB = A@B
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[0] = dt1
        dts2[0] = dt2
        #
        # multiplicando A y B con matriz dispersa
        t1 = perf_counter()
        A = matriz_laplaciana_dispersa(N)
        B = matriz_laplaciana_dispersa(N)
        t2 = perf_counter()
        
        A_multB = A@B
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[1] = dt1
        dts2[1] = dt2
        #
        # Solve Ax=b con matriz llena
        t1 = perf_counter()
        A = matriz_laplaciana_llena(N)
        B = ones(N,dtype=np.double)
        t2 = perf_counter()
        
        A_solveB = solve(A,B)
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[2] = dt1
        dts2[2] = dt2
        #
        # Solve Ax=b con matriz dispersa
        t1 = perf_counter()
        A = matriz_laplaciana_dispersa(N)
        B = ones(N,dtype=np.double)
        t2 = perf_counter()
        
        A_solveB = spsolve(A,B)
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[3] = dt1
        dts2[3] = dt2
        #
        # INV (A) con matriz llena
        t1 = perf_counter()
        A = matriz_laplaciana_llena(N)
        
        t2 = perf_counter()
        
        A_inv=linalg.inv(A)
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[4] = dt1
        dts2[4] = dt2
        #
        # INV (A) con matriz dispersa
        t1 = perf_counter()
        A = matriz_laplaciana_dispersa(N)
        
        t2 = perf_counter()
        
        A_inv=inv(A)
        
        t3 = perf_counter()
        dt1 = t2 - t1
        dt2 = t3 - t2
        dts1[5] = dt1
        dts2[5] = dt2
        #
            
        for j in range(len(files)):
            files[j].write(f"{N} {dts1[j]} {dts2[j]}\n")
            files[j].flush()