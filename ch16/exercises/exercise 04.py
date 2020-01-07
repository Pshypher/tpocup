# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:33:41 2018

@author: Pshypher
"""

def fibonacci(n, fibonacci_dict=None):
    """
    >>> fibonacci(4)
    5
    >>> fibonacci(6)
    13
    """
    if not fibonacci_dict:
        fibonacci_dict = {"f(0)": 1, "f(1)":1}
    
    if "f({:d})".format(n) in fibonacci_dict:   # base case
        return fibonacci_dict["f({:d})".format(n)]
    else:
        fibonacci_dict["f("+str(n)+")"] = fibonacci(n-1,fibonacci_dict) + \
            fibonacci(n-2,fibonacci_dict)
        return fibonacci_dict["f("+str(n-1)+")"] + fibonacci_dict[
                "f("+str(n-2)+")"]     # recursive case
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()