# -*- coding: utf-8 -*-

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
    
    def append(self,x): #this function will append new items
        if self.head is None: #if it'ts empty, it will create a head and tail
            self.head = Node(x) 
            self.tail = self.head 
        else:
            self.tail.next = Node(x) #this will add the node after tail
            self.tail = self.tail.next #redefining what the new tail is
        
    #-------------------------------------------------------------------------------------------------   
    def Print(self): #this function will print the data
        temp = self.head #saving head
        while temp is not None:  #making sure that the node is not empty
            print(temp.data, end=' ') #prings data
            temp = temp.next #mmoving to the next node
        print()

    #-------------------------------------------------------------------------------------------------
        
    def Insert(self,i): #this function will insert new nodes
        print("---The number we will insert is: ",i.data, "---")
        temp = self.head #temporary head
        always_head = self.head #saved the head
        always_tail = self.tail #saved the tail

        
        while temp.next is not None:

            if i.data > temp.data and i.data < temp.next.data: #checking if the new node
                tempss = temp.next  #saving the rest of the list
                temp.next = i #I am inserting the new node here
                i.next = tempss #I am saving the nodes
            temp = temp.next #moving to the next node
            
        if i.data < always_head.data: #if i is less than the data of head
            self.head, self.head.next = i,self.head #I am making i the head and the next one is head
            
        elif i.data > always_tail.data: #if i is greater than the tail
            self.tail.next = i #making the tail i
    #-------------------------------------------------------------------------------------------------
        
    def Delete(self,i): #this function will delete nodes
        print("Element that we will be deleting is: ",i) 
        temp = self.head.next #I am saving head.next
        previous = self.head #I am saving head 
        always_head = self.head #I am saving head
        always_tail = self.tail #I am saving tail
        
        while temp is not None:
            if temp.data == i:
                previous.next = temp.next #deleting node
            temp = temp.next #moving to the next node
            previous = previous.next #moving to the next node

        if i == always_head.data:
            self.head = self.head.next #making head.next the new head
            
        elif i == always_tail.data: 
            while temp is not None:
                if temp.next is None:
                    self.tail = previous #making this the new tail
                temp = temp.next #moving to the next node
                previous = previous.next #moving to the next node
                
            self.tail = previous 

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
self.append(1)
self.append(3)
self.append(9)
self.append(12)
self.append(15)
self.append(18)
self.append(21)
self.append(24)
self.append(27)
self.append(30)
self.append(33)
self.append(36)
self.append(39)
self.append(42)
self.append(45)
self.append(93)
self.append(96)


M = linked()
M.append(2)
M.append(4)
M.append(6)
M.append(8)
M.append(10)
M.append(12)
M.append(14)
M.append(16)
M.append(18)
M.append(20)
M.append(3004)
M.append(3005)
M.append(3006)
M.append(3007)
M.append(10000)
M.append(30069)
M.append(30076)


merged = linked()

#********************************

print("-------------------- THIS IS self.Print: --------------------") 
startTime = datetime.now() #starting time
self.Print()
print("Time it took to print: ",datetime.now()-startTime) #printing time
print()

#********************************

print("-------------------- THIS IS self.Insert: --------------------") 
startTime = datetime.now() #starting time
new_nodee = Node(2800)
self.Insert(new_nodee)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
new_nodee = Node(2900)
self.Insert(new_nodee)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
new_nodee = Node(2999)
self.Insert(new_nodee)
print("Time it took to insert: ",datetime.now()-startTime) #printing time
self.Print()
print()
#********************************

print("-------------------- THIS IS self.Delete: --------------------") 
startTime = datetime.now() #starting time
self.Delete(0)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Delete(4)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()

startTime = datetime.now() #starting time
self.Delete(13)
print("Time it took to delete: ",datetime.now()-startTime) #printing time
self.Print()
print()

#********************************

print("-------------------- THIS IS self.Merge(): --------------------")
print("The original list for ((((self)))) is: ")
self.Print()
print("The original list for (((M))) is: ")
M.Print()
print("The new linked list is: ")
self.Print()


startTime = datetime.now() #starting time
merged.head = Merge(self.head, M.head)
print("Time it took to merge: ",datetime.now()-startTime) #printing time
merged.Print()
print()

#********************************

print("-------------------- THIS IS self.IndexOf(): --------------------") 
print("Finding 299: ")
startTime = datetime.now() #starting time
print(self.IndexOf(299)) 
print("Time it took to find: ",datetime.now()-startTime) #printing time

print("Finding 30069: ")
startTime = datetime.now() #starting time
print(self.IndexOf(30069))
print("Time it took to find: ",datetime.now()-startTime) #printing time

print("Finding an element that doesn't exist (30069):  ")
startTime = datetime.now() #starting time
print(self.IndexOf(30076))
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

self.append(1)
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

self.append(1)
print("I am now appending 1")
print("The maximum number in the list is: ")
startTime = datetime.now() #starting time
print(self.Max())
print("Time it took to find max: ",datetime.now()-startTime) #printing time

print()
#********************************

print("------------------ THIS IS self.HasDuplicates(): ------------------")
print("The list is: ")
self.append(9)
self.append(100)
self.append(1000)
self.append(2000)

self.Print()
startTime = datetime.now() #starting time
print(self.HasDuplicates())
print("Time it took to find max: ",datetime.now()-startTime) #printing time
self.append(2000)
print("I am now appending 2000")
print("The list is: ")

self.Print()
startTime = datetime.now() #starting time
print(self.HasDuplicates())
print("Time it took to find dup: ",datetime.now()-startTime) #printing time
print()

#********************************
self.append(11)
self.append(11)
self.append(12)
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