# Word puzzle driver
# Assumes stateCapitals.txt file of one word per line

import string

def get_word_list():
    """ Return a list of words from a word_list.txt file . """
    data_file = open("stateCapitals.txt","r")
    word_list = [] # start with an empty word list
    for word in data_file: # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    data_file.close()
    return word_list

def puzzle(word_list):
    """Finds the Two U.S.state capitals that have a prefix that is the name
        of a month from the word list. """
    
    month_list = ["january","february","march","april","may","june","july",
                   "august","september","october","november","december"]
    
    for month in month_list:
        for capital in word_list:
            if capital[:len(month)]==month:
                print(capital)
            
word_list = get_word_list()
puzzle(word_list)