# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:18:19 2018

@author: Pshypher
"""

def take_step(n):
    """
    >>> take_step(4)
    'step(4) + step(3) + step(2) + Easy'
    """
    if n == 1:  # base case
        return "Easy"
    else:
        this_step = "step(" + str(n) + ")"
        previous_steps = take_step(n-1)
        return this_step + " + " +previous_steps
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()