# Program designed to compute multiplication using the
# Russian Peasant or Ancient Egyptian algorithm

# continue_str = 'y'
# product = 0
# loop if continue_str equals 'y'
    # prompt for two numbers to be multiplied together labelled A and B
    # while B is still divisible (i.e. greater than 0)
        # if B is odd
            # add the current value of A to the variable "product"
            # add the value of A to itself
        # otherwise multiply A by 2
        # divide B by 2, leaving out the decimal 
    # display the value of the product variable at the end of the loop
    # prompt the user to continue; 'y' to continue and vice-versa for
    # any other string

# unless stated otherwise, variables are assumed to be of type int

continue_str = 'y'

while continue_str == 'y':
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
    
    continue_str = input("Repeat multiplication?('y' or 'n'): ")
    
    
    
    
