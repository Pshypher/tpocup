# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 00:14:23 2018

@author: Pshypher
"""

def factorial(n):
    """recursive factorial with print to show operation."""
    indent = 4 * (6 - n) * " "  # more indent on deeper recursion
    print(indent + "Enter factorial n = ", n)
    if n == 1:
        print(indent + "Base case.")
        return 1
    else:
        print(indent + "Before recursive call f(" + str(n-1) + ")")
        # seperate recursive call allows print after call
        rest = factorial(n-1)
        print(indent + "After recursive call f(" + str(n-1) + ") = ", rest)
        return n * rest
