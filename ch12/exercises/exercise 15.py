# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 08:41:23 2018

@author: Pshypher
"""

def kilometer_to_miles(distance_flt):
    """Returns the distance measured in miles from the distance in kilometers."""
    return distance_flt * 0.621371

class Odometer(object):
    
    def __init__(self, distance_flt:float=0.0, unit_int:int=0):
        """Constructor an instance of the Odometer class."""
        units_tuple = "miles","kilometer"
        unit_int = unit_int if unit_int in (0,1) else 0
        self.__distance = distance_flt
        self.__unit = units_tuple[unit_int]
        
    def __str__(self):
        """String representation for an instance of the Odometer class."""
        return "total distance travelled {} {}".format(
                round(self.__distance, 1), self.__unit)
        
    def __repr__(self):
        """Format output of an Odometer instance in the python interpreter."""
        return "Distance: {:.1f}\nUnit: {}".format(self.__distance,
                          self.__unit)
        
    def __add__(self,distance_flt):
        """Adds distance_flt in miles to the total distance travelled as 
        measured by the Odometer."""
        if isinstance(distance_flt, int):
            distance_flt = float(distance_flt)
        if type(distance_flt) == float:
            if self.__unit == "kilometer":
                self.__distance = kilometer_to_miles(self.__distance)
            return round(self.__distance + distance_flt,1)
        else:
            raise(TypeError)
            
    def __radd__(self,distance_flt):
        """Adds distance_flt to the Odometer's measured distance in reverse."""
        return self.__add__(distance_flt)
    
    def __sub__(self,distance_flt):
        """Subtract distance_flt in miles from the distance travelled by a car 
        as measured by an Odometer."""
        if type(distance_flt) == int:
            distance_flt = float(distance_flt)
        if isinstance(distance_flt, float):
            if self.__unit == "kilometer":
                self.__distance = kilometer_to_miles(self.__distance)
            return round(abs(self.__distance - distance_flt),1)
        else:
            raise(TypeError)
            
    def __rsub__(self,distance_flt):
        """Subtracts the distance measured by the Odometer from distance_flt in
        units of miles."""
        if type(distance_flt) == int:
            distance_flt = float(distance_flt)
        if isinstance(distance_flt,float):
            if self.__unit == "kilometer":
                self.__distance = kilometer_to_miles(self.__distance)
            return round(abs(distance_flt - self.__distance),1)
        else:
            raise(TypeError)
            
# Sample code demonstrating the use of the Odometer class
if __name__ == '__main__':
    try:
        an_odometer = Odometer(12897.5528, 1)
        another_odometer = Odometer(4593.7113695, 0)
        print(another_odometer)
        print("an_odometer + 45082.169 = {}".format(an_odometer + 45082.169))
        print("3461.009035 + another_odometer = {}".format(
                3461.009035 + another_odometer))
        print("413495.072263 - an_odometer = {}".format(
                413495.072263 - an_odometer))
        print("another_odometer - 595.0291 = {}".format(
                another_odometer - 595.0291))
        print("an_odometer - another_odometer = {}".format(
                an_odometer - another_odometer))
    except TypeError:
        print('Error, wrong type')
        

    