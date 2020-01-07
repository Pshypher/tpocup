# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:09:42 2018

@author: Pshypher
"""

class Compound(object):
    
    def __init__(self,name:str,formula:str):
        """Constructor for a chemical Compound."""
        self.__name = name
        self.__formula = formula
        
    def __add__(self, param_Compound):
        """Adds two chemical compounds together."""
        print("{:s} + {:s}".format(self.__formula, param_Compound.__formula))
        
    def __str__(self):
        """String representation of chemical Compound."""
        return "{:s} ({:s})".format(self.__name, self.__formula)