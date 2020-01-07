def my_max(L):
    """Akin to Python built-in function max, finds and returns the
        maximum element in the list L."""
    # Assign the index of the first element of the list to max_index
    max_index = L[0]
    # from the second element to the end, if the element at
    # index i is larger than the element at L[max_index] assign i
    # to max_index
    for i in range(1, len(L)):
        if L[i] > L[max_index]:
            max_index = i
        
    return L[max_index]

def my_min(L):
    """Akin to Python's built in function min finds and returns the
       minimum element in the list L."""
    # Assign the index of the first element of L to min_index
    min_index = L[0]
    # loop through the elements to find the smaller element
    for i in range(1, len(L)):
        if L[i] < L[min_index]:     # Each time you find a smaller element
            min_index = i           # update min_index
        
    return L[min_index]
        
    