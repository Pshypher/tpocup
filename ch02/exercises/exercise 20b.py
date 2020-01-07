# Program calculates the roots of a quadratic equation using the quadratic formula
# prompt the user for the constants A, B and C
# the property of the discriminant (b*b - 4*a*c) is used to handle
# real and imaginary roots
# using the quadratic formula generate the roots of the equation

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
    root1_flt = (-B + math.sqrt(discriminant))/2*A
    root2_flt = (-B - math.sqrt(discriminant))/2*A
    print("The roots are:", root1_flt, "and", root2_flt)
elif discriminant == 0:
    root_flt = (-B + math.sqrt(discriminant))/2*A
    print("The root is:", root_flt)
else:
    imaginary_part_flt = math.sqrt(discriminant * -1)/2*A
    real_part = -B/2*A
    imaginary_part = str(imaginary_part_flt) + "j"
    root1_img = str(real_part) + "+" + imaginary_part
    root2_img = str(real_part) + "-" + imaginary_part 
    print("The roots are:", root1_img, "and", root2_img)
    