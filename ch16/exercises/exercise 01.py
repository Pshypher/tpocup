# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 03:07:51 2018

@author: Pshypher
"""

def properly_matched(parenthesis_str):
    """
    >>> properly_matched("(")
    False
    >>> properly_matched(")")
    False
    >>> properly_matched("()")
    True
    >>> properly_matched("(()())")
    True
    >>> properly_matched("(()")
    False
    >>> properly_matched(")(")
    False
    """
    try:
        if len(parenthesis_str) < 2:
            if len(parenthesis_str) > 0:
                return False
            return True
        else:
            opening_paren = parenthesis_str[0]
            closing_paren_sub = find(parenthesis_str,')')
            closing_paren = parenthesis_str[closing_paren_sub]
            rem_grouping_str = parenthesis_str[1:closing_paren_sub] + \
            parenthesis_str[closing_paren_sub+1:]
            return opening_paren == '(' and closing_paren == ')' and \
                properly_matched(rem_grouping_str)
    except IndexError:
            return False
            
def find(string,char):
    """
    >>> find('',')')
    Traceback (most recent call last):
        ...
    IndexError: ')' not found.
    >>> find('((_*',')')
    Traceback (most recent call last):
        ...
    IndexError: ')' not found.
    >>> find(')',')')
    0
    >>> find('(()())',')')
    2
    >>> find('(()',')')
    2
    """
    # Looks for a single char in a substring using recursion
    if not string:
        raise IndexError("'{}' not found.".format(char))
    elif string[:len(char)] == char:
        return 0
    else:
        string = string[1:]
        return find(string,char) + 1
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()