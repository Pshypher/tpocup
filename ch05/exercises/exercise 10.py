# Program designed to prompt for three numbers, divide the first number by the
# second number and add that result to the third number;The errors:
# ValueError and ZeroDivisionError are checked using exceptions

# Prompt for all three numbers
first_str = input("Enter first number: ")
second_str = input("Enter second number: ")
third_str = input("Enter third number: ")

# Catch the ValueError and ZeroDivisionError exceptions
try:
    first_int = int(first_str)
    second_int = int(second_str)
    third_int = int(third_str)
    result_float = first_int / second_int + third_int
except ValueError:
    if first_str.isalpha():
        print("first_str({:s}) isn't a number.".format(first_str))
    elif second_str.isalpha():
        print("second_str({:s}) isn't a number.".format(second_str))
    else:
        print("third_str({:s}) isn't a number.".format(third_str))
except ZeroDivisionError:
    print("The second number has a zero value.")