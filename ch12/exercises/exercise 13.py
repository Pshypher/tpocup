# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:27:09 2018

@author: Pshypher
"""

class WholeNumber(object):
    
    def __init__(self, number:int=0):
        """Initializes an instance of the WholeNumber class."""
        if number >= 0:
            self.__number = number
        else:
            print('WholeNumber argument ({:d}) less than 0'.format(number))
            raise(ValueError)
            
    def __add__(self, param_WholeNumber):
        """Adds two WholeNumbers together. Returns a WholeNumber"""
        return WholeNumber(self.__number + param_WholeNumber.__number)
    
    def __sub__(self, param_WholeNumber):
        """Subtracts a WholeNumber from another. Returns a WholeNumber"""
        if self.__number - param_WholeNumber.__number < 0:
            print('Subtraction of WholeNumbers should not yield -ve values.')
            raise(ValueError)
        return WholeNumber(self.__number - param_WholeNumber.__number)
    
    def __mul__(self, param_WholeNumber):
        """Multiply two WholeNumbers together. Returns a WholeNumber"""
        return WholeNumber(self.__number * param_WholeNumber.__number)
    
    def __str__(self):
        """String representation of WholeNumber."""
        return "Value (" + str(self.__number) + ")"
    
# Sample code using the WholeNumber class
if __name__ == '__main__':
    try:
        a_whole_number = WholeNumber(15)
        another_whole_number = WholeNumber(4)
        print(a_whole_number + another_whole_number)
        print(a_whole_number * another_whole_number)
        print(a_whole_number - another_whole_number)
    except ValueError:
        pass

            
    