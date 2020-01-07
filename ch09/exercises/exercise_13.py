# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 06:23:04 2018

@author: Pshypher
"""

# Gettysburg address analysis
# count words, unique words

def make_word_list(a_file):
    """Create a list of words from a file."""
    word_list = []      # 2. list of speech words: initialized to be empty
    
    for line_str in a_file:          # 3. read file line by line
        line_list = line_str.split() # 3a. split each line to a list of words
        for word in line_list:          # get words one at a time from list
            word = word.lower()         # make words lower case
            word = word.strip('.,')     # strip off commas and periods
            if word != "--":            # if the word is not "--"
                word_list.append(word)      # add the word to the speech list
    return word_list

def make_unique(word_list):
    """Create a set of unique words."""
    unique_set = set()    # set of unique words: initialized to be empty
    
    for word in word_list:          # get words one at a time from speech
        unique_set.add(word)
            
    return unique_set
           

################################

gba_file = open("gettysburg.txt", "r") # 1. open file for reading
speech_list = make_word_list(gba_file)
print("Speech Length: ", len(speech_list))
unique_set = make_unique(speech_list)
# 4. print the speech and its lengths
print(unique_set)
print("Unique Length: ", len(make_unique(speech_list)))