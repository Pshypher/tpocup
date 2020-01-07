# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:06:37 2018

@author: Pshypher
"""
import math

class Logarithm(object):
    
    def __init__(self, base:int, number:float):
        """Constructs an object of the Logarithm class."""
        self.__base = base
        self.__number = number
        
    def __add__(self, param_Logarithm):
        """Adds two numbers of similar or different bases together."""
        if self.__base != param_Logarithm.__base:
            # convert both instances of the Logarithm class to a canonical base
            # such as base 2 or base 10
            base = 10
            for log_obj in (self,param_Logarithm):
                log_obj.__number = base ** (math.log10(log_obj.__number)/
                                          math.log10(log_obj.__base))
                log_obj.__base = base
        else:
            base = self.__base
            
        return Logarithm(base, self.__number+param_Logarithm.__number)
    
    def __sub__(self,param_Logarithm):
        """Subtracts two numbers of similar or different bases together."""
        if self.__base != param_Logarithm.__base:
            # convert both instances of the Logarithm class to a canonical base
            # such as base 2 or base 10
            base = 10
            for log_obj in (self,param_Logarithm):
                log_obj.__number = base ** (math.log10(log_obj.__number)/
                                          math.log10(log_obj.__base))
                log_obj.__base = base
        else:
            base = self.__base
            
        return Logarithm(base, self.__number-param_Logarithm.__number)
    
    def __str__(self):
        """String representation of Logarithm instance."""
        return "number {:.2f}, base ({:d})".format(self.__number,self.__base)