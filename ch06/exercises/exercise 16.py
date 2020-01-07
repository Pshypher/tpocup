# Prints out all the common multiples of two divisors (6 and 10) up until a
# certain number which is less than the upper limit (100)

def common_multiples(X, Y, Z):
    """Prints out all the common multiples of parameters X and Y less than Z."""
    
    dividend_int = 1
    
    while dividend_int < Z:
        if not dividend_int % X and not dividend_int % Y:
            print(dividend_int, end=' ')
        dividend_int += 1
        
common_multiples(6, 10, 100)
        
    
    
    