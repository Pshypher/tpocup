# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:55:07 2018

@author: Pshypher
"""

dig_str = input("Input an integer: ")
try:
    if dig_str.isdigit():
        dig_int = int(dig_str)
    else:
        raise ValueError(dig_str)   # raise an exception here!
except ValueError:
    print("Conversion to int Error: ", dig_str)