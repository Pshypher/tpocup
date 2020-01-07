# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:07:54 2018

@author: Pshypher
"""
# Unless stated otherwise, vriables are assumed to be the type int
def open_file():
    '''Opens a file and returns the file object if found otherwise None'''
    try:
        file_name = input("Enter the name of file: ")
        in_file = open(file_name, 'r')
    except IOError:
        print("*** unable to open file ***")
        in_file = None
        
    return in_file

def student_scores(student_file, student_grade_dict):
    '''Build the dictionary mapping each student name to their total scores.'''
    for line_str in student_file:
        line_str = line_str.strip()
        if not line_str or line_str[:4] == 'Name':
            continue

        student_name, score_str = line_str.split()
        
        # Add previous score of a student to the current and otherwise
        # initialize the score to the current score and add the student_name,
        # score mapping to the dictionary
        student_grade_dict[student_name] = student_grade_dict.get(
                student_name, 0) + int(score_str)


def display_grades(names_grade_dict):
    '''Display the student names and scores in a nice format.'''
    print("{:10s} {:10s}".format("Names", "Scores"))
    print('-'*21)
    for key, val in names_grade_dict.items():
        print("{:10s} {:<10d}".format(key,val))
    

def main():
    student_file_1 = open_file()
    student_file_2 = open_file()
    
    all_student_grade_dict = {}
    
    if student_file_1 != None and student_file_2 != None: 
        student_scores(student_file_1, all_student_grade_dict)
        student_scores(student_file_2, all_student_grade_dict)
        display_grades(all_student_grade_dict)
    
    
    
    