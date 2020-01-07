def remove_evens(numbers: list) -> list:
    '''Removes even numbers from a list of integers.'''
    
    # Return a new list object without modifying the list passed in as an
    # argument to the function
    return [num for num in numbers if num%2]


def remove_odds(numbers: list) -> list:
    '''Removes odd numbers from a list of integers.'''
    
    # Return a new list object without modifying the list passed in as an
    # argument to the function
    return [num for num in numbers if not num%2]


def remove_evens_odds(numbers, odd_bool):
    '''Removes odd numbers from the list of integers in <numbers> if <odd_bool>
        is true, otherwise even numbers are removed.'''
    if odd_bool:
        numbers = remove_odds(numbers)
    else:
        numbers = remove_evens(numbers)
        
    return numbers