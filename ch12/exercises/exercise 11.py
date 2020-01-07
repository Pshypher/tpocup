# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:46:53 2018

@author: Pshypher
"""

class Sound(object):
    
    def __init__(self, decibels_flt:float):
        """Constructor of a Sound object."""
        self.__decibels = decibels_flt
        
    def get_decibels(self)->float:
        """Returns the sound level in decibels."""
        return self.__decibels
    
    def set_decibels(self, decibels_flt:float):
        """Adjust the sound level."""
        self.__decibels = decibels_flt
        
    def __add__(self, param_Sound):
        """Add two Sound levels together. Returns a new Sound object."""
        return Sound(self.__decibels + param_Sound.__decibels)
    
    def __sub__(self,param_Sound):
        """Subtract a Sound level from another. Returns a new Sound object."""
        return Sound(abs(self.__decibels - param_Sound.__decibels))