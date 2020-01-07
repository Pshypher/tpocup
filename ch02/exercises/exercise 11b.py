# Program written to find X sums consecutive numbers

# prompt user for an integer and assign to the variable X
# loop from the numbers 1 through int X assigning each number to the
# variable "outer_num"
#   assign 0 to the variable total
#   loop through numbers 1 to the value of "outer_num" assign
#   each value to "inner_num"
#       add each value of inner_num to the total
#   display the values of each sum of the consecutive numbers

# unless otherwise stated, the variables are assumed to be of type int

X_str = input("Enter an integer: ")
X = int(X_str)

for outer_num in range(1, X+1):
    total = 0
    for inner_num in range(1, outer_num+1):
        total = total + inner_num
    print("\nSum:", total)