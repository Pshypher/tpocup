# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:33:41 2018

@author: Pshypher
"""

def fibonacci(n):
    """
    >>> fibonacci(4)
    5
    >>> fibonacci(6)
    13
    """
    if n == 0 or n == 1:        # base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive case
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()