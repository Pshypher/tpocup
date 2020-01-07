# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:57:31 2018

@author: Pshypher
"""

class LinearEquation(object):
    
    def __init__(self,slope:float,intercept:float=0.0):
        """Initializes an instance of a LinearEquation."""
        self.__slope = slope
        self.__intercept = intercept
        
    def __str__(self):
        """Returns a string representation of a LinearEquation."""
        return "y = {:.2f}x + {:.2f}".format(self.__slope, self.__intercept)
    
    def __repr__(self):
        """Representation of LinearEquation instance in the interpreter."""
        return self.__str__()
    
    def value(self,x_flt:float):
        """Calculate the value of the function given x. Returns a float."""
        if type(x_flt) == int:
            x_flt = float(x_flt)
            
        if not isinstance(x_flt, float):
            raise(TypeError)
            
        return self.__slope * x_flt + self.__intercept
    
    def compose(self, param_LinearEquation):
        """Return a LinearEquation which is the result of the composition of
        two LinearEquations."""
        if not isinstance(param_LinearEquation, LinearEquation):
            raise TypeError
            
        slope = self.__slope * param_LinearEquation.__slope
        intercept = self.__slope * param_LinearEquation.__intercept + \
        self.__intercept
        return LinearEquation(slope,intercept)
    
    def __add__(self,param_LinearEquation):
        """Returns the sum of two LinearEquation."""
        if type(param_LinearEquation) != LinearEquation:
            raise TypeError
            
        slope = self.__slope + param_LinearEquation.__slope
        intercept = self.__intercept + param_LinearEquation.__intercept
        return LinearEquation(slope,intercept)
    
# sample code that demonstrates the use of the LinearEquation class
if __name__ == '__main__':
    try:
        a_linear_eq = LinearEquation(1, 1)
        other_linear_eq = LinearEquation(2, 5)
        print("a_linear_eq + other_linear_eq returns {}".format(
                a_linear_eq + other_linear_eq))
        print("a_linear_eq.compose(other_linear_eq) returns {}".format(
                a_linear_eq.compose(other_linear_eq)))
        print("other_linear_eq.value(2) returns {}".format(
                other_linear_eq.value(2)))
        print("other_linear_eq.compose(5.625) returns ".format(
                other_linear_eq.compose(5.625)))
    except TypeError:
        print('Error, wrong type.')