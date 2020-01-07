# Program designed to solve a NPR radio show "car talk" puzzle

# odometer measures distance starting from 000000 up to 999999
#   check if the last four digits, but not the last five digits are palindromes
#       add one mile to the previous measured distance
#       check if the last five digits form a palindrome
#           add another mile to previous distance
#               does the four digits in the middle of the measured distance
#               form a palindrome
#                   finally add another mile to the distance if the middle 4 digits are palindromes
#                       check if all six digits now form a palindrome
#                           print the mileage from the first time all these palindromes were noticed
#                           (i.e. when the last four digits formed a palindrome)

# unless stated otherwise, all variables are assumed to be of type int
import string

def is_palindrome(substr):
    """Returns True of the substring is a palindrome."""
    
    for char in substr:
        if char in string.whitespace + string.punctuation:
            substr = substr.replace(char, '')
    
    return substr == substr[::-1]


mileage = 000000
ODOMETER_LIMIT = 999999


while mileage < ODOMETER_LIMIT:
    # are the last four digits but not the last five palindromes?
    mileage_str = '{:06d}'.format(mileage)
    if is_palindrome(mileage_str[2:]):
        # are the last five digits of the previous mileage + 1 palindromes 
        mileage_str = '{:06d}'.format(mileage+1)
        if is_palindrome(mileage_str[1:]):
            # after a mile, do the four digits in the middle form a palindrome?
            mileage_str = '{:06d}'.format(mileage+2)
            if is_palindrome(mileage_str[1:5]):
                # after another mile, do all six digits form a palindrome?
                mileage_str = '{:06d}'.format(mileage+3)
                if is_palindrome(mileage_str):
                    print(mileage)
                    mileage = 999998            
    mileage = mileage + 1
    

