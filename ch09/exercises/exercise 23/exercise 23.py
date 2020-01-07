# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 08:50:43 2018

@author: Pshypher
"""

def get_original_word(prefix: str, words_file_pointer) -> None:
    '''Retrieves the original word from a word list with a prefix whose last
    letter is missing and prints it.'''
    for line_str in words_file_pointer:
        word = line_str.strip()
        if word[:-1] == prefix:
            print(word)
            
def main():
    # open file containing list of words
    file_pointer = open("wordList.txt", 'r')
    # prompt user for word with missing last letter.
    prefix_str = input("Enter word with last letter missing: ")
    # display list of words with the same prefix preceeding another letter
    get_original_word(prefix_str, file_pointer)
