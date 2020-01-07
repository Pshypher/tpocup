# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:22:18 2018

@author: Pshypher
"""

def factorial(n):
    """
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    if n == 1:
        return 1                    # base case
    else:
        return n * factorial(n-1)   # recursive case
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    