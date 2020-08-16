# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:48:42 2020

@author: 56977
"""

import matplotlib.pyplot as plt
import numpy as np

def plotting(names):
    absisas = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    TPO = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60.,60*10]
    TPO_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
    
    plt.figure()
    
    for name in names:
        data = np.loadtxt(name)
        Ns = data[:, 0]
        dts = data[:, 1]
        
        plt.loglog(Ns, dts.T, "-o", label=name)
        plt.ylabel("Tiempo transcurrido")
        plt.xlabel("Tamaño matriz N")
        plt.grid(True)
        plt.xticks(absisas,absisas,rotation=45)
        plt.yticks(TPO,TPO_label)
        
    plt.tight_layout()
    plt.legend(loc="upper left")
    plt.show()
    
names = ["A_invB_inv.txt","A_invB_npSolve.txt", "A_invB_spSolve.txt","A_invB_spSolve_symmetric.txt","A_invB_spSolve_pos.txt","A_invB_spSolve_pos_overwrite.txt"]
plotting(names)