def fibonacci_sequence(length):
    """Function prints the first N(not less than 1) fibonacci numbers."""
    
    nth_term = 1
    parent_nth_term = 1
    grandparent_nth_term = 0
    
    while length > 1:
        nth_term = parent_nth_term + grandparent_nth_term
        print(parent_nth_term, end=', ')
        grandparent_nth_term = parent_nth_term
        parent_nth_term = nth_term
        length -= 1
    else:
        print(nth_term)
        
def nth_fibonacci_term(N):
    """Display the nth term only of a fibonacci sequence."""
    
    nth_term = 1
    parent_nth_term = 1
    grandparent_nth_term = 0
    
    while N > 1:
        nth_term = parent_nth_term + grandparent_nth_term
        grandparent_nth_term = parent_nth_term
        parent_nth_term = nth_term
        N -= 1
    else:
        print(nth_term) 