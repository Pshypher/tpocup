# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 09:29:44 2018

@author: Pshypher
"""
from operator import itemgetter
import htmlFunctions
import string

# 1. prompt user for file name, read the file
def open_file():
    '''Prompts user for file name, opens the file and returns both the name of
    the file and the file descriptor object.'''
    found = False 
    while not found:
        try:
            file_name = input("Enter name of file: ")
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("*** unable to open file ***")
            
    return file_name, file_pointer
        
# 2. read and parse the file 
def read_file(words_dict, file_tuple):
    '''reads the file to a dictionary of words spoken by participants of a 
    debate, otherwise a list of words is returned for regular a document.
    returns a dictionary with the name of participant or file as key and the 
    list of words as value.'''
    file_name, file_descriptor = file_tuple
    # document is a debate if first line holds the name of the moderator
    HEADING = 1
    
    moderator_str = ''
    for line_str in file_descriptor:
        line_str = line_str.strip()
        if not line_str:    # skip empty lines
            continue
        line_list = line_str.split()    # split on whitespace
        # names of moderator is all uppercase seperated by a whitespace and
        # succeeded by a colon
        if HEADING: 
            # last name of speaker preceeded by a colon and 
            if line_list[1].isupper() and line_list[1][-1] == ':':
                moderator_str = line_list[1][:-1].lower()  # name of moderator
                # moderator is the 1st person to speak on a political debate
                speaker_str = moderator_str 
            HEADING = 0
            
        if moderator_str:   # document is a transcript of a political debate?
            # the transcript begins the line with name of participant each
            # time a different person speaks
            
            if len(line_list) > 1 and line_list[1].isupper() and \
            line_list[1][-1] == ':':
                speaker_str = line_list[1][:-1].lower()
                line_list[:2] = []
                # exclude the moderator and check if the participant name is 
                # already a key in the dictionary
                if speaker_str != moderator_str and speaker_str in words_dict:
                    words_dict[speaker_str].extend(line_list)
                # participant not yet in words_dict
                elif speaker_str != moderator_str:  
                    words_dict[speaker_str] = line_list
            else:   # add the words in other lines to the list of words spoken
                    # by the current participant
                if speaker_str != moderator_str:
                    words_dict[speaker_str].extend(line_list)
        else:   # otherwise,document is a regular file?
            if words_dict:
                words_dict[file_name].extend(line_list)
            else:
                file_name = file_name[:file_name.find('.')]
                words_dict[file_name] = line_list
                
# 3. make list of stop words from the document containing stop words
def make_stop_words(file_name, stop_words):
    '''makes a list of stop words to be excluded from the document whose 
    tag cloud ".html" file is made from the word frequency of the document.'''
    stop_words_file = open(file_name, 'r')
    
    for line_str in stop_words_file:
        line_str = line_str.strip()
        if line_str:
            stop_words.append(line_str)

# 4. remove all stop words, punctuations from the list of words by each 
#   candidate if the document is a political debate transcript or from the list 
#   for any other document.
def remove_stop_words(words_dict, stop_words):
    '''removes stop words, punctuations and other chars from each list of words
    in words_dict.'''
    for words_list in words_dict.values():
        i = 0
        while i < len(words_list):
            # remove whitespaces and punctuation chars from each word
            words_list[i] = words_list[i].strip().strip(
                    string.punctuation).lower()
            # remove empty strings and stop words from the list of words in 
            # words_dict
            if words_list[i].isalpha() and len(words_list[i]) > 3 and \
            words_list[i] not in stop_words:
                i = i+1
                continue
            else:
                words_list[i:i+1] = []
                
# 5. count the number of words in the document
def set_word_count(words_dict, words_frequency_dict):
    '''counts the words in a document or words spoken out during a dialogue. 
    returns a dictionary indexing another dictionary, the outer keys maps the 
    names of the speakers or the name of a file to another dictionary that
    contains word: count pairs.'''
    pass

    for key, val in words_dict.items():
        words_frequency_dict[key] = {}
        for word in val:
            words_frequency_dict[key][word] = words_frequency_dict[key].get(
                    word,0) + 1
            
def sort_word_count(words_frequency_dict):
    '''sorts the words of each particitant or an entire file alphabetically, 
    returns a dictionary with each key paired with a list of tuples where each 
    tuple is a (word,count) pair.'''
    for key in words_frequency_dict:
        # dictionary indexed by name of paricipant or file name,changed to a
        # list of tuples
        words_count_list = list(words_frequency_dict[key].items())
        # sort based on the count of each word
        words_count_list.sort(reverse=True, key=itemgetter(1))
        # get the word count for the 40 most frequently occuring words
        words_count_list[40:] = []
        words_count_list.sort() # sort remaining word,count pair alphabetically
        words_frequency_dict[key] = words_count_list
        

# 6. generate a tag cloud for the document
def main():
    stop_words = [] # initialize empty list for stop words
    words_dict = {} # initialize dictionary, key(name of participant), value
                    # (list of words spoken by participant)
    words_frequency_dict = {}
    file_name,file_descriptor = open_file()
    # parse the file into words_dict
    read_file(words_dict,(file_name,file_descriptor))
    # fill in the stop words
    make_stop_words("stopWords.txt",stop_words)
    # remove stop words from words_dict 
    remove_stop_words(words_dict,stop_words)
    set_word_count(words_dict,words_frequency_dict)
    sort_word_count(words_frequency_dict)
    
    # html document(s) containing tag cloud for each candidate if the file  
    # happens to be a political debate transcript or a single html tag cloud 
    # document for a regular file
    for title,word_count_pair in words_frequency_dict.items():
        body = ''
        word,high_count = max(word_count_pair,key=itemgetter(1))
        word,low_count = min(word_count_pair,key=itemgetter(1))
        for word,count in word_count_pair:
            body = body + htmlFunctions.makeHTMLword(
                    word,count,high_count,low_count) + ' '
        body = body.strip()
        box = htmlFunctions.makeHTMLbox(body)
        htmlFunctions.printHTMLfile(box,title)
        
if __name__ == "__main__":
    main()        