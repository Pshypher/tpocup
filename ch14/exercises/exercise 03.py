# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:45:16 2018

@author: Pshypher
"""

def split_str(words_ints_str):
    '''Splits a string of words and digits into seperate list of words and 
    list of integers.'''
    words_ints_list = words_ints_str.split(' ')
    integers_lst = []
    words_lst = []
    for elem in words_ints_list:
        try:
            integers_lst.append(int(elem))
        except ValueError:
            words_lst.append(elem)
            
    return integers_lst, words_lst


        