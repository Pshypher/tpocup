# Prints numbers from A to B containing digits in the set {1,3,4,8,9}
# Unless stated otherwise, variables are of the type int

import math

def disp_num_in_range(A, B):
    """Function prints all numbers in the range A to B that have all digits in
        the set {1,3,4,8,9}. It also swaps the numbers assigned to A and B, 
        if B is less than A."""
    
    digits_set = {1,3,4,8,9}
    
    if A > B:
        temp = A
        A = B
        B = temp
        
    num = A
    while num <= B:   # Loop through numbers A to B
        i = 0
        if set_contains_num_digits(num, digits_set):
            print(num, end=' ')
            num += 1
        else:
            num += 1
            continue
        
def set_contains_num_digits(num, digits_set):
    """Iterates through the digits of a number and checks if all the digits
        in the number belongs to the set, digits_set (the second parameter)"""
    divisor = 10
    count = 0
    member_bool = True
    
    while count < math.floor(math.log10(num)):
        remainder = num % divisor
        num = num // divisor
        if remainder not in digits_set:
            member_bool = False
            break
    else:
        if num not in digits_set:
            member_bool = False
            
    return member_bool