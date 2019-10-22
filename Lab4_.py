#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 4 BST and BTree
#Date of last modification: October 21st, 2019
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to learn how insert and access word embeddings
#   within btrees and bst
#TA: Anindita Nath

import numpy as np
from datetime import datetime
import sys

class WordEmbedding(object):
    def __init__(self,word,embedding):
        # word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)

class BST(object):
    # Constructor
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right      
      
        
def Search(T,k): #searchs for word
    if T == None:
        t = None
    elif T.data.word == k:
        t= T #saves emb
    elif T.data.word > k: 
        t=Search(T.left,k) 
    else:
        t=Search(T.right,k) 
    return t #returns the word embedding

        
def Insert(T,newdata): #T.word
    if T == None:
        T =  BST(newdata)
    
    elif T.data.word > newdata.word: #comparing
        T.left = Insert(T.left,newdata) #insert
    else:
        T.right = Insert(T.right,newdata) #insert
    
    return T #returns tree

    
def reading_file(word,T, numberofnodes):
    i = 1
    new_list = []
    while i <= int(numberofnodes):
        new_list.append(word[i])
        i+=1
        
    inserting = WordEmbedding(word[0], new_list) #creating word embedding

    T = Insert(T,inserting) #inserting word embedding
    return T
    

def reading_2_lines(line2):
    line2 = line2.split(' ') #reading the two words inside 
    
    
    line2[1] = line2[1].strip() 
    
    u = Search(T,line2[0]) #searches for word
    v = Search(T,line2[1]) #searches for word
    
    total = (np.dot(u.data.emb, v.data.emb)) / (np.linalg.norm(u.data.emb) * np.linalg.norm(v.data.emb)) #calculation
    
    
    print('Similarity',line2,'=',round(total,4)) #prints similarity
    return

def height(T):
    if T is None:
        return 0
    else:
        left_depth= 1 + height(T.left) #adding every time there is a left
        right_depth = 1 + height(T.right) #adding every time there is a right
        if left_depth < right_depth: #comparing to see which one is greater
            return right_depth
        else:
            return left_depth
        
        
def numofnodes(T):
    if T is None:
        return 0
    return 1 + numofnodes(T.left) + numofnodes(T.right)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data

def FindChild(T2,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T2.data)):
        if k.word < T2.data[i].word:
            return i
    return len(T2.data)
             
def InsertInternal(T2,i):
    # T cannot be Full
    if T2.isLeaf:
        InsertLeaf(T2,i)
    else:
        k = FindChild(T2,i)   
        if IsFull(T2.child[k]):
            m, l, r = Split(T2.child[k])
            T2.data.insert(k,m) 
            T2.child[k] = l
            T2.child.insert(k+1,r) 
            k = FindChild(T2,i)  
        InsertInternal(T2.child[k],i)   
            
def Split(T2):
    #print('Splitting')
    #PrintNode(T)
    mid = T2.max_data//2
    if T2.isLeaf:
        leftChild = BTree(T2.data[:mid],max_data=T2.max_data) 
        rightChild = BTree(T2.data[mid+1:],max_data=T2.max_data) 
    else:
        leftChild = BTree(T2.data[:mid],T2.child[:mid+1],T2.isLeaf,max_data=T2.max_data) 
        rightChild = BTree(T2.data[mid+1:],T2.child[mid+1:],T2.isLeaf,max_data=T2.max_data) 
    return T2.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T2,i):
    T2.data.append(i)  
    T2.data.sort(key = lambda WordEmbedding: WordEmbedding.word)

def IsFull(T2):
    return len(T2.data) >= T2.max_data
        
def Insert2(T2,i):
    if not IsFull(T2):
        InsertInternal(T2,i)
    else:
        m, l, r = Split(T2)
        T2.data =[m]
        T2.child = [l,r]
        T2.isLeaf = False
        k = FindChild(T2,i)  
        InsertInternal(T2.child[k],i)   
     
 
def Search2(T2,k):
    # Returns node where k is, or None if k is not in the tree

    for t in T2.data:
        if t.word == k.word:
            return t
    if T2.isLeaf:
        return None
    return Search2(T2.child[FindChild(T2,k)],k)

    
def readfile(word,T2, numofnodes):
    i = 1
    new_list = [] #creating a list with the number of items the user inputs
    while i <= int(numofnodes): #counter to access the number of items
        new_list.append(word[i])
        i+=1
    inserting = WordEmbedding(word[0], new_list) #creating word embedding
    Insert2(T2,inserting)
    
    
def reading_2_lines2(line2):
    line2 = line2.split(' ')
    line2[1] = line2[1].strip()
    one = WordEmbedding(line2[0], None) #saving word as embedding
    two = WordEmbedding(line2[1], None) #saving word as embedding
    
    u = Search2(T2,one) #searching to access embedding
    v = Search2(T2,two) #searching to access embedding
    
    total = (np.dot(u.emb, v.emb)) / (np.linalg.norm(u.emb) * np.linalg.norm(v.emb))
    
    
    print('Similarity',line2,'=',round(total,4))

def numofnodes2(T2):
    s = 1
    if not T2.isLeaf:
        for i in T2.child: #going into every child
            
            s += numofnodes2(i) #makes a recursive call to the children
        if T2.isLeaf:
            return 
    return s
   
def Height2(T2):
    if T2.isLeaf:
        return 0
    return 1 + Height2(T2.child[0])  #adding every time there is a child       
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
tree = input('-----------Welcome! Enter 1 for BST and 2 for BTree--------:')
if tree == '1':
    print("-----------------------------BST----------------------------")
    file = 'glove.6B.50d.txt'
    T = None
    number_of_nodes = input('enter the maximum number of items to store in a node: ')
    print('Reading word file to determine similarities')
    startTime = datetime.now() #starting time
    
    with open(file, encoding = 'utf-8-sig') as fp:
        for line in fp:
            line = line.split(' ')
            T = reading_file(line, T, number_of_nodes) #sending the line to method

    print('Number of nodes: ',numofnodes(T))
    print('Height: ' ,height(T))
    print('Running time for binary search tree construction:',datetime.now()-startTime)
  
    
    startTime = datetime.now() #starting time
    file2 = '2_words_per_line.txt'
    with open(file2, encoding = 'utf-8-sig') as fp:
        for line2 in fp:
            reading_2_lines(line2) #reading line per line of text file
            
    print('Running time for binary search tree query processing: ',datetime.now()-startTime)


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
elif tree == "2":
    print("BTree:")
    T2 = BTree([],max_data=5)
    numberoflines = 0
    file = 'glove.6B.50d.txt'
    numofitems = input('enter the maximum number of items to store in a node: ')
    startTime = datetime.now() #starting time
    
    
    with open(file, encoding = 'utf-8-sig') as fp:
        for line in fp:
            line = line.split(' ')
            readfile(line, T2,numofitems)

    print('Running time for binary search tree construction:',datetime.now()-startTime,) #printing time)
    print('Number of nodes: ',numofnodes2(T2))
    print('Height: ' ,Height2(T2))
    
    
    startTime = datetime.now() #starting time
    file2 = '2_words_per_line.txt'
    with open(file2, encoding = 'utf-8-sig') as fp:
        for line2 in fp:
            reading_2_lines2(line2) #reading line per line of text file
            
    print('Running time for binary search tree query processing: ',datetime.now()-startTime)