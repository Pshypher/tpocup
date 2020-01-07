# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:36:42 2018

@author: Pshypher
"""

class Sentence(object):
    
    def __init__(self,sentence_str):
        """Initializes an instance of the sentence class."""
        self.__sentence_str = sentence_str
        self.__words = sentence_str.split()
        
    def get_first_word(self):
        """Returns the first word of the Sentence."""
        return self.__words[0]
    
    def get_all_words(self):
        """Returns all words in the Sentence."""
        return self.__words
    
    def replace(self,index,new_word):
        """Change a word at a particular index to new_word."""
        self.__words[index] = new_word
        return ' '.join(self.__words)