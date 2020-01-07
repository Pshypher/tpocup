# Determines if the year argument passed in is a leap year according to the
# Gregorian calendar
def leap_year(year_str):
    """Returns true if the year is a leap year."""
    return bool(not int(year_str)%400 or not int(year_str)%4 and int(year_str)%100)

# Rotates a string such that the last n characters have been moved to the
# beginning
def rotate(str, n_int):
    """Returns a rotated string such that the last n characters
        have been moved to the beginning."""
    if str == '' or len(str) == 1:
        return str
    elif len(str) < n_int:
        print(n + ' is larger than the length of the string "{:s}"'.format(str))
        return str
    else:
        return str[-n_int:] + str[:-n_int]
    
# Counts the number of even, odd and zero digits before the decimal point of
# of float or all of the digit in an integer
def count_digits(number):
    """Returns a count of even digits, a count of odd digits, and a count of
        zeros that are to the left of the decimal point."""
    
    number_int = int(number//1)
    
    even_count = 0
    odd_count = 0
    zero_count = 0
    
    while number_int > 0:
        digit = number_int % 10
        number_int = number_int // 10
        if digit == 0:
            zero_count += 1
        elif digit % 2:
            odd_count += 1
        else:
            even_count += 1
    else:
        return even_count, odd_count, zero_count
    
# Checks that each string argument passed in is a float.A float is defined to
# be a string of digits that has at most one decimal point. An string of
# integers would also suit the definition of a float
def float_check(number_str):
    """Returns true if the argument number_str represents a float, with at most
        one decimal point."""
    return number_str.count('.') <= 1 and number_str.replace('.', '').isdigit()