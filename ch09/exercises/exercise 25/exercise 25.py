# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 11:31:26 2018

@author: Pshypher
"""

import string

# Program compares two historic documents, find the most common meaningful 
# words between the two documents and outputs them in alphabetical order.

def parse_file(document, words_set):
    '''Adds each word in the document to the words_set.'''
    for line_str in document:   # loop through each line in the file
        line_str = line_str.strip() # strip off whitespaces at the end of line
        words_list = line_str.split()
        for word in words_list:
            # remove whitespaces and punctuations from each word
            word = word.strip().strip(string.punctuation).lower()
            if len(word) > 3:   # exclude stop words such as (and,a,but, etc.)
                words_set.add(word)

# open two historic documents
file_name = input("Enter name of first historic document: ")
first_document = open(file_name, 'r')
file_name = input("Enter name of second historic document: ")
second_document = open(file_name, 'r')
first_document_words_set = set()
second_document_words_set = set()

# add words in both documents to the respective sets for comparison
parse_file(first_document, first_document_words_set)
parse_file(second_document, second_document_words_set)

# find the common words in both sets
common_words_set = first_document_words_set & second_document_words_set
# sort the common words alphabetically and print 
common_words_list = list(common_words_set)
common_words_list.sort()

print("\nCommon words")
print('-'*12)
word_count = 1
for word in common_words_list:
    if word_count % 5:
        print('{:<12s}'.format(word), end=' ')
    else:
        print('{:<12s}'.format(word), end='\n')
    word_count += 1
    