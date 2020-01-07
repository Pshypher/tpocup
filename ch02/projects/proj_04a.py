# Program designed to compute multiplication using the
# Russian Peasant or Ancient Egyptian algorithm

# prompt for two numbers to be multiplied together labelled A and B
# product = 0
# while B is still divisible (i.e. greater than 0)
    # if B is odd
        # add the current value of A to the variable "product"
        # add the value of A to itself
    # otherwise multiply A by 2
    # divide B by 2, leaving out the decimal 
# display the value of the product variable at the end of the loop

# unless stated otherwise, variables are assumed to be of type int

A_str = input("Enter the first number: ")
B_str = input("Enter the second number: ")
A = int(A_str)
A_copy = A
B = int(B_str)
B_copy = B

product = 0

while B_copy > 0:
    if B_copy % 2:
        product = product + A_copy
        A_copy = A_copy + A_copy
    else:
        A_copy = A_copy * 2
    B_copy = B_copy // 2
    
print(A, "*", B, "=", product)
    
