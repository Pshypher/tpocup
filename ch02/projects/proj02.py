# display the denominations and num of each coin (quarters, dimes, nickels,
#   pennies) in stock
# prompt the user repeatedly for a price in the form xx.xx where x denotes a
# digit, or to enter 'q' to quit.
# when a price is entered
#   if the price is -ve, print an error message and request a new price or 'q'
#   to quit
#   prompt for the number of dollars in payment, if insufficient, print an
#   error message and reprompt for payment
#   determine the coins to be dispensed as change
#   print the number of coins to be dispensed as change and their denominations
#   in cases where exact payment is made print a message such as "No change."
#   if no change can be made with the remaining coins, print an error message
#   and halt execution of the program

# unless otherwise stated, variable are assumed to be of type int

QUARTER_VALUE = 25
DIME_VALUE = 10
NICKEL_VALUE = 5
PENNY = 1

CENTS_PER_DOLLAR = 100

num_of_quarters = 10
num_of_dimes = 10
num_of_nickels = 10
num_of_pennies = 10


print("\nWelcome to change-making program.")
print("\nStock:", num_of_quarters, "quarters,", num_of_dimes, "dimes,", \
      num_of_nickels, "nickels, and", num_of_pennies, "pennies")

purchase_price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

while purchase_price_str != 'q':
    purchase_price_flt = float(purchase_price_str)
    if purchase_price_flt < 0:
        print("Error: purchase price must be non-negative.")
        print("\nStock:", num_of_quarters, "quarters,", num_of_dimes, \
            "dimes,", num_of_nickels, "nickels, and", num_of_pennies, "pennies")
        purchase_price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
        continue
    
    payment_dollars_str = input("\nInput dollars paid (int): ")
    payment_dollars = int(payment_dollars_str)
    
    while payment_dollars < purchase_price_flt:
        print("Error: insufficient payment.")
        payment_dollars_str = input("\nInput dollars paid (int): ")
        payment_dollars = int(payment_dollars_str)
        
    purchase_price_cents = round(purchase_price_flt * CENTS_PER_DOLLAR)
    payment_cents = payment_dollars * CENTS_PER_DOLLAR
    change_due = payment_cents - purchase_price_cents
    
    if purchase_price_cents == payment_cents:
        print("No change.")
        print("\nStock:", num_of_quarters, "quarters,", num_of_dimes, "dimes,", \
            num_of_nickels, "nickels, and", num_of_pennies, "pennies")
    
        purchase_price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
        continue
    
    # calculate the change to be dispensed in denominations of
    # quarters, dimes, nickels and pennies
    quarters = change_due // QUARTER_VALUE
    if 0 < quarters <= num_of_quarters:
        change_due = change_due - (quarters * QUARTER_VALUE)
        num_of_quarters = num_of_quarters - quarters
    elif 0 < num_of_quarters < quarters:
        change_due = change_due - (num_of_quarters * QUARTER_VALUE)
        quarters = num_of_quarters
        num_of_quarters = 0
    else:
        quarters = 0
        
    dimes = change_due // DIME_VALUE
    if 0 < dimes <= num_of_dimes:
        change_due = change_due - (dimes * DIME_VALUE)
        num_of_dimes = num_of_dimes - dimes
    elif 0 < num_of_dimes < dimes:
        change_due = change_due - (num_of_dimes * DIME_VALUE)
        dimes = num_of_dimes
        num_of_dimes = 0
    else:
        dimes = 0
        
    nickels = change_due // NICKEL_VALUE
    if 0 < nickels <= num_of_nickels:
        change_due = change_due - (nickels * NICKEL_VALUE)
        num_of_nickels = num_of_nickels - nickels
    elif 0 < num_of_nickels < nickels:
        change_due = change_due - (num_of_nickels * NICKEL_VALUE)
        nickels = num_of_nickels
        num_of_nickels = 0
    else:
        nickels = 0

    pennies = change_due
    if pennies > num_of_pennies:
        print("Error: ran out of coins.")
        break
    else:
        num_of_pennies = num_of_pennies - pennies
        
    print("\nCollect change below:")
    if quarters > 0:
        print("Quarters:", quarters)
    if dimes > 0:
        print("Dimes:", dimes)
    if nickels > 0:
        print("Nickels:", nickels)
    if pennies > 0:
        print("Pennies:", pennies)
        
    print("\nStock:", num_of_quarters, "quarters,", num_of_dimes, "dimes,", \
      num_of_nickels, "nickels, and", num_of_pennies, "pennies")
    
    purchase_price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")