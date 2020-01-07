# Program written to display a number and its root if it is a perfect square
# prompt user for a number
# while the number entered is not a perfect square
#   prompt the user for another number
# display the number and its root

import math

# prompt user for a number
number_str = input("Enter an integer that is a perfect square: ")
number_int = int(number_str)

# calculate the root of the number
root_int = int(math.sqrt(number_int))

# Re-prompt user for a number if the previous number entered
# is not a perfect square
while not root_int * root_int == number_int:
    number_str = input("Enter an integer that is a perfect square: ")
    number_int = int(number_str)
    root_int = int(math.sqrt(number_int))
    
print("  Perfect Square:  ")
print("Number:", number_int)
print("Root:", root_int)



