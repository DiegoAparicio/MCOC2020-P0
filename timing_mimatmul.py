# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:25:11 2020

@author: 56977
"""

from scipy import rand
from time import perf_counter
import numpy as np
from mimatmul import mimatmul


dts = []
mem = []

datos = open("datos2_corrida9.txt","w")

N = [2,5,10,12,15,20,25,30,40,50,60,70,80,90,100,125,150,175,200,300,400,500,650,800,1000]

for n in N:
    print (f"N = {n}")
    A = rand(n,n)
    B = rand(n,n)
    result = np.zeros(shape=(n,n))
    
    t1 = perf_counter()
    mimatmul(A,B,result)
    t2 = perf_counter()
    
    dt = t2 - t1
    
    ram = 3*(n**2)*8
    
    dts.append(dt)
    mem.append(ram)
    
    datos.write(f"{n} {dt} {ram}\n")
    
    print (f"Tiempo transcurrido = {dt} s")
    print (f"Memoria RAM usada = {ram} bytes")
    
    datos.flush()