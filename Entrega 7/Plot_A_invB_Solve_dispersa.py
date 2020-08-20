# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:02:46 2020

@author: 56977
"""

import matplotlib.pyplot as plt
import numpy as np

def plotting(names):
    absisas = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    TPO = [0.01e-3,0.1e-3,1e-3,1e-2,0.1,1.,10.,60.,60*10,60*100]
    TPO_label = ["0.01 ms","0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    
    plt.figure()
    dtsy1 = []
    dtsy2 = []
    for name in names:
        data = np.loadtxt(name)
        Ns = data[:, 0]
        dts1 = data[:, 1]
        dts1max = max(dts1)
        Nsmax = max(Ns)
        dts2 = data[:, 2]
        dts2max = max(dts2)
        dtsy1=0*Ns+dts1max
        dtsy2=0*Ns+dts2max
        
        plt.subplot(2,1,1)
        plt.title("A_invB_Solve_dispersa")
        plt.ylim([0.01e-3,100])
        plt.loglog(Ns, dts1.T, "k-o", alpha=0.4,markersize=3)
        plt.ylabel("Tiempo de ensamblado")
        
        
        plt.subplot(2,1,2)
        plt.ylim([0.01e-3,100])
        plt.loglog(Ns, dts2.T, "k-o", alpha=0.4,markersize=3)
        plt.ylabel("Tiempo de solucion")
        plt.xlabel("Tamaño matriz N")
       
    plt.subplot(2,1,1)
    plt.plot(Ns,dtsy1, "c--") 
    plt.loglog(Ns,Ns*(dts1max/Nsmax),"y--")
    plt.plot(Ns,Ns**2*(dts1max/Nsmax**2),"g--")
    plt.plot(Ns,Ns**3*(dts1max/Nsmax**3),"r--")
    plt.plot(Ns,Ns**4*(dts1max/Nsmax**4),"m--")
    plt.xticks(absisas,[])
    plt.yticks(TPO,TPO_label)
    plt.subplot(2,1,2)
    plt.plot(Ns,dtsy2, "c--",label="Constante") 
    plt.loglog(Ns,Ns*(dts2max/Nsmax),"y--",label="O(N)")
    plt.plot(Ns,Ns**2*(dts2max/Nsmax**2),"g--",label="O(N^2)")
    plt.plot(Ns,Ns**3*(dts2max/Nsmax**3),"r--",label="O(N^3)")
    plt.plot(Ns,Ns**4*(dts2max/Nsmax**4),"m--",label="O(N^4)")
    plt.xticks(absisas,absisas,rotation=45)
    plt.yticks(TPO,TPO_label)
        
        
    plt.tight_layout()
    plt.legend(loc="upper left")
    plt.show()
    
names = ["A_invB_Solve_dispersa0.txt","A_invB_Solve_dispersa1.txt","A_invB_Solve_dispersa2.txt","A_invB_Solve_dispersa3.txt","A_invB_Solve_dispersa4.txt"]
plotting(names)

