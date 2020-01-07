# Program written to find the sum of numbers from the value 
# of the number down to one

# prompt user for an integer assigned to a variable "X"
# loop through values from "X" to 1
#   each time through the loop add the integer to a
#   variable "total"
# unless otherwise stated, variables are assumed to be of type int

X_str = input("Enter an integer: ")
X = int(X_str)
total = 0

for num in range(X, 0, -1):
    total = total + num
    
print("X is", X)
print("\nTotal:", total)
    