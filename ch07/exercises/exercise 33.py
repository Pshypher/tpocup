def sort_tuple(T):
    """Takes a tuple T as an argument and sorts the tuple: Uses bubble sort
        algorithm. Returns a sorted tuple."""
    
    temp_list = list(T)
    didSwap = False
    
    for i in range(1, len(temp_list)):
        for j in range(0, len(temp_list)-i):
            if temp_list[j+1] < temp_list[j]:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                didSwap = True
        if not didSwap:
            break
        
    return tuple(temp_list)