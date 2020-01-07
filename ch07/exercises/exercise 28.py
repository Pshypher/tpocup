# Program generates a list of lists from a list of alphabets in the following 
# form [a,b,c,...,z] -> [[z], [y,z], [x,y,z], ... ,[a,b, ... ,y,z]]

# Unless stated otherwise, variables are assumed to be of the list data type

import string

# create a list of alphabets
alphabets = list(string.ascii_lowercase)

# initialize the list of lists as an empty list
list_of_lists = []
# iterate through the list of alphabets starting at the end of the list
for i in range(len(alphabets), 0, -1):
    # slice the list of alphabets from the end to the current index
    slice = alphabets[i-1:]
    # append the slice to the list of lists
    list_of_lists.append(slice)
    
for letters in list_of_lists:
    print("Alphabets:", letters)