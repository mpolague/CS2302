# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:55:24 2019

@author: miria
"""

#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 2 Bubble sort, Quick sort, and Modified Quick Sort
#Date of last modification: September 22th 2019
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to find the an element in position k,
#   learn about how to find an element with recursion.
#TA: Anindita Nath


import sys
from datetime import datetime
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------PART 1------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------SELECT BUBBLE---------------------------------------------------------

def select_bubble(L, k):
    print("This is select_bubble: ")
    size = len(L)

    for i in range(size):
        
        for j in range(0, size-i-1): #This iterates through the list
            if L[j] > L[j+1]: #this is checking if the element is greater than the next one
                temp = L[j] #saving value into temporary variable
                L[j] = L[j+1] #swapping
                L[j+1] = temp #swapping
            
    print("The sorted list is: ", L)
    
    returning = L[k] #returning element at position k
    return returning
    print("----------")
#-----------------------------------------------------------QUICKSORT----------------------------------------------------------
        
def partition(L,l,h): 
    i = ( l-1 ) #I am saving the index of smaller element 
    pi = L[h] #This is the pivot 
    
    for j in range(l, h): 
        if   L[j] <= pi: #comparing element with pivot
            
            i = i+1 #increment index of small by one
            temp = L[i] #saving it into a temporary variable
            L[i] = L[j] #swapping
            L[j] = temp #swapping
            
    temp2 = L[i+1] #I am saving it into a temporary variable
    L[i+1] = L[h] #swapping the positions of last element with new one
    L[h] = temp2 #saving temp2 into high
    return(i+1)  #increment
  

def select_quick(L,low,high, k): 
    if low < high: 
        pi = partition(L,low,high)  #saving the call here
  
        select_quick(L, low, pi-1, k) #calling itself to keep on sorting
        select_quick(L, pi+1, high, k) #callign itself to keep on sorting
        
    return L[k] #returning the element at position k
    
#-----------------------------------------------------------MODIFIED QUICK-------------------------------------------------------
    
def select_modified_firstsplit(L, k):
    #this is the function that is making the first split and returnig the list that has 
    #   the kth element
    left = [] #temporary 
    equal = [] #temporary
    right = [] #temporary
    
    if len(L) > 1:
        pi = L[0] #making pivot L[0]
        for i in L: #iterating through the whole list
            if i < pi: #appending if i is less than pivot
                left.append(i)
            elif i == pi: #appending if i is equal to the pivot
                equal.append(i)
            elif i > pi: #appending if i is greater than the pivot
                right.append(i)
                
    for i in range(len(equal)): #I am adding the number that was the pivot to right
        right.append(equal[i])

    
    
    if k > len(left): #This is checking if k is inside left or not
        return(right, len(left)) #if k is greater than the length of left, it returns right
  
    else:
        return(left, len(left)) #if k is within the length of left, it returns left
    
        
def select_modified_quick(new, low, high, two, k): #this is modified quick sort

    if low< high: 
        pi = partition(new,low,high) #saving the call here
        
        select_modified_quick(new, low, pi-1, two, k) #calling itself to keep sorting
        select_modified_quick(new, pi+1, high,two, k) #calling itself to keep sorting
    kk = k-two #k is the number the user entered, and I am subtracting 'two' because
        #'two' represents the length of length of left, so that way it returns the right
        #value inside of right
    return new[kk]
        
                
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------PART 2------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------STACK-------------------------------------------------------------

def quick_stack(L, low, high):
    length = high - low + 1 #this is length of list/arr
    s = [0] * length #this is the stack I'm creating, size of the list/array
   
    upmost = L[-1] #top of stack
    

    upmost = upmost + 1 #incrementing top's value
    s[upmost] = low #saving the value of low here
    upmost = upmost + 1 #incrementing top's value
    s[upmost] = high #saving high's value here

  
    while upmost >= 0:  #popping
  
        # This is popping high and low
        high = s[upmost] #saving the top in high
        upmost = upmost - 1 #decrement index
        low = s[upmost] #saving value of top-1
        upmost = upmost - 1 #decrement index, index out of range error if taken out
        pi = partition(L, low, high)  #calling method partition and saving it as pivot
  #--------------
        if pi-1 > low: #checking left side of pivot
            
            upmost = upmost + 1 #incrementing index
            s[upmost] = low #saving value
            upmost = upmost + 1 #incrementing index
            s[upmost] = pi - 1 #saving pivot-1
  #--------------
        if pi + 1 < high:  #checking right side of pivot
            
            upmost = upmost + 1 #incrementing index
            s[upmost] = pi + 1 #saving pivot+1
            upmost = upmost + 1 #incrementing index
            s[upmost] = high #saving value
  #--------------     
  
    print("The sorted array is: ",L) #printing sorted array
    return L[k] #returning element at position k
#-------------------------------------------------------------WHILE LOOP------------------------------------------------------
        
def while_loop(L, low, high, k):
    length = high - low +1
    new_list = [0] * length
    temp = high
    
    for temp in range(len(L)):
        while temp != low:
            pi = partition(L,low,high)
            new_list.append(pi)
            temp = temp-1
            
        
    print(new_list)
    return new_list[k]
    
#===============================================================================================================================
#===============================================================================================================================

L = [6, 4, 1, 0, 12, 9, 30, 15, 2, 30, 60, 4, 19, 33, 40, 2, 16, 17, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
     3, 3, 12, 12, 3, 123, 5, 6, 4, 1, 0, 12, 9, 30, 15, 2, 30, 60, 4, 19, 33, 40, 2, 16, 17, 10, 3, 3, 3, 3, 3, 3, 3, 3, 
     3, 3, 3, 3, 12, 12, 3, 123, 5, 6, 4, 1, 0, 12, 9, 30, 15, 2, 30, 60, 4, 19, 33, 40, 2, 16, 17, 10, 3, 3, 3, 3, 3, 3, 
     3, 3, 3, 3, 3, 3, 12, 12, 3, 123, 5, 3, 3, 12, 12, 3, 123, 5, 6, 4, 1, 0, 12, 9, 30, 15, 2, 30, 60, 4, 19, 33, 40, 2, 
     16, 17, 10, 3, 3, 3, 3, 3, 3, 3452, 3, 3, 3, 3, 3, 12, 12, 3, 123, 5, 6, 4, 
     1, 0, 12, 9, 30, 15, 2, 30, 60, 4, 19, 33, 434235, 2, 16, 17, 10, 3, 60, 3, 3, 3, 3, 
     3, 3, 3, 3, 3, 34234, 12, 12, 3, 123, 5]

#YOU CAN ALSO ASK THE USER TO ENTER A LIST THEMSELVES
"""L = []
size = int(input("What is the size of the list you want to create?: "))
for i in range(0, size):
    num = input("Please enter number: ")
    L.append(num)"""

print("This is the list: ", L)
k = int(input("Please enter the kth smallest element you are looking for: "))

part = input("part1 (1) or part2 (2)?: ")
n = len(L) 

if part == '1':
    print("------------------------------------------------------")
    print("----------Hello, welcome to Part 1 of Lab 2!----------")
    print("------------------------------------------------------")
    bullet = input("What bullet of Part 1 would you like to access? bubble (b), quick (q), or modified (m): ")
    
        #****************************************************
    if bullet == "b":
        startTime = datetime.now() #starting time
        print("Element at position ", k, "is: ", select_bubble(L, k))
        print("Time it took to sort and return element: ",datetime.now()-startTime) #printing time
        print("----------")
        
        #****************************************************
        
    elif bullet == "q":
        startTime = datetime.now() #starting time
        
        print("This is select_quick: ")
        print("Element at position ", k, "is: ", select_quick(L,0,n-1, k))  #0 is the beginning of list, n-1 is the last element
        print("Sorted list is: ", L)
        print("Time it took to sort and return element: ",datetime.now()-startTime) #printing time
        
        print("----------")
        
        #****************************************************
        
    elif bullet == "m":
        
        startTime = datetime.now() #starting time
        
        L2 = select_modified_firstsplit(L, k) #splitting it into two sub lists
        one = L2[0] #this is the new list
        two = L2[1] #this is the length of left

        
        
        print("This is select_quick_modified: ")
        print("Element at position ",k,"is: ",select_modified_quick(one, 0, len(one)-1, two, k)) #CALLING METHOD
        #0 is the beginning of list, len(one) is the last element of new list
        print("Sorted list is: ",one)
        print("Time it took to sort and return element: ",datetime.now()-startTime) #printing time
        print("----------")
        #****************************************************
        
    else:
        sys.exit()

#===============================================================================================================================
#===============================================================================================================================
if part == '2': 
    print("------------------------------------------------------")
    print("----------    Welcome to Part 2 of Lab 2!   ----------")
    print("------------------------------------------------------")
    
    bullet2 = input("What bullet of Part 2 would you like to access? 1 or 2: ")
    
    if bullet2 == '1':
        startTime = datetime.now() #starting time
        print("Implement quicksort using a stack instead of recursion: ")
        print("Element at position ",k, "is: ",quick_stack(L, 0, n-1)) #0 is the beginning of the list,
        #n-1 is the last element in the list
        print("Time it took to sort and return element: ",datetime.now()-startTime) #printing time

    elif bullet2 == '2':
        startTime = datetime.now() #starting time
        print("Implement select_modified_quick(L, k) using a while loop without stacks or recursion: ")
        print("Element at position ",k,"is:",while_loop(L, 0, n-1, k)) #0 is the beginning of the list, n-1 is the last element in the list
        print("Time it took to sort and return element: ",datetime.now()-startTime) #printing time
        
    else:
        sys.exit()
#===============================================================================================================================
#===============================================================================================================================
else:
    sys.exit