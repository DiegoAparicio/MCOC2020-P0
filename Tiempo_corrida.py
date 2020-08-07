# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:21:19 2020

@author: 56977
"""

from scipy import matrix, rand
from time import perf_counter

dts = []
mem = []

datos = open("datos_corrida10.txt","w")

N = [2,5,10,12,15,20,25,30,40,50,60,70,80,90,100,125,150,175,200,300,400,500,650,800,1000,2000,5000,10000]

for n in N:
    print (f"N = {n}")
    A = matrix(rand(n,n))
    B = matrix(rand(n,n))
    
    t1 = perf_counter()
    C = A@B
    t2 = perf_counter()
    
    dt = t2 - t1
    
    ram = 3*(n**2)*8
    
    dts.append(dt)
    mem.append(ram)
    
    datos.write(f"{n} {dt} {ram}\n")
    
    print (f"Tiempo transcurrido = {dt} s")
    print (f"Memoria RAM usada = {ram} bytes")
    
    datos.flush()

