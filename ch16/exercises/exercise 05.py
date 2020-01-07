# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:16:55 2018

@author: Pshypher
"""

def calculate_interest(principal,rate,year):
    """
    >>> calculate_interest(37500,48,3)
    121567.2
    >>> calculate_interest(26250,53,3)
    94016.39625
    >>> calculate_interest(26250,53,'three')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'int'
    """
    if year == 0:
        return principal
    else:
        rate_flt = rate / 100
        interest = rate_flt * principal
        principal = principal + interest
        return calculate_interest(principal,rate,year-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
