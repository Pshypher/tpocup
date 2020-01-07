# Program designed to make payment on a credit card with a credit limit of $1000
# the minimum payment due is always $20

import random

CREDIT_LIMIT = 1000
DEBT = random.random() * CREDIT_LIMIT

def make_payment(P):
    """ Makes payment on a credit card."""
    
    MINIMUM_PAYMENT = 20
    
    valid_payment = False
    
    if P < MINIMUM_PAYMENT:
        print("Minimum allowable payment is $20.")
        print("Retry")
    elif P > CREDIT_LIMIT:
        print("You've paid more than the allowed credit limit on the card.")
        print("Retry")
    else:
        print("Success")
        if P >= DEBT:
            print("You will be given a ${:.2f} refund.".format(P-DEBT))
        valid_payment = True
        
    return valid_payment
            
            
valid_payment = False
while not valid_payment:
    payment_str = input("Enter amount you wish to pay: ")
    try:
        payment_int = int(payment_str)
        valid_payment = make_payment(payment_int)
    except ValueError:
        print("Payment should be of type int or float")
        