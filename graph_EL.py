# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:32:47 2019

@author: 19158
"""

# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, source, dest, weight=1):
        
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, weighted = False, directed = False):
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        if weight == 1:
            listing = [source , dest ,1]
            self.el.append(listing)
        else:
            listing2 = [source,dest,weight]
            self.el.append(listing2)

    
    def delete_edge(self,source,dest): 

        listing = [source, dest,1]
        self.el.remove(listing)
        return  
                
    def display(self):
        print('[',end='')
        for i in range(len(self.el)):
            print('[',end='')
            print('(',self.el[i], ')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
#        scale = 30
#        fig, ax = plt.subplots()
#        for i in range(len(self.el)):
#            for edge in self.el[i]:
#                d,w = edge.dest, edge.weight
#                if self.directed or d>i:
#                    x = np.linspace(i*scale,d*scale)
#                    x0 = np.linspace(i*scale,d*scale,num=5)
#                    diff = np.abs(d-i)
#                    if diff == 1:
#                        y0 = [0,0,0,0,0]
#                    else:
#                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
#                    f = interp1d(x0, y0, kind='cubic')
#                    y = f(x)
#                    s = np.sign(i-d)
#                    ax.plot(x,s*y,linewidth=1,color='k')
#                    if self.directed:
#                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
#                        yd = [y0[2]-1,y0[2],y0[2]+1]
#                        yd = [y*s for y in yd]
#                        ax.plot(xd,yd,linewidth=1,color='k')
#                    if self.weighted:
#                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
#                        yd = [y0[2]-1,y0[2],y0[2]+1]
#                        yd = [y*s for y in yd]
#                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
#            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
#            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
#             bbox=dict(facecolor='w',boxstyle="circle"))
#        ax.axis('off') 
#        ax.set_aspect(1.0)
        return 
            
    def as_AM(self):
        arraying = []