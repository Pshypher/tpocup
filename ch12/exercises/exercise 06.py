# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:19:25 2018

@author: Pshypher
"""

import math

def feet_to_meters(distance_ft: float) -> float:
    """Converts speed in feet per seconds to meters per second. 
    Returns a float."""
    return distance_ft * 0.3048
    
def calculate_degree(x: float, y: float) -> float:
    """Calculates the degree a segment from (0,0) to (x,y) makes with the 
    x-axis. Returns a float value."""
    # the arctan function returns values between -pi/2 and pi/2
    degree_arctan = math.degrees(math.atan2(y,x))
    if x < 0:   # line segment lies in the 2nd and 3rd quadrant
        degree = 180 + degree_arctan
    elif x > 0 and y < 0:
        degree = 360 + degree_arctan
    else:
        degree = degree_arctan
        
    return degree

class Velocity(object):
    
    def __init__(self,distance=0,time=None,direction=0,unit=0):
        """Initialize the properties of an instance of Velocity."""
        distance = feet_to_meters(distance) if unit != 0 else distance
        self.__speed = distance / time if isinstance(time, int) else 0
        self.__units = 'm/s','ft/s'
        self.__unit = self.__units[unit] if unit < 2 else self.__units[0]
        self.__direction = direction # direction in degrees
        self.__x = self.__speed * math.cos(math.radians(self.__direction))
        self.__y = self.__speed * math.sin(math.radians(self.__direction))
        
    def __add__(self, param):
        """Add two Velocity object. Returns the resultant Velocity."""
        # Calculate the speed 
        speed = math.sqrt((self.__x-param.__x)**2 +(self.__y-param.__y)**2)
        # Calculate the direction
        direction_flt = calculate_degree(self.__x+param.__x,self.__y+param.__y)
        net_velocity = Velocity(direction=direction_flt)
        net_velocity.set_speed(speed)
        return net_velocity
    
    def set_speed(self,speed):
        """Change the speed attribute of Velocity object."""
        self.__speed = speed
        
    def __str__(self):
        """String representation of a Velocity object."""
        return "{:.2f}{:s} @ {:.2f} degrees".format(self.__speed,self.__unit,
                self.__direction)
        