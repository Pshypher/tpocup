# An function designed to apply discounts on an item; if the buyer is a member,
# a 10% discount is applied, if today happens to be father's day a 5% discount
from datetime import date

today = date.today()

def apply_discount(cost_flt, member_bool):
    """Applies discount to the cost of an item."""
    
    MEMBERSHIP_DISCOUNT = 0.1
    FATHERS_DAY_DISCOUNT = 0.05
    
    if member_bool:
        discount_flt = cost_flt * MEMBERSHIP_DISCOUNT
        cost_flt =  cost_flt - discount_flt
        
    if today.month == 6 and 2 < (today.day/7) <= 3:
        discount_flt = cost_flt * FATHERS_DAY_DISCOUNT
        cost_flt = cost_flt - discount_flt
        
    return cost_flt