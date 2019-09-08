#Programmer: Miriam Olague
#Lab 1 Recursion
#Date is due: 09/06/2019
#Professor: Olac Fuentes
#Purpose: The purpose of this lab is to find the anagrams and display the time it took 
#   to find the anagrams.
#-------------------------------------------------------------------------------------------- 
from datetime import datetime
import sys
    
def scrambled(letters, _scrambled_, _creating_set_, _newSet_): 
    #This is part 1 of the assignment 
    if len(letters) == 0: #base case)
        _newSet_.add(_scrambled_) #adding the word into the new set
        _newSet_ = _newSet_.intersection(_creating_set_) #re-writing the set with the words that actually appear inside of words_alpha
    else: 
        for i in range(len(letters)): #letter at i will be scrambled
            _scram_letters_ = letters[i]
            _remain_ = letters[:i] + letters[i+1:] #letter will be removed from remain letters list
            scrambled(_remain_, _scrambled_ + _scram_letters_, _creating_set_, _newSet_) #calling method
        
#--------------------------------------------------------------------------------------------   
            
def noDup(letters, scram, _creating_set_, _newnewSet_, pref_set): 
    #this is part 2 of the assignment
    if len(letters) == 0: #base case
        _newnewSet_.add(scram) #adding the word into the new set
        _newnewSet_ = _newnewSet_.intersection(_creating_set_) #re-writing the set with the words that actually appear inside of words_alpha
    else:
        for i in range(len(letters)): #letter at i will be scrambled
            if (letters in pref_set) and (letters[i+1:] != letters[:i+1]): #making sure that the partial word is a prefix of any word in the word set and that every other character does not repeat itself
                _scr_l_ = letters[i] #saving character
                _rem_ = letters[:i] + letters[i+1:] #letter will be removed from remain letters list
                noDup(_rem_, scram + _scr_l_, _creating_set_, _newnewSet_, pref_set) #calling method
   
#--------------------------------------------------------------------------------------------


print("----------")
print("Hello! Welcome to the main function!")
print("----------") 
fileName = input("Enter the File Name please!: ")
print("----------")
_creating_set_ = set(open(fileName, 'r').read().split()) #This is splitting the words and putting them into a set
size = len(_creating_set_)


_method_name_ = input("What method would you like to access?: ")
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
    
    if _newSet_ == 0:
        print("This word has 0 anagrams. ")
    else:
        print("The word ", _word_input_, " has the following ", length_of_newSet, "anagrams: ")
    

    for i in range(length_of_newSet):
        print(_newSet_[i])
    
    
    print ("Time it took to find the anagrams of this word: ", datetime.now() - startTime) #I am stopping time as we finish with method part1
    print("----------")

        #**************************************************

elif _method_name_ == "part2": #calling noDup()
    
    pref_list = list() 
    pref_set = set('') 
    creating_list = list(_creating_set_) #converting set to list
    creating_list = sorted(creating_list) #sorted
    
    for i in range(len(creating_list)): #iterating through every word
      temp_string = '' #blank
      temp_word = creating_list[i] #saving a word temporarily here
      for j in range(len(temp_word)-1): #iterating through every character but the last one
          temp_string += temp_word[j] #adding next character
          pref_list.append(temp_string) #adding prefix to the list
          
    pref_set.update(pref_list) #I am putting the elements of the list inside of a set

    _newnewSet_ = set() 
    startTime = datetime.now() #I am starting time as we go inside part2
    
    noDup(letters, '', _creating_set_, _newnewSet_, pref_set)  
    
    _newnewSet_ = sorted(_newnewSet_.intersection(_creating_set_)) #I am saving the created set by the method noDup
    length_of_newSet2 = len(_newnewSet_)

        #**************************************************

    if _newnewSet_ == 0:
        print("This word has 0 anagrams. ")
    else:
        print("The word ", _word_input_, " has the following ", length_of_newSet2, "anagrams: ")
        
        
    for j in range(length_of_newSet2):
        print(_newnewSet_[j])
    #print("The word ", _word_input_, "has the following anagrams: ")
    print ("Time it took to find the anagrams of this word: ", datetime.now() - startTime) #I am stopping time as we finish with method part2
    print("----------")
    
        #**************************************************
        
else:
    print("Since you did not choose a valid method, you were kicked out of the program. Bye! Thank you for using the program. ")
    sys.exit() #exits program
    
#--------------------------------------------------------------------------------------------   