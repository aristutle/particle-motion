# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:09:30 2016
particle motion simulating,
probably visualization.


@author: shmcao
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import time

class ParticleCluster:
    def __init__(self,n,d):
        if(n<=0 or d<=0):return None
        self.n=n
        self.d=d
        self.R=np.random.rand(n,d)
        self.V=np.zeros((n,d))
        return None
        
    def move(self,velocity=0.1):
        n=self.n
        d=self.d
        if(n==0):return
        self.V = velocity * 2 * (np.random.rand(n,d)-0.5*np.ones((n,d)))
        self.R += self.V
        return
        
def update_plt(fig,coords):
    fig.set_xdata(coords[0])
    fig.set_ydata(coords[1])
    plt.draw()
    return
pars = ParticleCluster(100,2)
plt.figure("Particles")
plt.axis(xmin=0,xmax=1,ymin=0,ymax=1)
plt.xlabel(r'x')
plt.ylabel(r'y')
plt.ion()
coords=np.transpose(pars.R)
plt.scatter(coords[0],coords[1])
while(True):
    #plt.scatter([p[0] for p in particles.R],[p[1] for p in particles.R])
    pars.move(0.01)
    coords=np.transpose(pars.R)
    plt.clf()
    plt.axis(xmin=0,xmax=1,ymin=0,ymax=1)
    plt.xlabel(r'x')
    plt.ylabel(r'y')
    plt.scatter(coords[0],coords[1])
    plt.pause(0.5)
    
#plt.close()