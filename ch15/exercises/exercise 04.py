# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:21:55 2018

@author: Pshypher
"""
import doctest
doctest.testmod()

def are_anagrams(word1, word2):
    """
    >>> are_anagrams("maria", 13)
    Traceback (most recent call last):
        ...
    ValueError: bad parameter,expected a string got 13
    >>> are_anagrams("fred", "joe")
    False
    >>> are_anagrams("iceman", "cinema")
    True
    """
    
    if type(word1) != str:
        raise ValueError("bad parameter,expected a string got {}".format(word1))
        
    if not isinstance(word2,str):
        raise ValueError("bad parameter,expected a string got {}".format(word2))
        
    #2. Sort the characters in the words
    word1_sorted = sorted(word1)    # sorted returns a sorted list
    word2_sorted = sorted(word2)

    #3. Check that the sorted words are identical.
    return word1_sorted == word2_sorted

print("Anagram Test")

# 1. Input two words, checking for errors now
valid_input_bool = False
while not valid_input_bool:
    try:
        two_words = input("Enter two space seperated words: ")
        word1,word2 = two_words.split()   # split the input string into a list
                                            # of words
        valid_input_bool = True
    except ValueError:
        print("Bad Input")

if are_anagrams(word1, word2):      # function returned True or False
    print("The words {} and {} are anagrams.".format(word1, word2))
else:
    print("The words {} and {} are not anagrams.".format(word1, word2))
    
