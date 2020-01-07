# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:36:14 2018

@author: Pshypher
"""

def open_file():
    '''Open a .csv file where owners and their credit cards are stored.'''
    # sentinel variable, a flag to see if a file is in the current directory
    found = False
    while not found:    # keep prompting user until file is found
        try:
            file_name = input("Enter file name: ")
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:     # file not found
            print("*** unable to open file ***")
            
    return file_pointer

def read_file(file_pointer, credit_card_dict):
    '''Reads each line of the file and add a credit card owner and their 
    credit card numbers to the dictionary'''
    for line_str in file_pointer:
        line_str = line_str.strip()
        line_list = line_str.split(',')
        owner_str, credit_card = line_list
        first_name, last_name = owner_str.split()
        # add holder names and credit card number to dicitionary
        if (first_name, last_name) in credit_card_dict:
            credit_card_dict[(first_name, last_name)].append(credit_card)
        else:
            credit_card_dict[(first_name, last_name)] = credit_card

def main():
    # open file
    file_pointer = open_file()
    credit_card_dict = {}   # initialize an empty dictionary
    # add credit card details to dictionary from file
    read_file(file_pointer, credit_card_dict)
    
    # prompt user for the name of card holder
    card_holder_str = input("Name of credit card holder: ")
    if card_holder_str in credit_card_dict:
        print("Credit card(s) held by {}".format(card_holder_str))
        for card in credit_card_dict[card_holder_str]:
            print(card)
    else:
        print("{} has no credit card(s)".format(card_holder_str))
    
    