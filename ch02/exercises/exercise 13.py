# Program displays the input only when it is of type int
# prompt user for integer
# re-prompt user if the previous value entered is a different type
# display the entered value if it is an integer

number_str = input("Input an integer: ")

while not number_str.isdigit():
    number_str = input("Error: try again. Input an integer: ")
    
print("The integer is :", number_str)