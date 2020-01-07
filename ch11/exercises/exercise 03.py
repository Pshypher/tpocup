# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:11:31 2018

@author: Pshypher
"""

class TableFan(object):
    
    def __init__(self,manufacturer,cost=0.0,used_bool=False):
        """Initializes an instance of a TableFan class."""
        self.__speed = 0
        self.__rotate = False
        self.__on = True
        self.__degrees = 0
        self.__manufacturer = manufacturer
        self.__cost = cost
        self.__used = used_bool
        
    def control_speed(self):
        """Adjust the speed of the fan."""
        self.__speed = (self.__speed+1)%6
        
    def toggle_rotation(self):
        """Toggle between both rotation states."""
        self.__rotate = False if self.__rotate else True
        
    def switch_on(self):
        """Power on TableFan."""
        self.__on = True
        
    def switch_off(self):
        """Power off TableFan."""
        self.__on = False
        
        