# Program calculates the roots of a quadratic equation using the quadratic formula
# prompt the user for the constants A, B and C
# the property of the discriminant (b*b - 4*a*c) are used to ignore imaginary roots
# using the quadratic formula generate the real roots of the equation

# Unless otherwise stated, the variables are of type int 

import math

A_str = input("Enter the coefficient a: ")
A = int(A_str)
B_str = input("Enter the coefficient b: ")
B = int(B_str)
C_str = input("Enter the constant c: ")
C = int(C_str)

discriminant = B*B - 4*A*C

if discriminant > 0:
    larger_root_flt = (-B + math.sqrt(discriminant))/2*A
    smaller_root_flt = (-B - math.sqrt(discriminant))/2*A
    print("The roots are:", larger_root_flt, "and", smaller_root_flt)
elif discriminant == 0:
    root_flt = (-B + math.sqrt(discriminant))/2*A
    print("The root is:", root_flt)
    