# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:29:52 2019

@author: 19158
"""

# Adjacency list representation of graphs
import graph_AM as graph # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest 
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')  
            
            
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        
#---------------------------------------------------------------------------------------------------
        
    def method1(self, binary_number):   
        nums = list()
        for i in binary_number:
            nums.append(i)
            
        #nums[0] represents Fox --- nums[1] represents Chicken --- nums[2] represents Grain --- nums[3] represents me    
        if nums[0] == '0' and nums[1] == '0' and nums[2] == '0' and nums[3] == '1': 
            #I cant leave them alone
            return 0
        
        if (nums[0] == '0' and nums[1] == '0' and nums[3] == '1') or (nums[0] == '1' and nums[1] == '1' and nums[3] == '0'):
            #checking if fox and chicken are alone
            return 0
        
        if (nums[1] == '0' and nums[2] == '0' and nums[3] == '1') or (nums[1] == '1' and nums[2] == '1' and nums[3] == '0'):
            #checking if chicken and grain are alone
            return 0
        return nums
        
    
    def as_AM(self): #hugo
        for i in self.al:
            print(i)
    
        
    def problem(self):
        valid = 0
        list_of_valids = list()
        
        binar = '0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'
        binar = binar.split(' ')
        
        for index in range(len(binar)):
            binary_number = binar[index]
            
            valid = self.method1(binary_number)
            
            if valid != 0:
                list_of_valids.append(valid)
                
        print(list_of_valids)
        gra = Graph(len(list_of_valids))
        g.insert_edge(0,1)
        
        return

    
    def as_EL(self):
        g = []
        for source in range(len(self.al)):
            for dest in range(len(self.al[source])):
                g.append([source,dest])
        return g
        