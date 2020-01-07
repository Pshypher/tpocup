def is_sorted(items: list) -> bool:
    '''Checks whether a list of characters or numbers is sorted in either
        ascending or descending order. Returns true if the list is sorted,
        false otherwise.'''
    
    sorted_bool = True
    if len(items) > 2:
            # Boolean to check if the elements in the list are sorted in
            # ascending order
            ascending_bool = items[0] < items[1]
    else: 
        return sorted_bool
    
    if ascending_bool:  # List sorted in ascending order
        sorted_bool = sorted_asc_desc(items, '>')   
    else:   # List sorted in descending order
        sorted_bool = sorted_asc_desc(items, '<')
    
    return sorted_bool


def sorted_asc_desc(items, comp_operator):
    """Determines if the list of elements are sorted in ascending or
      descending order."""
    sorted_bool = True
    for i in range(len(items)-1):
        current = items[i]
        next = items[i+1]
        expression_str = 'current' + comp_operator + 'next'
        if eval(expression_str):
            sorted_bool = False
            break
        
    return sorted_bool