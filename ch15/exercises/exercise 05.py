# Program designed for the purposes of substring matching with applications
# in genetics, such as trying to find a substring of bases ACTG
# (adenine, cytosine, thymine and guanine) in a known DNA string, or
# reconstructing an unknown DNA string from pieces of nucleotide bases

# Unless stated otherwise,all variables are of the type int

# Without using the string method find, a custom function that finds the lowest
# index that a substring occurs within a string is defined
import doctest
doctest.testmod()

def find(some_string, substring, start, end):
    """Returns the lowest index where a substring is first found occuring
        within a larger string or -1 if the substring is not contained within
        the string."""
    
    if end > len(some_string):
        end = len(some_string)
    
    index = start
    while len(some_string[index:]) >= len(substring) and index < end:
        if some_string[index:index + len(substring)] != substring:
            index = index + 1
        else:
            break
    else:
        index = -1
        
    return index

# The subsequent function defined below finds all the locations where a
# substring is found, not simply the first one within a larger string
def multi_find(some_string, substring, start, end):
    """
    >>> multi_find("GCATCGGACATCG", "ATCG", 2, 5)
    '2'
    >>> multi_find("GCATCGGACATCG", "ATCG", 0, 13)
    '2, 9'
    >>> multi_find("GACCG", "GC", 0, 4)
    ''
    >>> multi_find("TACGGACCGTAGGATTCATGCA", 02037, 0, 12)
    Traceback (most recent call last):
        ...
    SyntaxError: invalid token
    >>> multi_find("TAGGACCGTAGGATTCATAGCA", "TAG", 0, 22)
    '0, 8, 17'
    """
    indices_str = ""
    
    index = start
    while index != -1:
        index = find(some_string, substring, index, end)
        if index != -1:
            indices_str = indices_str + str(index) + ', '
            index += 1
    else:
        indices_str = indices_str[:-2]
    
    return indices_str