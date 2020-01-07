# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:57:57 2018

@author: Pshypher
"""

class Organ(object):
    
    def __init__(self, organ_class='', size_float=0.0):
        """Constructor for an Organ instance."""
        self.__organ_class = organ_class
        self.__size = size_float
        
    def get_size(self):
        """Return the dimension of Organ."""
        return self.__size
    
    def __str__(self):
        """String representation of Organ."""
        print('in str')
        return "Organ: {}".format(self.__organ_class)

class Heart(Organ):
    
    def __init__(self, size_float=0.0):
        """Initialize the attributes for the Heart organ."""
        Organ.__init__(self,'Heart',size_float)
        
    def pump(self):
        print("Pump blood through the entire human body.")
        
    def generate_heartbeat(self):
        print("Specialized muscles in heart contract spontaneously & generate \
electrical signals that spread to the rest of the heart.")
        
    def regulate(self):
        print("Control the rate of heart beats per minutes")

class Brain(Organ):
    
    def __init__(self, size_float=0.0, hemisphere_str=''):
        """Constructor of the brain organ."""
        # set the dominant hemisphere either left/right
        Organ.__init__(self, 'Brain', size_float)
        self.hemisphere = hemisphere_str
        
    def dominant_hemisphere(self):
        """Return the dominant hemisphere."""
        return self.hemisphere
    
    def reasoning(self):
        print("Retrieving and using previously stored information to reason \
through difficult problems")
        
    def memorize(self):
        print("Recording and storing information")
        
    def sense(self):
        print("React to sensations conveyed from the nerve endings")