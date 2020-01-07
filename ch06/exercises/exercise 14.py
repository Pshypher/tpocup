# International calling card to India, special offers give an extra call charge
# for certain amounts of card charge purchased.
def call_charge_with_offer():
    """Function asks user for the amount he/she wants on the card and returns
    the total charge that the user gets."""
    charge_str = input("How much call credit would you like to buy? ")
    charge_flt = float(charge_str)
    
    if charge_flt == 25:
        total_charge_flt = charge_flt + 3
    elif charge_flt == 50:
        total_charge_flt = charge_flt + 8
    elif charge_flt == 100:
        total_charge_flt = charge_flt + 20
    else:
        total_charge_flt = charge_flt
        
    return total_charge_flt