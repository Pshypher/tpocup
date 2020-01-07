# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:20:38 2018

@author: Pshypher
"""

def not_within_range(color_flt:float)->bool:
    """Checks if a color doesn't lie within the range 0.0-1.0.
        Returns a boolean."""
    return color_flt < 0.0 or color_flt > 1.0

class Color(object):
    
    def __init__(self,red:float,green:float,blue:float):
        """Constructor for an instance of the Color class."""
        for primary_color in (red,green,blue):
            if not_within_range(primary_color):
                print(primary_color, "lies outside acceptable range 0.0-1.0")
                raise(ValueError)
            else:
                self.__red = red
                self.__green = green
                self.__blue = blue
                
    def __add__(self,param_Color):
        """Adds the respective primary color fields of two Colors."""
        primary_colors = [self.__red+param_Color.__red,
                          self.__green+param_Color.__green,
                          self.__blue+param_Color.__blue]
        for i,color in enumerate(primary_colors):
            if not_within_range(color):
                primary_colors[i] = 1.0
                
        red,green,blue = primary_colors
        return Color(red,green,blue)
    
    def __sub__(self,param_Color):
        """Subtracts the respective primary color fields of two Colors."""
        primary_colors = [self.__red-param_Color.__red,
                          self.__green-param_Color.__green,
                          self.__blue-param_Color.__blue]
        for i,color in enumerate(primary_colors):
            if not_within_range(color):
                primary_colors[i] = 0.0
                
        red,green,blue = primary_colors
        return Color(red,green,blue)
    
    def __str__(self):
        """String representation of an instance of a Color."""
        return "red({:.1f}),green({:.1f}),blue({:.1f}".format(self.__red,
                   self.__green, self.__blue)
                
        
                