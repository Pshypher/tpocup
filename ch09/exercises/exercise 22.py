# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 08:21:33 2018

@author: Pshypher
"""

# Program prompts user for an integer and prints out the integer using words
integer_word_dict = {1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",
                     7: "seven",8: "eight",9: "nine",0: "zero"}
# prompt user for a number
all_digits = False
while not all_digits:
    number_str = input("Enter a number: ")
    if number_str.isdigit():
        all_digits = True
    
# print the number entered in words
num_in_word = '' 
for digit in number_str:
    num_in_word = num_in_word + " " + integer_word_dict[int(digit)]
    
print(num_in_word)