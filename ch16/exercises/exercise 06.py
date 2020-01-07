# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:37:25 2018

@author: Pshypher
"""

def convert(decimal):
    """
    >>> convert(1)
    '1'
    >>> convert(5)
    '101'
    >>> convert(9)
    '1001'
    >>> convert(45)
    '101101'
    """
    if decimal < 2:
        return str(decimal)
    else:
        quotient = decimal // 2
        remainder = decimal % 2
        return  str(remainder) + convert(quotient)
         

if __name__ == '__main__':
    import doctest
    doctest.testmod()