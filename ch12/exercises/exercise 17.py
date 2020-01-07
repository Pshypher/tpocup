# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:07:51 2018

@author: Pshypher
"""

class Compass(object):
    
    def __init__(self,degrees:int=0,minutes:int=0):
        """Constructor for an instance of the Compass class."""
        if type(degrees) != int or not isinstance(minutes, int):
            self.__degrees = 0
            self.__minutes = 0
        else:
            minutes = 0 if minutes < 0 else minutes
            degrees = 0 if degrees < 0 else degrees
            self.__minutes = minutes % 60
            self.__degrees = (minutes//60 + degrees) % 360
            
    def __str__(self):
        """String representation of Compass instance."""
        return "bearing({0:d},{1:d})".format(self.__degrees,
                          self.__minutes)
        
    def __repr__(self):
        """Representation of an instance of the Compass class during execution
        in the python shell."""
        return "Degrees - {0:d}\nMinutes - {1:d}".format(self.__degrees,
                          self.__minutes)
        
    def __add__(self,param):
        """Adds two instances of the Compass class or a Compass instance and an
        integer together. Returns an instance of the Compass class."""
        if isinstance(param, int):
            param = Compass(param)
        if type(param) == Compass:
            degrees = self.__degrees + param.__degrees
            minutes = self.__minutes + param.__minutes
            return Compass(degrees,minutes)
        else:
            raise(TypeError)
            
    def __radd__(self, param):
        """Adds a Compass instance and an integer (in reverse). Returns a 
        Compass instance."""
        return self.__add__(param)
    
# Sample code demonstrating the use of the Compass class
if __name__ == '__main__':
    try:
        a_Compass = Compass(359,59)
        other_Compass = Compass(10,35)
        print("a_Compass =",a_Compass)
        print("a_Compass + other_Compass =",a_Compass + other_Compass)
        print("other_Compass + Compass(275,45) =", other_Compass + Compass(275,45))
        print("a_Compass + 45 =", a_Compass + 45)
        print("49 + other_Compass =", 49 + other_Compass)
        print("a_Compass + (185,31) =", a_Compass + (185,31))
    except TypeError:
        print("Error, wrong type")