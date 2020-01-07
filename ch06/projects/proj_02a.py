# Program designed for the purposes of substring matching with applications
# in genetics, such as trying to find a substring of bases ACTG
# (adenine, cytosine, thymine and guanine) in a known DNA string, or
# reconstructing an unknown DNA string from pieces of nucleotide bases

# Without using the string method find, a custom function that finds the lowest
# index that a substring occurs within a string is defined
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