#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 7 Algorithm design techniques
#Date of last modification: December 4th 2019
#Professor: Olac Fuentes
# #Purpose: The purpose of this lab is to understand randomized algorithms (Hamiltonian), 
#   backtracking, and Dynamic Programming
#TA: Anindita Nath
import random
import numpy as np
from datetime import datetime

def checkifconst(s1,s2):
    one = False
    two = False
    
    v = ['a','e','i','o','u']
    for i in range(len(v)):
        if s1 == v[i]:
            one = True
        if s2 == v[i]:
            two = True
            
    if one == two:
        return True
    else:
        return False

def edit_distance(first, second):
    
    d = np.zeros((len(first)+1, len(second)+1),dtype=int)
    d[0,:] = np.arange(len(second)+1)
    d[:,0] = np.arange(len(first)+1)
    
    for i in range(1,len(first)+1):
        for j in range(1,len(second)+1):
            if first[i-1] == second[j-1]:
                d[i,j] = d[i-1,j-1]
                
            else:
                isvalid = checkifconst(first[i-1],second[j-1])
                if isvalid == True:
                    n = [d[i,j-1], d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
                else:
                    n = [d[i,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
    return d[-1,-1]
                    
    
def cycle(g): 
    created_path = [-1] * len(g.am)
    created_path[0] = 0
    if hamcy(g,created_path,1) == False: 
        print ("No solution.")
        return False
    prin(g, created_path) 
    return True
  
def prin(g, path): 
    print ("Solution Exists: ")
    for v in path: 
        print(v, end = ' ')
    print(path[0], "\n")
    
def hamcy(g, path, pos): #checking if v is in path already
    if pos == len(g.am): 
        #last must connect to first 
        if g.am[path[pos-1] ][ path[0]] == 1: 
            return True
        else: 
            return False

    for vertex in range(1,len(g.am)):
        if valid(g,vertex, pos, path) == True: 
            path[pos] = vertex
            if hamcy(g,path, pos+1) == True: 
                return True
            path[pos] = -1
    return False
  
def valid(g, v, pos, path): 
    if g.am[path[pos-1]][v] == 0: #looking at the v we're in and the last node
        return False
    for vertex in path: #checking if this has already been seen
        if vertex == v: 
            return False
    return True


#----------------------------------------------------------------------
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



class DSF:
    # Constructor
    def __init__(self, sets):
        # Creates forest with 'sets' root nodes
        self.parent = np.zeros(sets,dtype=int)-1
        
    def find(self,i):
        # Returns root of tree that i belongs to
        if self.parent[i]<0:
            return i
        return self.find(self.parent[i])
    
    def union(self,i,j):
        # Makes root of j's tree point to root of i's tree if they are different
        # Return 1 if a parent reference was changed, 0 otherwise
        r1 = self.find(i)
        r2 = self.find(j)
        if r1 != r2:
            self.parent[r1] = r2
            return 1
        return 0 


def connected_components(g): #this is a code I got from Fuentes's disjoint set forest program
    vertices = len(g)
    components = vertices
    s = DSF(vertices) #calling DFS
    for v in range(vertices):
        for edge in g[v]:
            components -= s.union(v,edge)
    return components


def random_ham(vertices, edges, tries=3):  
    for i in range(tries):
        g = random_graph(vertices, edges) #creating random
        print('Graph',i,':',g)
        path = set()
        for i in range(len(g)):
            for edge in g[i]:
                if len(g[i]) == 2:
                    path.add(i)
                else:
                    path.add(-1)   
        #if the path contains a -1 it means that its not valid and it stops
        if ((-1) not in path) and (connected_components(g) < 2):
            print('True, path: ', path)
        else:
            print('False, path: ',path)
        print()
    return
        
def random_graph(vertices, edges, duplicate = True): #this will create a random graph
    g = [[] for i in range(vertices)]
    num = 0
    while num < edges:
        first = random.randint(0, vertices-1) #random
        second = random.randint(0, vertices-1) #random
        if (first < second) and (second not in g[first]):
            g[first].append(second) #creating edge
            if duplicate:
                g[second].append(first)
            num+=1
    for edg in range(len(g)):
        g[edg].sort()
    return g

#----------------------------------------------------------------------

print('Randomized Graph')

print(random_graph(4,4))
print()
print('------')
startTime = datetime.now() #starting time
print('3 tries to get see if it outputs a hamiltonian graph (randomized)')
random_ham(4,4)
print('Running time: ',datetime.now()-startTime)
print('---------')
print('Backtracking')
print('problem number 1: ')
startTime = datetime.now() #starting time
g = Graph(10)
g.insert_edge(0,1)
g.insert_edge(0,3)
g.insert_edge(1,3)
g.insert_edge(1,4)
g.insert_edge(2,0)
g.insert_edge(2,4)
g.insert_edge(3,0)
g.insert_edge(3,1)
g.insert_edge(4,0)
g.insert_edge(4,1)
g.insert_edge(5,1)
g.insert_edge(5,2)
cycle(g)
print('Running time: ',datetime.now()-startTime)

print('problem number 2: ')
startTime = datetime.now() #starting time
g2 = Graph(4)
g.insert_edge(0,1)
g.insert_edge(0,4)
g.insert_edge(1,0)
g.insert_edge(1,2)
g.insert_edge(1,3)
g.insert_edge(2,1)
g.insert_edge(2,4)
g.insert_edge(3,1)
g.insert_edge(4,0)
g.insert_edge(4,2)
cycle(g2)
print('Running time: ',datetime.now()-startTime)
print('-------')
print()
print('sand and sound: ')
print(edit_distance('sand','sound'))