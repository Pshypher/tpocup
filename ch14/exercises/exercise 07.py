# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:48:25 2018

@author: Pshypher
"""

def open_file():
    '''Opens a file, reprompts user for filename if bad file name is given.'''
    found = False
    while not found:
        file_name = input('Enter file name: ')
        try:
            file_pointer = open(file_name, 'r')
        except IOError:
            print('Bad file name!')
        else:
            found = True
            
    return file_pointer

def read_file(file_pointer):
    '''Reads the file line by line and stores all the records in a list.
    Returns a list of lists.'''
    student_records_list = []
    for line_str in file_pointer:
        line_str = line_str.strip()
        line_list = line_str.split(',')
        student_records_list.append(line_list)
    
    file_pointer.close()
    
    return student_records_list
        
def main():
    in_file = open_file()
    records = read_file(in_file)
    print("{:12s} {:^4s} {:^4s}".format("Student Name,","ID","GPA"))
    print("-"*25)
    for name,s_id,gpa in records:
        print("{:<15s} {:>4s} {:>4s}".format(name,s_id,gpa))