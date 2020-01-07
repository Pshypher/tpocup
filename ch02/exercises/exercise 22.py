# prompt user for a number "num" greater than 2
# repeatedly prompt the user for the number "num" if it is not greater than 2
# while the number "num" is greater than 2
#   take the square root of "num"
#   increment a count variable "times" used to record how many times the
#   operation has been completed
#   each time display the root of "num" and the number of times the operation
#   was run

# unless stated otherwise, variables are assumed to be of type int

import math

num_str = input("Enter a number greater than 2: ")
num = int(num_str)

while not(num > 2):
    num_str = input("Enter a number greater than 2: ")
    num = int(num_str)
   
times = 0

while num >= 2:
    num = math.sqrt(num)
    times = times + 1
    print("{}: {:.3f}".format(times, num))
    
