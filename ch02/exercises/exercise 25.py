# program displays a two digit number such that when you square it, the
# resulting three-digit number has its rightmost two digits the same as
# the original two-digit number

# loop through number 10 to 99
#   during each iteration square a 2 digit number
#   if the square of the 2 digit number AB produces a 3 digit number such that
#   AB * AB = CAB
#       display the number

# unless otherwise stated, variables are assumed to be of type int

number = 10
STOP = 99

while number < STOP:
    square = number * number
    tokens_of_tens_and_unit = square % 100
    
    if number == tokens_of_tens_and_unit:
        print(number)
        number = STOP
        
    number = number + 1