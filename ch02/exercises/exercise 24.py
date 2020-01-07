# Program designed to solve a NPR radio show "car talk" puzzle

# odometer measures distance starting from 100000 up to 999999
#   check if the last four digits, but not the last five digits are palindromes
#       add one mile to the previous measured distance
#       check if the last five digits form a palindrome
#           add another mile to previous distance
#               does the four digits in the middle of the measured distance
#               form a palindrome
#                   finally add another mile to the distance if the middle 4 digits are palindromes
#                       check if all six digits now form a palindrome
#                           print the mileage from the first time all these palindromes were noticed
#                           (i.e. when the last four digits formed a palindrome)

# unless stated otherwise, all variables are assumed to be of type int

mileage = 100000
ODOMETER_LIMIT = 999999

while mileage < ODOMETER_LIMIT:
    # are the last four digits but not the last five palindromes?
    ten_thousands = mileage % 100000 // 10000
    thousands = mileage % 10000 // 1000
    hundreds = mileage % 1000 // 100
    tens = mileage % 100 // 10
    unit = mileage % 10
    if thousands == unit and hundreds == tens and not \
       (ten_thousands == unit and thousands == tens):
        # print(mileage)
        
        # are the last five digits of the previous mileage + 1 palindromes 
        mileage = mileage + 1
        ten_thousands = mileage % 100000 // 10000
        thousands = mileage % 10000 // 1000
        tens = mileage % 100 // 10
        unit = mileage % 10
        if ten_thousands == unit and thousands == tens:
            # print(mileage)
            
            # after a mile, do the four digits in the middle form a palindrome?
            mileage = mileage + 1
            ten_thousands = mileage % 100000 // 10000
            thousands = mileage % 10000 // 1000
            hundreds = mileage % 1000 // 100
            tens = mileage % 100 // 10
            if ten_thousands == tens and thousands == hundreds:
                # print(mileage)
                
                # after another mile, do all six digits form a palindrome?
                mileage = mileage + 1
                hundred_thousands = mileage // 100000
                ten_thousands = mileage % 100000 // 10000
                thousands = mileage % 10000 // 1000
                hundreds = mileage % 1000 // 100
                tens = mileage % 100 // 10
                unit = mileage % 10  
                if hundred_thousands == unit and ten_thousands == tens and \
                   thousands == hundreds:
                    # print(mileage)
                    
                    mileage = mileage - 3
                    print(mileage)
                    mileage = 999998
                    
    mileage = mileage + 1