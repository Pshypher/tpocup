# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:21:55 2018

@author: Pshypher
"""

import os
import string
from gettysburg_words import *


def process_line(line, word_count_dict):
    '''Process the line to get lowercase words to add to the dictionary.'''
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        # ignore the '--' that is in the file and eliminate stop words
        # such as a, and, but, etc.
        if word != '--' and len(word) > 3:
            word = word.lower()
            word = word.strip()
            # get commas, periods and other puctuation out as well
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

            
def add_word(word, word_count_dict):
    '''Update the word frequency: word is the key, frequency is the value.'''
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
        

def pretty_print(word_count_dict):
    '''
    >>> pretty_print(ALL_GTY_WORDS_DICT)
    Word       Count      
    _____________________
    that         13 
    here         8  
    nation       5  
    have         5  
    this         4  
    dedicated    4  
    they         3  
    shall        3  
    people       3  
    great        3  
    dead         3  
    >>> pretty_print(SOME_GTY_WORDS_DICT)
    Word       Count      
    _____________________
    here         8  
    have         5  
    >>> pretty_print(SINGLE_COUNT_WORDS_DICT)
    Word       Count      
    _____________________
    '''
    # create a list of tuples, (value, key)
    # value_key_list = [(val, key) for key val in d.items()]
    value_key_list = []
    for key,val in word_count_dict.items():
        value_key_list.append((val,key))
    # sort method sorts on list's first element, the frequency.
    # Reverse to get biggest first
    value_key_list.sort(reverse=True)
    # value_key_list = sorted([(v,k) for k,v in word_count_dict.items()], reverse=True)
    print('{:11s}{:11s}'.format('Word', 'Count'))
    print('_'*21)
    for val,key in value_key_list:
        if val > 2: # print only words that occurs more than twice
            print('{:12s} {:<3d}'.format(key,val))
            
def main():
    """
    >>> main()
    Length of the dictionary: 104
    Word       Count      
    _____________________
    that         13 
    here         8  
    nation       5  
    have         5  
    this         4  
    dedicated    4  
    they         3  
    shall        3  
    people       3  
    great        3  
    dead         3  
    """
    os.chdir("..\\..\\ch09\\programs")
    global word_count_dict
    word_count_dict={}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    print('Length of the dictionary:',len(word_count_dict))
    pretty_print(word_count_dict)
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()