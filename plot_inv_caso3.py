# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:35:36 2020

@author: 56977
"""

import scipy as sp
import matplotlib.pyplot as plt

data = sp.loadtxt("datos3_corrida6.txt")

N = data[:,0]
dts = data[:,1]
mem = data[:,2]

for i in range(7,9):
    data = sp.loadtxt(f"datos3_corrida{i}.txt")
    dts = sp.vstack((dts, data[:,1]))
    
absisas = [10,20,50,100,200,500,1000,2000,5000,10000,20000]

TPO = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60.,60*10]
TPO_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

RAM = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10,10**11]
RAM_label = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB", "" ]
    
plt.figure()

plt.subplot(2,1,1)
plt.title("Rendimiento np.double")
plt.loglog(N, dts.T, "-o")
plt.legend(["numpy",'scipy False', 'scipy True'],loc="upper left")
plt.ylabel("Tiempo transcurrido")  
plt.xticks(absisas,[])
plt.yticks(TPO,TPO_label)
plt.grid(True)  
plt.subplot(2,1,2)
plt.loglog(N, mem.T, "-o")
plt.ylabel("Uso de memoria") 
plt.xlabel("Tamaño matriz N")
plt.yticks(RAM,RAM_label)
plt.xticks(absisas,absisas,rotation=45)
plt.axhline(1.6*10**10,  0, 1,ls="--",color="k") #linea discontinua en el limite de memoria RAM de mi computador
plt.axhline(3.84*10**5,  0, 1,ls="--",color="k") #cache L1
plt.axhline(1.5*10**6,  0, 1,ls="--",color="k") #cache L2
plt.axhline(9*10**6,  0, 1,ls="--",color="k") #cache L3
plt.grid(True)
plt.show()