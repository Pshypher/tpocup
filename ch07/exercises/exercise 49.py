# Adds two fractions together, fractions are represented in a tuple
# Fraction -> (numerator, denominator)
# Denominators are assumed to greater than 0 or less than 0 
# Unless otherwise stated, each variable is assumed to be a tuple

import math

def add_fraction(operand_1, operand_2):
    """Sums both fractions operand_1 + operand_2 together, both operands are
        fractions represented as a tuple: Returns a tuple which is the sum
        of both fractions."""
    # Find the lowest common multiple of both operands denominator
    lcm_int = find_lcm(operand_1[1], operand_2[1])
    
    numerator_1_int = operand_1[0]*(lcm_int//operand_1[1])
    numerator_2_int = operand_2[0]*(lcm_int//operand_2[1])
    
    fraction_sum = numerator_1_int+numerator_2_int, lcm_int
    
    # Eliminate a common factor from both numerator and denominator and reduce
    # the sum to its simplest terms
    gcd = math.gcd(fraction_sum[0], fraction_sum[1])
    return fraction_sum[0]//gcd, fraction_sum[1]//gcd


def find_lcm(first_int, second_int):
    """Find the lowest common multiple of both integers: Returns a
        number which is the lowest common multiple of both numbers."""
    gcd = math.gcd(first_int, second_int)
    return (first_int//gcd * second_int//gcd * gcd)
    
def mult_fraction(operand_1, operand_2):
    """Multiplies two fractions which are tuples (numerator, denominator)
        together.Returns a fraction that is the multiple of both operands."""
    # Multiply the numerator of both operands together
    numerator = operand_1[0] * operand_2[0]
    # Multiply the denominator of both operands together
    denominator = operand_1[1] * operand_2[1]
    # Eliminate the common factors from both the numerator and denominator
    factor = math.gcd(numerator, denominator)
    return numerator//factor, denominator//factor
    