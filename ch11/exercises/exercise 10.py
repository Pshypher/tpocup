# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:50:03 2018

@author: Pshypher
"""

class Vegetable(object):
    
    def __init__(self,code_str,name_str,description_str=None,price_float=0.0):
        """Initializes an instance of the Vegetable class."""
        self.__product_code = code_str
        self.__name = name_str
        self.__description = description_str
        self.__price = price_float
        
    def get_code(self):
        """Returns the product code of an instance of the Vegetable class."""
        return self.__product_code
    
    def set_code(self,code_str):
        """Change the product code of Vegetable."""
        self.__product_code = code_str
        
    def get_name(self):
        """Returns the name of the Vegetable."""
        return self.__name
    
    def set_name(self,name_str):
        """Change the name of the Vegetable."""
        self.__name = name_str
        
    def get_description(self):
        """Returns the description set for an instance of a Vegetable class."""
        return self.__description
        
    def set_description(self,description_str):
        """Set the desciption of Vegetable."""
        self.__description = description_str
        
    def get_price(self,price_float):
        """Change how much a Vegetable costs per unit."""
        self.__price = price_float
        
        