# Shifts the numbers in a list (left or right) circularly by some
# integer amount
# Unless stated otherwise, variables are assumed to be the list data type

def left_shift(N, k_int):
    """Given a list of N numbers, function shifts the numbers circularly by
        some integer k_int (where k < N). Returns the shifted list."""
    # Slice the list N from 0 up to but not including the item at
    # index k
    shift_seq = N[:k_int]
    N[:k_int] = []
    N = N + shift_seq
    
    return N
    
def shift(N, k_int, dir_str):
    """Given a list of N numbers, function shifts the numbers circularly
        by some integer k_int in the direction(left, right) as specified by
        the argument dir_str. Returns the shifted list."""
    if dir_str.lower() == "left":
        left_shift(N, k_int)
    elif dir_str.lower() == "right":
        # Slice the list N from -k to the end of N
        shift_seq = N[-k_int:]
        N[-k_int:] = []    # delete the elements from -k to the end of the list
        N = shift_seq + N
    else:
        print('Direction should either be "left" or "right" rather than',
              dir_str)
        
    return N