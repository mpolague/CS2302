# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:34:03 2019

@author: 19158
"""
#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 6 AL, AM, and EL
#Date of last modification: November 15th, 2019
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to learn how to insert edges with AL, AM, and EL
#TA: Anindita Nath

import matplotlib.pyplot as plt
import numpy as np
#import graph_AL as graph
#import graph_AM as graph # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
import graph_EL as graph # Replace line 3 by this one to demonstrate edge list implementation
from datetime import datetime
    
if __name__ == "__main__":  
    
    plt.close("all")  
    g = graph.Graph(6)
    #Sg.problem()
    
    
    
    print('not directed not weighted')
    
    startTime = datetime.now() #starting time
    g = graph.Graph(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()    
    print()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print() 
    
    print('directed but not weighted')
    g = graph.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    print()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print('weighted but not directed')
    g = graph.Graph(6,weighted = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    print()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    
    print('directed and weighted')
    g = graph.Graph(6,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    print()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    print()
    print('Running time for binary search tree query processing: ',datetime.now()-startTime)
    
    #UNDER AM----------
    #print('The AM presentation of the Fox, Chicken, and Grain sack:')
    #g.problem()
    
    #UNDER AL----------
    #g.as_AM()
    print('The EL representation:')
    #print(g.as_EL())
    
    #UNDER EL----------

    
    #g1=g.as_AL()
    #g1.draw()
        

        
