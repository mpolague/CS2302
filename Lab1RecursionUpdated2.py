#Course: CS 2302 Data Structures
#Programmer: Miriam Olague
#Lab 1 Recursion
#Date of last modification: September 8th
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to find the anagrams and display the time it took 
#   to find the anagrams.
#TA: Anindita Nath
#-------------------------------------------------------------------------------------------- 
from datetime import datetime
import sys
    
def scrambled(letters, _scrambled_, _creating_set_, _newSet_): 
    #This is part 1 of the assignment 
    if len(letters) == 0: #base case)
        _newSet_.add(_scrambled_) #adding the word into the new set
        _newSet_ = _newSet_.intersection(_creating_set_) #re-writing the set with the 
        #words that actually appear inside of words_alpha
        if len(_newSet_) == 0:
            print("This word has 0 anagrams. ")
    else: 
        for i in range(len(letters)): #letter at i will be scrambled
            _scram_letters_ = letters[i]
            _remain_ = letters[:i] + letters[i+1:] #letter will be removed from remain letters list
            scrambled(_remain_, _scrambled_ + _scram_letters_, _creating_set_, _newSet_) #calling method
        
#--------------------------------------------------------------------------------------------   
            
def noDup(letters, scram, _creating_set_, _newnewSet_): 
    #this is part 2 no duplicates of the assignment
    if len(letters) == 0: #base case
        _newnewSet_.add(scram) #adding the word into the new set
        _newnewSet_ = _newnewSet_.intersection(_creating_set_) #re-writing the set with the 
        #words that actually appear inside of words_alpha
    else:
        for i in range(len(letters)): #letter at i will be scrambled
            if letters[i+1:] != letters[:i+1]: #making sure that the partial word is a prefix of any word
                #in the word set and that every other character does not repeat itself
                _scr_l_ = letters[i] #saving character
                _rem_ = letters[:i] + letters[i+1:] #letter will be removed from remain letters list
                noDup(_rem_, scram + _scr_l_, _creating_set_, _newnewSet_) #calling method
   
#--------------------------------------------------------------------------------------------
def prefixes(a, scrams, _creating_set_, _newSet3_, prefs_set):
        #this is part 2 of the assignment
    if len(a) == 0: #base case
        _newSet3_.add(scrams) #adding the word into the new set
        _newSet3_.update(_newSet3_.intersection(_creating_set_)) #re-writing the set with 
        #the words that actually appear inside of words_alpha
    else:
        for i in range(len(a)): #letter at i will be scrambled
            if a in prefs_set: #making sure that the partial word is a prefix of any word in the word set 
                _scrs_l_ = a[i] #saving character
                _rems_ = a[:i] + a[i+1:] #letter will be removed from remain a list
                prefixes(_rems_, scrams + _scrs_l_, _creating_set_, _newSet3_, prefs_set) #calling method
#--------------------------------------------------------------------------------------------


print("----------")
print("Hello! Welcome to the main function!")
print("----------") 
fileName = input("Enter the File Name please!: ")
print("----------")
_creating_set_ = set(open(fileName, 'r').read().split()) #This is splitting the words and putting them into a set
size = len(_creating_set_)


_method_name_ = input("What method would you like to access? 'part1', 'noDup' (First part of Part2 of the assignment), or 'prefixes' (Second part of Part2 of the assignment?: ")
print("----------")

_word_input_ = input("Enter a word or empty string: ") #word will be utilized 
a = _word_input_
letters = _word_input_
letters2 = sorted(_word_input_) 
print("----------")
        

        #**************************************************
        
if _method_name_ == "part1": #calling scrambled()
    _newSet_ = set() #This is where I will store the anagrams that were found inside the document
    startTime = datetime.now() #I am starting time as we go inside part1
    
    scrambled(letters, '', _creating_set_, _newSet_) #calling method
    _newSet_ = sorted(_newSet_.intersection(_creating_set_))
    length_of_newSet = len(_newSet_)
    
    if len(_newSet_) == 0:
        print("This word has 0 anagrams. ")
    else:
            print("The word ", _word_input_, " has the following ", (length_of_newSet)-1, "anagrams: ")
    
    
    _newSet_.remove(_word_input_)
    
    for i in range(length_of_newSet):
        if i < (length_of_newSet)-1:
            print(_newSet_[i])
    
    
    print ("Time it took to find the anagrams of this word: ", datetime.now() - startTime) #I am stopping time as we finish with method part1
    print("----------")

        #**************************************************
        
#======================================================================================================================================================================= 
elif _method_name_ == "noDup": #calling noDup()
    print("You are now in Part 2.1 of the assignment. This is for no duplicates: ")
    
    _newnewSet_ = set() 
    startTime = datetime.now() #I am starting time as we go inside part2.1
    
    noDup(letters, '', _creating_set_, _newnewSet_)  #CALLING METHOD---
    
    _newnewSet_ = sorted(_newnewSet_.intersection(_creating_set_)) #I am saving the created set by the method noDup
    length_of_newSet2 = len(_newnewSet_)

        #**************************************************

    if len(_newnewSet_) == 0:
        print("This word has 0 anagrams. ")
    else:
        print("The word ", _word_input_, " has the following ", (length_of_newSet2)-1, "anagrams: ")
        
        
    _newnewSet_.remove(_word_input_)
    for i in range(length_of_newSet2):
        if i < (length_of_newSet2)-1:
            print(_newnewSet_[i])
            
            
    print ("Time it took to find the anagrams of this word: ", datetime.now() - startTime) #I am stopping time as we finish with method part2
    print("----------")
    
        #**************************************************
#======================================================================================================================================================================= 
elif _method_name_ == "prefixes":
    print("You are now in Part 2.2 of the assignment. This is for prefixes: ")
    _newSet3_ = set() #creating empty set
    prefs_list = list() #creating empty list
    prefs_set = set() #creating empty list
    creatings_list = list(_creating_set_) #converting set to list
    creatings_list = sorted(creatings_list) #sorted
    
    
    for i in range(len(creatings_list)): #iterating through every word
      temps_string = '' #blank
      temps_word = creatings_list[i] #saving a word temporarily here
      for j in range(len(temps_word)): #iterating through every character but the last one
          temps_string += temps_word[j] #adding next character
          prefs_list.append(temps_string) #adding prefix to the list
        
    for i in range(len(prefs_list)):
        temp = prefs_list[i]
        prefs_set.add(temp) #I am adding every element of the list into the set
        
    prefs_set = sorted(prefs_set)
    

    
    
    startTime = datetime.now() #I am starting time as we go inside part2.2
    prefixes(a, '', _creating_set_, _newSet3_, prefs_set) #CALLING METHOD ---
    
    
    print(a)
    _newSet3_ = sorted(_newSet3_.intersection(_creating_set_))
    _lenSet3_ = len(_newSet3_)
    
    if len(_newSet3_) == 0:
        print("This word has 0 anagrams. ")
    else:
        print("The word ", a, " has the following ", (_lenSet3_)-1, "anagrams: ")
        
    _newSet3_.remove(a)
    for i in range(_lenSet3_):
        if i < (_lenSet3_)-1:
            print(_newSet3_[i]) #I am printing the anagrams
            
            
    print ("Time it took to find the anagrams of this word: ", datetime.now() - startTime) #I am stopping time as we finish with method part2
    print("----------")
        
#======================================================================================================================================================================= 
    
else:
    print("Since you did not choose a valid method, you were kicked out of the program. Bye! Thank you for using the program. ")
    sys.exit() #exits program
    
#--------------------------------------------------------------------------------------------