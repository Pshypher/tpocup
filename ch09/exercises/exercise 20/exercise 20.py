# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:22:49 2018

@author: Pshypher
"""

# Program helps to find an uncapitalized seven letter word in which six of the
# seven letters use the same number on a telephone key pad
telephone_keypad_dict = {2: "abc",3: "def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",
                         8:"tuv",9:"wxyz"}

# open a file of word lists
file_pointer = open("wordList.txt", 'r')
word_list = []

# read each line of the file (a word) remove enclosing whitespaces and add the
# word to the list of words
for line_str in file_pointer:
    line_str = line_str.strip().lower()
    if len(line_str) == 7:
        word_list.append(line_str)
        
# get single number on telephone key pad whose letters make 6 out 7 letters in 
# a seven letter word
for word in word_list:
    digits_str = ''     # build a string of digits from the telephone key pad
    for key, val in telephone_keypad_dict.items():
        for char in word:
            if char in val:
                digits_str = digits_str + str(key)
        digits_set = set(digits_str)
    # count the number of times each item in the set appears in the string
    # of digits
    if len(digits_set) == 2:
        first_digit, second_digit = digits_set
        # either of both digits appears six times in the numbers dialed 
        # while the other appears once,display the word
        first_digit_count = digits_str.count(first_digit)
        second_digit_count = digits_str.count(second_digit)
        if first_digit_count==6 or second_digit_count==6:
            print(word)