# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 06:39:16 2018

@author: Pshypher
"""
import numpy
import pylab
import random
import string


def get_common_letter(letter_count_dict):
    '''Returns the most occuring letter in the letter frequency dictionary.'''
    # A collection of count, letter pairs from the letter count dictionary
    count_letter_pair_list = list(zip(letter_count_dict.values(), 
                                      letter_count_dict.keys()))
    # sort the list of the (count, letter) pair tuple and return the highest
    # occuring letter from the result of the sort
    count_letter_pair_list.sort(reverse=True)
    count, letter = count_letter_pair_list[0]
    return letter
    
    
def frequency_of_letters(text_str: str, letter_count_dict: dict) -> None:
    '''Dictionary of letters and the number of times they appear in a 
    string of words, spaces are excluded.'''
    
    for char in text_str:   # get each char in the string add to the dictionary
        if char.isalpha():  # with an initial count of 1 if it is an alphabet
            char = char.lower()
            letter_count_dict[char] = letter_count_dict.get(char,0) + 1
            

def plot_bar_chart(letter_count_dictionary):
    '''Plots a bar chart of each letter in a string of characters against its 
    number of occurence in the string.'''
    letters_list = [key for key in letter_count_dictionary]
    counts_list = [val for val in letter_count_dictionary.values()]
    # get ticks as the keys/letters
    bar_width = 0.5
    x_values = numpy.arange(len(letters_list))
    pylab.xticks(x_values, letters_list)
    # create the bar graph
    pylab.bar(x_values,counts_list,width=bar_width,color='r')
    pylab.show()


def main():
    # generate a random sequence of 500 letters
    characters_list = list(string.ascii_letters + string.punctuation + 
                          string.whitespace) 
    random_chars = ''.join([random.choice(characters_list) for i in range(
            500)])
    # get the number of occurence of each letter in a string
    letter_count_dict = {}
    frequency_of_letters(random_chars, letter_count_dict)
    print("Highest occuring letter:", get_common_letter(letter_count_dict))
    
    plot_bar_chart(letter_count_dict)
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    