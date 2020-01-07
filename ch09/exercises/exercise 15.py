# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:16:04 2018

@author: Pshypher
"""

def to_lowercase(name_str: str) -> str:
    '''Converts each character in a name to lowercase ascii characters.Returns 
    a string.'''
    name_lower_str = ''
    for char in name_str:
        name_lower_str = name_lower_str + char.lower()
        
    return name_lower_str
        
def get_common_letters_1():
    '''Returns a list of common letters between the first and last 
    names of a person using a list.'''
    first_name_str = input("Enter first name: ")
    last_name_str = input("Enter last name: ")
    first_name_str = to_lowercase(first_name_str)
    last_name_str = to_lowercase(last_name_str)
    common_letters_list = []
    
    for char in first_name_str:
        if char in last_name_str and char not in common_letters_list:
            common_letters_list.append(char)
            
    return common_letters_list


def get_common_letters_2():
    '''Returns a collection of common letters between the first and 
    last names of a person using a set.'''
    first_name_str = input("Enter first name: ")
    last_name_str = input("Enter last name: ")
    first_name_str = to_lowercase(first_name_str)
    last_name_str = to_lowercase(last_name_str)
    return set(first_name_str) & set(last_name_str)


def get_distinct_letters():
    '''Uses set to find the set of letters in either one of the names but not
    in both.'''
    first_name_str = input("Enter first name: ")
    last_name_str = input("Enter last name: ")
    first_name_str = to_lowercase(first_name_str)
    last_name_str = to_lowercase(last_name_str)
    return set(first_name_str) ^ set(last_name_str)