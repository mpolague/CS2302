# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:31:48 2019

@author: 19158
"""

# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as graph
#import graph_EL as graph # Replace line 3 by this one to demonstrate edge list implementation

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int) -1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if source>=len(self.am) or dest>=len(self.am) or source<0 or dest<0:
            print('Error, vertex number out of range')

        else:
            if self.directed:
                self.am[source][dest] = 1
                if self.weighted:
                    self.am[source][dest] = weight
    

            if not self.directed:
                self.am[source][dest] = 1
                self.am[dest][source] = 1
                if self.weighted:
                    self.am[source][dest] = weight
                    self.am[dest][source] = weight
                
                
               
        
    def delete_edge(self,source,dest):
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            if not self.directed:
                deleted = self.am[source][dest] = -1
                deleted = self.am[dest][source] = -1
            else:
                deleted = self.am[source][dest] = -1
                
        if not deleted:        
            print('Error, edge to delete not found')   
        
        
                
    def display(self):
        print(self.am)
     
    def draw(self):
        return 
    
    def as_AL(self):
        g = graph.Graph(6)
        
        for i in self.am[self.source]:
            print(i)
            
        #g.insert_edge(self,source,dest,weight=1)
        return
    
    
    #--------------------------------------------------------
    
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
            
        gra = Graph(4)
        gra.insert_edge(0,2)
        gra.insert_edge(0,3)
        gra.insert_edge(1,3)
        gra.insert_edge(2,3)
        gra.display()
        gra.draw() 
        
        
        return
                
                    
            
    
    
        
