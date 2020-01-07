# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 09:19:59 2018

@author: Pshypher
"""

def open_file():
    '''Prompts user for the name of a file containing a list of words, and 
    returns a file object that contains the list of words.'''
    found = False
    while not found:
        try:
            file_name = input("Enter file containing list of words: ")
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("*** unable to open file ***")
            
    return file_pointer

def get_anagrams_from_word_list(words_file_obj, anagrams_dict):
    '''Finds each word that is an anagram to another from the list of words.''' 
    for word_str in words_file_obj: # loop through word list
        word_str = word_str.strip().lower() 
        chars_list = list(word_str)
        # canonical representation of anagrams are as a 
        # sorted sequence of characters, used as keys in the dictionary
        chars_list.sort()
        key_str = ''.join(chars_list)
        if key_str in anagrams_dict:    # current word is an anagram
            # add the word to the list of anagrams
            anagrams_dict[key_str].add(word_str)
        else:   # create the canonical representation of an anagram (the key)
            # and assign to the key a set containing the original word 
            anagrams_dict[key_str] = {word_str} # prior to being sorted
            
def display_anagrams(anagrams_dict):
    '''Displays the list of words that are anagrams in the dictionary.'''
    print("\nAnagrams")
    print('-'*8)
    for key, val in anagrams_dict.items():
        if len(val) > 1:
            anagram_str = '\t'
            for word in val:
                anagram_str = anagram_str + word + ' '
            print(anagram_str)
            
def main():
    # open file containing list of words
    words_file_pointer = open_file()
    # empty dictionary maps the standard representation of anagrams to a list 
    # of words that appears to be anagrams of one another
    anagrams_dict = {}
    # update the dictionary to get words that are anagrams in the word list
    # and display all the anagrams in the word list
    get_anagrams_from_word_list(words_file_pointer, anagrams_dict)
    words_file_pointer.close()  # close the file object
    display_anagrams(anagrams_dict)
    
if __name__ == "__main__":
    main()
    
            
