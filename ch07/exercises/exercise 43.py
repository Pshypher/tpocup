# Unless stated otherwise, variables are assumed to be of the type str

def sort_string(S):
    """Converts the str S to a list, sorts the list, and converts the list
        back to a str: Returns the resulting str."""
    L = list(S)     # Convert string to list
    L = sort(L)     # Sort list using predefined sort function
    return ''.join(L)

def sort(L):
    """Sorts a list using bubble sort algorithm: Returns the sorted list."""
    for i in range(len(L)-1):       # For each pass through the entire list
                                    # make (n-1) comparisons
        for j in range(len(L)-1-i): # Compare element at index j (n-1-i) times
            
            if L[j] > L[j+1]:       # Swap adjacent element or neighbors in
                temp = L[j+1]       # list if the preceeding item is greater than
                L[j+1] = L[j]       # suceeding item
                L[j] = temp
                
    return L

# Use the sort_string function to sort the letters in the word EXAMPLE
word = "EXAMPLE"
print(sort_string(word))
    