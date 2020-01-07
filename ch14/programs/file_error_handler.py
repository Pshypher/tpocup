# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:19:35 2018

@author: Pshypher
"""

# all aspects of exceptions

def process_file(data_file):
    """Print each line of a line with its line number."""
    count = 1
    for line in data_file:
        print('Line ' + str(count) + ': ' + line.strip())
        count = count + 1
        
while True:     # loop forever: until "break" is encountered
    filename = input('Input a file to open: ')
    try:
        data_file = open(filename)
    except IOError:                     # we get here if file open failed
        print('Bad file name; try again')
    else:
        # no exception so let's process the file
        print('Processing file', filename)
        process_file(data_file)
        break       # exit "while" loop (but do "finally" block first)
    finally:        # we get here whether there was an exception or not
        try:
            data_file.close()
        except NameError:
            print('Going around again')
            
print('Line after try-except group')
        