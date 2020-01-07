# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:43:30 2018

@author: Pshypher
"""

def gcd(bigger, smaller):
    """Calculate the greatest common divisor of two positive integers."""
    print('in gcd')
    if not bigger > smaller:        # swap if necessary so bigger > smaller
        bigger, smaller = smaller, bigger
    while smaller != 0:                         # 1. if smaller == 0, halt
        remainder = bigger % smaller            # 2. find remainder
        # print('calculation, big:{}, small:{}, rem:{}'.format(
        #         bigger, smaller, remainder))    # debugging
        bigger, smaller = smaller, remainder    # 3. reapply

    return bigger

def lcm(a,b):
    """Calculate the lowest common multiple of two positive integers."""
    print('in lcm')
    return (a*b)//gcd(a,b)  # Equation 12.1, // ensures an int is returned
    

class Rational(object):
    """Rational with numerator and denominator. Denominator
    parameter defaults to 1."""
    def __init__(self,numer,denom=1):
        print('in constructor')
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        """String representation for printing"""
        print('in str')
        return str(self.numer) + '/' + str(self.denom)
    
    def __repr__(self):
        """Used in interpreter. Call __str__ for now"""
        print('in repr')
        return self.__str__()
    
    def __add__(self, param):
        """Add two Rationals. Allows int as a parameter"""
        print('in add')
        if type(param) == int:  # convert ints to Rationals
            param = Rational(param)
        if type(param) == Rational:
            # find a common denominator (lcm)
            the_lcm = lcm(self.denom, param.denom)
            # multiply each by the lcm, then add
            numerator_sum = (the_lcm * self.numer/self.denom) + \
                (the_lcm * param.numer/param.denom)
            return Rational(int(numerator_sum), the_lcm)
        else:
            print('wrong type')     # problem: some type we cannot handle
            raise(TypeError)
        
    def __radd__(self, param):
        """Add two Rationals (reversed)"""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to param
        print("in radd")
        # mapping is already reversed so self will be Rational; call __add__
        return self.__add__(param)
    
    def __sub__(self, param):
        """Subtract two Rationals. Allow int as parameter"""
        print('in sub')
        if isinstance(param, int):
            param = Rational(param)
        if isinstance(param, Rational):
            # subtraction is the same but with '-' instead of '+'
            the_lcm = lcm(self.denom, param.denom)
            numerator_diff = (the_lcm * self.numer/self.denom) - \
                (the_lcm * param.numer/param.denom)
            return Rational(int(numerator_diff), the_lcm)
        else:
            print('wrong type')
            raise(TypeError)
    
    def __rsub__(self, param):
        """Subtract two Rationals(reversed)."""
        print('in rsub')
        if isinstance(param, int):
            param = Rational(param) # convert int to Rational
        if isinstance(param, Rational):
            the_lcm = lcm(param.denom, self.denom)
            numerator_diff = (the_lcm * param.numer/param.denom) - \
            (the_lcm * self.numer/self.denom)
            return Rational(int(numerator_diff), the_lcm)
        else:
            print('wrong type')
            raise(TypeError)
            
    def __mul__(self, param):
        """Multiply two Rationals together. Allow int parameter."""
        print('in mul')
        if isinstance(param, int):
            param = Rational(param)
        if isinstance(param, Rational):
            numerator_prod = self.numer * param.numer
            denominator_prod = self.denom * param.denom
            return Rational(numerator_prod, denominator_prod)
        else:
            print('wrong type')
            raise(TypeError)
            
    def __rmul__(self, param):
        """Multiply two Rationals(reversed)."""
        print('in rmul')
        return self.__mul__(param)
    
    def __div__(self, param):
        """Divide two Rationals. Allow int as parameter."""
        if isinstance(param, int):
            param = Rational(param)
        if type(param) == Rational:
            numerator = self.numer * param.denom
            denominator = self.denom * param.numer
            return Rational(numerator, denominator)
        else:
            print('wrong type')
            raise(TypeError)
            
    def __rdiv__(self, param):
        """Divide two Rationals(reversed). param is type int."""
        print('in rdiv')
        param = Rational(param)
        numerator = param.numer * self.denom
        denominator = param.denom * self.numer
        return Rational(numerator, denominator)
            
    def reduce_rational(self):
        """Return the reduced fractional value as a Rational."""
        print('in reduce')
        # find the gcd and then divide numerator and denominator by gcd
        the_gcd = gcd(self.numer,self.denom)
        return Rational(self.numer//the_gcd, self.denom//the_gcd)
    
    def __eq__(self,param_Rational):
        """Compare two Rationals for equality, return Boolean"""
        print('in eq')
        # reduce both; then check that numerators and denominators are equal
        reduced_self = self.reduce_rational()
        reduced_param = param_Rational.reduce_rational()
        return reduced_self.numer == reduced_param.numer and \
            reduced_self.denom == reduced_param.denom