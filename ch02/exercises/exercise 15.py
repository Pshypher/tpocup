# Program written that checks if a number N is prime
# prompt user for an integer and assign to a variable N
# divisor = 2
# while divisor is less than the square root of N
#   check if the number divides N evenly without a remainder

# unless otherwise stated, the type of a variable is assumed to be an integer

import math

N_str = input("Enter a number: ")
N = int(N_str)
divisor = 2

while divisor <= math.sqrt(N):
    if N % divisor == 0:
        print(N, "is not a prime number")
        break
    divisor = divisor + 1
else:
    print(N, "is prime")