# Checks whether the date given as an argument to the function is a leap year
# according to the Gregorian calendar system.

def is_leap_year(year):
    """Takes in a year as input and prints whether it's a leap year (or not)"""
    if year % 4:
        print("{:d} is not a leap year".format(year))
    else:
        if not (year % 4) and not (year % 100) and year % 400:
            print("{:d} is not a leap year".format(year))
        else:
            print("{:d} is a leap year".format(year))
    