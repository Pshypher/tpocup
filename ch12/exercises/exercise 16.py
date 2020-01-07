# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 09:55:13 2018

@author: Pshypher
"""

class Clock(object):
    
    def __init__(self,hours=0,minutes=0,seconds=0):
        """Constructor for an instance of the Clock class."""
        for param in (hours,minutes,seconds):
            if not isinstance(param, int):
                self.__second,self.__minute,self.__hour = 0,0,0
                break
        else:
            self.__second = seconds % 60
            minutes = seconds//60 + minutes
            self.__minute = minutes % 60
            hours = minutes//60 + hours
            self.__hour = hours % 24
        
    def __str__(self):
        """String representation of the Clock instance."""
        return "({:02d}:{:02d}:{:02d})".format(self.__hour,self.__minute,
                self.__second)
        
    def __repr__(self):
        """Clock instance output in python shell."""
        # uses the Clock.__str__(self) method
        return self.__str__()
    
    def __add__(self, param):
        """Adds two Clock instances or a Clock instance and an integer 
        together. Returns a new Clock instance."""
        if isinstance(param, int):
            param = Clock(param,0,0)
        if isinstance(param, Clock):
            hours = self.__hour + param.__hour
            minutes = self.__minute + param.__minute
            seconds = self.__second + param.__second
            return Clock(hours,minutes,seconds)
        else:
            raise(TypeError)
            
    def __radd__(self,param):
        """Adds a Clock instance and an integer together (in reverse). Returns
        a Clock instance."""
        return self.__add__(param)
        

# Sample code demonstrating the use of the Clock class
if __name__ == '__main__':
    try:
        a_Clock = Clock(23,59,22)
        another_Clock = Clock(15,30,38)
        print("a_Clock", a_Clock)
        print("another_Clock", another_Clock)
        print("a_Clock + another_Clock =", a_Clock + another_Clock)
        print("another_Clock + a_Clock =", another_Clock + a_Clock)
        print("2 + a_Clock =", 2 + a_Clock)
        print("another_Clock + 10 =", another_Clock + 10)
        print("(23,59,59) + a_Clock =", (23,59,59) + a_Clock)
    except TypeError:
        print("Error, wrong type")
    
    
        