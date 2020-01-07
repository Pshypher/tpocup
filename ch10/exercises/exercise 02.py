# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:39:06 2018

@author: Pshypher
"""

def make_averages(sums_list,total_int):
    """Convert each list element into an average by dividing by the total."""
    return [value_int/total_int for value_int in sums_list]