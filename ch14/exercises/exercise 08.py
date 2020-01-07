# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:38:09 2018

@author: Pshypher
"""

import os,string

def read_file(file_pointer):
    '''Reads a file and creates a list of rows of words in each line of the 
    file. Returns a list of lists.'''
    words_in_file = []
    for line_str in file_pointer:
        line_list = line_str.strip().split(' ')
        words_per_line = []
        for word in line_list:
            word = word.strip().strip(string.punctuation)
            if word.isalpha():
                words_per_line.append(word.lower())
        try:
            last_word = words_per_line.pop()
            words_per_line.append(last_word)
        except IndexError:
            print('\nempty line!')
        else:
            words_in_file.append(words_per_line)
            
    return words_in_file
            
def main():
    # open file
    try:
        file_str = input("Enter file name: ")
        dir_str = input("Enter directory path: ")
        path_str = os.path.join(dir_str, file_str)
        file_pointer = open(path_str, 'r')
    except IOError:
        print('Bad file name!')
    else:
        # parse file for words, place each word that contains only alphabet in a 
        # list and each line of words in an outer list of lists
        file_contents_lst = read_file(file_pointer)
        print('\n' + '-'*80)
        for row in file_contents_lst:
            line_str = ' '.join(row)
            print(line_str)
    finally:
        try:
            file_pointer.close()
        except NameError:
            print('Reference to file descriptor not found!')
    