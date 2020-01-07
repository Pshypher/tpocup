# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 09:55:13 2018

@author: Pshypher
"""

###########################################################################
## Class Time
###########################################################################

class Time(object):
    
    def __init__(self,hours=0,minutes=0,seconds=0):
        """Construct a Time using three integer variables."""
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
        """String representation of the Time instance."""
        return "({:02d}:{:02d}:{:02d})".format(self.__hour,self.__minute,
                self.__second)
        
    def __repr__(self):
        """Time instance output in the Python shell."""
        # uses the Time.__str__(self) method
        return "Class Time " + self.__str__()
    
    def from_str(self, time_str):
        """Updates the Time using the time_str in the format "hh:mm:ss"."""
        hour,minutes,seconds = time_str.split(':')
        self.__hour = int(hour.strip())
        self.__minute = int(minutes.strip())
        self.__second = int(seconds.strip())
    
    def __add__(self, param):
        """Adds two Time instances or a Time instance and an integer 
        together. Returns a new Time instance."""
        if isinstance(param, int):
            param = Time(param,0,0)
        if isinstance(param, Time):
            hours = self.__hour + param.__hour
            minutes = self.__minute + param.__minute
            seconds = self.__second + param.__second
            return Time(hours,minutes,seconds)
        else:
            raise(TypeError)
            
    def __radd__(self,param):
        """Adds a Time instance and an integer together (in reverse). Returns
        a Time instance."""
        return self.__add__(param)