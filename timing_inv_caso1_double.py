# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:24:20 2020

@author: 56977
"""

from time import perf_counter
from numpy import zeros, double
from numpy.linalg import inv


def matriz_laplaciana(N, dtype=double):
    A= zeros((N,N),dtype=dtype)
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i + 1 == j:
                A[i,j] = -1
            if i - 1 == j:   
                A[i,j] = -1
    return inv(A)

dts = []
mem = []

datos = open("datos3_corrida6.txt","w")

Ns = [3,4,5,10,15,20,25,30,40,50,60,70,80,90,100,125,150,175,200,300,400,500,650,800,1000,2000,5000,10000]

for N in Ns:
    print (f"N = {N}")
    
    t1 = perf_counter()
    matriz_laplaciana(N)
    t2 = perf_counter()
    
    dt = t2 - t1
    
    ram = 2*(N**2)*64
    
    dts.append(dt)
    mem.append(ram)
    
    datos.write(f"{N} {dt} {ram}\n")
    
    print (f"Tiempo transcurrido = {dt} s")
    print (f"Memoria RAM usada = {ram} bytes")
    
    datos.flush()