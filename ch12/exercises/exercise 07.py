# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:21:26 2018

@author: Pshypher
"""

class Course(object):
    
    def __init__(self, course_name:str, course_code:str, unit:int=1):
        """Constructor of a Course class."""
        self.__course_name = course_name
        self.__course_code = course_code
        self.__unit = unit
        
    def get_course_name(self):
        """Return course title."""
        return self.__course_name
    
    def get_course_code(self):
        """Return course code."""
        return self.__course_code
    
    def get_unit(self):
        """Return course credit weight."""
        return self.__unit
    
    def __str__(self):
        """String representation of an instance of the Course class."""
        return "course title \"{:s}\"\ncourse code ({:s})\n{:d} unit(s)."\
    .format(self.__course_name, self.__course_code, self.__unit)
    
    def __repr__(self):
        """Interpreter representation for a Course (during execution)."""
        return self.__str__()
    
class SemTranscript(object):
    
    def __init__(self, student_name:str, course_grades:list=[]):
        """Constructor for the Semester Transcipt class."""
        self.__student = student_name
        # course_grades is a list of (course, grade_str) pair 
        self.__course_grades = course_grades
        
        
    def grade_point_sum(self):
        """Calculate grade point sum for the semester."""
        grades = ['a','b','c','d','e','f']
        grades.reverse()
        total = 0
        for course,grade in self.__course_grades:
            total += grades.index(grade.lower()) * course.get_unit()
            
        return total
    
    def total_course_units(self):
        """Calculate the total credit weight per semester."""
        total = 0
        for course,grade in self.__course_grades:
            total += course.get_unit()
            
        return total
    
    def __add__(self,param_SemTranscript):
        """Calculate the cummulative grade point average for the year of the 
        same student."""
        if self.__student == param_SemTranscript.__student:
            course_grades = self.__course_grades + param_SemTranscript.__course_grades
            return SemTranscript(self.__student, course_grades)
        else:
            print("wrong student")
    
    def __str__(self):
        """String representation of Semeseter Transcript."""
        report_str = "student: {:s}\n\n".format(self.__student)
        for course,grade in self.__course_grades:
            report_str += " {:s}: {:s}\n".format(course.get_course_name(),grade)
        gpa = self.grade_point_sum() / self.total_course_units()
        report_str += "\ngrade point average - {:.2f}".format(gpa)
        
        return report_str