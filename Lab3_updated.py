# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:44:11 2019

@author: miria
"""
#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 3 Linked Lists
#Date of last modification: October 3rd 2019
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to learn how to modify linked lists
#TA: Anindita Nath

import math
from datetime import datetime

class Node(object):
    def __init__(self, data, next = None): #Creating nodes
        self.data = data
        self.next = next
        
    
        #-------------------------------------------------------------------------------------------------
        
class linked(object):
    def __init__(self, head = None, tail = None): 
        self.head = head #setting head
        self.tail = tail #setting tail
        
    #-------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------      
    #-------------------------------------------------------------------------------------------------
    
    
    def getLength(self): #gets length of linked list
        temp = self.head #temporary, saving head
        i = 0 #this will increment as it finds new nodes
        while temp is not None: 
            i = i+1
            temp = temp.next #moving to the next node
        return i #returns length 
    
    #-------------------------------------------------------------------------------------------------
    
#    def append(self,x): #this function will append new items
#        if self.head is None: #if it'ts empty, it will create a head and tail
#            self.head = Node(x) 
#            self.tail = self.head 
#        else:
#            self.tail.next = Node(x) #this will add the node after tail
#            self.tail = self.tail.next #redefining what the new tail is
#        
    #-------------------------------------------------------------------------------------------------   
    def Print(self): #this function will print the data
        t = self.head
        while t is not None:
            print(t.data, end=' ')
            t = t.next
        print()

    #-------------------------------------------------------------------------------------------------
        
    def Insert(self,i): #this function will insert new nodes

        if self.head is None:
            self.head = Node(i)
            self.tail = self.head
            
        temp = self.head #temporary head
        always_head = self.head #saved the head
        always_tail = self.tail #saved the tail 
    
        if i < always_head.data: #if i is less than the data of head
            self.head, self.head.next = Node(i),self.head #I am making i the head and the next one is head
        
        elif i > always_tail.data: #if i is greater than the tail
            self.tail.next = Node(i) #making the tail i
            self.tail = Node(i)
            

        while temp is not None:
            
            if i > temp.data and i <= temp.next.data: #checking if the new node
                tempss = temp.next  #saving the rest of the list
                temp.next = Node(i) #I am inserting the new node here
                temp.next.next = tempss #I am saving the nodes
            temp = temp.next #moving to the next node
        

#            self.tail.next = Node(i)
#            self.tail = self.tail.next
    #------------------------------------------------------------------------
        
    def Delete(self,i): #this function will delete nodes
        print("Element that we will be deleting is: ",i) 
        temp = self.head.next
        previous = self.head
   
        if i == self.head.data:
            self.head = self.head.next

            self.head = self.head.next #making head.next the new head
            
        if self.head is None:
            return None
        
        if self.head.next is None and i == self.head.data:
            self.head = None
            
        while temp is not None:
            if temp.data == i:
                previous.next = temp.next
            temp = temp.next
            previous = previous.next
        
            
    #-------------------------------------------------------------------------------------------------
    
        
    def IndexOf(self,i): 
        index = 0 #initialize counter
        temp = self.head #saving head
        while temp is not None: 
            index +=1 #incrementing index
            if temp.data == i: 
                return index #returns the position
            temp = temp.next #moving to next node
        return -1 #if not found, returns -1
    #-------------------------------------------------------------------------------------------------  
        
    def Clear(self):
        self.head = None #clears list
    #-------------------------------------------------------------------------------------------------
        
    def Min(self):
        if self.head is not None:
            return self.head.data #sorted list, head is the minimum
        else:
            return math.inf #if the list is empty, it returns inf
    #-------------------------------------------------------------------------------------------------
        
    def Max(self):
        if self.head is not None:
            return self.tail.data #sorted list, tail is the maximum
        else:
            return math.inf #if the list is empty, it returns inf
    #-------------------------------------------------------------------------------------------------
        
    def HasDuplicates(self):
        if self.head is None:
            return -1
        print("HasDuplicates")
        if self.head is not None:
            temp = self.head #saving head
            temp2 = temp.next #saving next
            while temp is not None and temp2 is not None: 
                if temp.data == temp2.data: #since it's a sorted list, it will check the next one to see if 
                    #they're identical
                    return True 
                temp = temp.next #moves to next
                temp2 = temp.next #moves to next
            return False #else returns false
        
    #-------------------------------------------------------------------------------------------------
        
    def Select(self,k):
        if k > self.getLength(): #if k is greater than the length of the list, it returns inf
            return math.inf
        
        temp = self.head #saving head
        ii = 0 #initializing counter
        while temp is not None:
            if k == ii:
                return temp.data #returns integer
            temp = temp.next #moving to next node
            ii = ii+1 #incrementing
        return
        
    #-------------------------------------------------------------------------------------------------
    
    
def Merge(first, second):  
    
    if first is None: #returning M list
        return second 
    
    elif M.head is None: #returning self list
        return first
    
    elif first.data <= second.data: 

        temporary = first #first will be saved first
        temporary.next = Merge(first.next, second) #making a recursive call, moving nodes
    else:
        temporary = second #second will be saved first
        temporary.next = Merge(first, second.next) #making a recursive call, moving nodes
        
    return temporary 
    
print("--------------------------------------------------------------")
print("------------------ Hello, welcome to Lab 3! ------------------")
print("--------------------------------------------------------------")
print()

self = linked()


M = linked()


merged = linked()

#********************************

print("-------------------- THIS IS self.Print: --------------------") 
startTime = datetime.now() #starting time
self.Print()
print("Time it took to print: ",datetime.now()-startTime) #printing time
print()

#********************************

print("-------------------- THIS IS self.Insert: --------------------") 
self.Insert(400)
self.Insert(4)
self.Insert(44)
self.Insert(101)
self.Insert(3)
self.Insert(9)
self.Insert(67)
self.Insert(404)
self.Print()

M.Insert(356)
M.Insert(5)
M.Insert(8)
M.Insert(301)
M.Insert(7)
M.Insert(350)
M.Insert(800)
M.Insert(700)
M.Insert(750)
M.Insert(670)


startTime = datetime.now() #starting time
print("inserting 99")
self.Insert(99)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
print("inserting 20")
self.Insert(20)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
print("inserting 6")
self.Insert(6)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
print("inserting -2")
self.Insert(-2)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Insert(80)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Insert(60)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Insert(68)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Insert(67)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()


#********************************

print("-------------------- THIS IS self.Delete: --------------------") 
startTime = datetime.now() #starting time
self.Delete(404)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Delete(-2)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Delete(400)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()
#********************************

print("-------------------- THIS IS self.Merge(): --------------------")
print("The original list for ((((self)))) is: ")
self.Print()
print("The original list for (((M))) is: ")

M.Print()
print("The new linked list is: ")

startTime = datetime.now() #starting time
merged.head = Merge(self.head, M.head)
print("Time it took to merge: ",datetime.now()-startTime) #printing time
merged.Print()
print()

#********************************

print("-------------------- THIS IS self.IndexOf(): --------------------") 
print("Finding 101: ")
startTime = datetime.now() #starting time
print(self.IndexOf(101)) 
print("Time it took to find: ",datetime.now()-startTime) #printing time

print("Finding 4: ")
startTime = datetime.now() #starting time
print(self.IndexOf(4))
print("Time it took to find: ",datetime.now()-startTime) #printing time

print("Finding an element that doesn't exist (23434324):  ")
startTime = datetime.now() #starting time
print(self.IndexOf(23434324))
print("Time it took to find: ",datetime.now()-startTime) #printing time
print()

#********************************
print("-------------------- THIS IS self.Clear(): --------------------")
print("I will clear the entire list")
startTime = datetime.now() #starting time
print(self.Clear())
print("Time it took to clear: ",datetime.now()-startTime) #printing time
print()
#********************************
print("-------------------- THIS IS self.Min(): --------------------")
print("The minimum number in the list is: ")
startTime = datetime.now() #starting time
print(self.Min())
print("Time it took to find min: ",datetime.now()-startTime) #printing time

self.Insert(1)
print("I am now appending 1")
print("The minimum number in the list is: ")
startTime = datetime.now() #starting time
print(self.Min())
print("Time it took to find min: ",datetime.now()-startTime) #printing time

print("I am now clearing the list")
print(self.Clear())
print()

#********************************
print("-------------------- THIS IS self.Max(): --------------------")
print("The maximum number in the list is: ")
startTime = datetime.now() #starting time
print(self.Max())
print("Time it took to find max: ",datetime.now()-startTime) #printing time

self.Insert(1)
print("I am now appending 1")
print("The maximum number in the list is: ")
startTime = datetime.now() #starting time
print(self.Max())
print("Time it took to find max: ",datetime.now()-startTime) #printing time

print()
#********************************

print("------------------ THIS IS self.HasDuplicates(): ------------------")
print("The list is: ")
self.Clear()
self.Insert(600)
self.Insert(100)
self.Insert(1000)
self.Insert(200)

self.Print()
startTime = datetime.now() #starting time
print(self.HasDuplicates())
print("Time it took to find max: ",datetime.now()-startTime) #printing time
self.Insert(200)
print("I am now appending 200")
print("The list is: ")

self.Print()
startTime = datetime.now() #starting time
print(self.HasDuplicates())
print("Time it took to find dup: ",datetime.now()-startTime) #printing time
print()

#********************************

print("-------------------- THIS IS self.Select(): --------------------")
print("List is now: ")
self.Print()
print("Smallest element index input is: ",1)
print("kth smallest element is: ")
startTime = datetime.now() #starting time
print(self.Select(1))
print("Time it took to find k: ",datetime.now()-startTime) #printing time

print("Smallest element index input is: ",4)
print("kth smallest element is: ")
startTime = datetime.now() #starting time
print(self.Select(4))
print("Time it took to find k: ",datetime.now()-startTime) #printing time

print("Smallest element index input is: ",100)
print("kth smallest element is: ")
startTime = datetime.now() #starting time
print(self.Select(100))
print("Time it took to find k: ",datetime.now()-startTime) #printing time
