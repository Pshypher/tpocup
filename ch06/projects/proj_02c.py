# Program designed for the purposes of substring matching with applications
# in genetics, such as trying to find a substring of bases ACTG
# (adenine, cytosine, thymine and guanine) in a known DNA string, or
# reconstructing an unknown DNA string from pieces of nucleotide bases

# Unless stated otherwise,all variables are of the type int

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

# The subsequent function defined below finds all the locations where a
# substring is found, not simply the first one within a larger string
def multi_find(some_string, substring, start, end):
    """Returns a string containing all the indices of all the occurences of
        a substring within a larger string. An empty string is returned if the
        string contains no such occurence of the substring."""
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


some_string = "GCatcgGACATCG"
another = "TACGgaccgtaggattcATGCA"
another_all_uppercase = "ATGCCAGTTGGCAATAGGTGGGGCATG"

base_ltrs_only_substr = "ATCG"
nucleotide_substr = "GACCG"
another_nucleotide_substr = "AATAGGT"

if find(some_string.upper(), base_ltrs_only_substr, 0, 6) != -1:
    print("{0:s} is contained within {3:s}[{1:d}:{2:d}]".format(
        base_ltrs_only_substr,0, 6, some_string.upper()))
    
print("{:s} in {:s}:".format(nucleotide_substr, another.upper())  + " " + \
      str(bool(multi_find(another.upper(), nucleotide_substr, 0, 22))))

print("{:s} in {:s}:".format(nucleotide_substr, another.upper()[10:22]) + \
      " " + str(bool(multi_find(another.upper(), nucleotide_substr, 10, 22))))

print("{:s} in {:s}:".format(nucleotide_substr,
                             another.upper()[5:22]) + \
      " " + str(bool(multi_find(another.upper(), nucleotide_substr, 5, 22))))

print("{:s} in {:s}:".format(another_nucleotide_substr,
                             another_all_uppercase[0:13]) + \
      " " + str(bool(multi_find(another_nucleotide_substr.upper(),
                                another_all_uppercase, 0, 13))))

print("{:s} in {:s}:".format(another_nucleotide_substr,
                             another_all_uppercase[14:27]) + \
      " " + str(bool(multi_find(another_all_uppercase,
                                another_nucleotide_substr, 14, 27))))

print("{:s} in {:s}:".format(another_nucleotide_substr,
                             another_all_uppercase) + \
      " " + str(bool(multi_find(another_all_uppercase, nucleotide_substr, 0, 27))))


        
