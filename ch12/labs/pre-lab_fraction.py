
################################################################################
## Class Fraction
################################################################################

debug = False

class Fraction( object ):
 
    def __init__( self, numer=0, denom=1 ):

        self.__numer = 0
        self.__denom = 1

        if type( numer ) == int and type( denom ) == int:
        
            self.__numer = numer
            self.__denom = denom
            self.__reduce()

        if debug:
            print( "__init__:", locals() )
            print()

    def __repr__( self ):

        return "Fraction: {}/{}".format( self.__numer, self.__denom )
       
    def __str__( self ):

        out_str = str( self.__numer )

        if self.__denom != 1:
            
            out_str = out_str + "/" + str( self.__denom )

        return out_str

    def __add__( self, other ):
        
        # a/b + c/d  ==>  (ad+bc)/bd

        if type( other ) != Fraction:

            other = Fraction( other )

        top = (self.__numer * other.__denom) + (self.__denom * other.__numer)
        bottom = self.__denom * other.__denom

        if debug:
            print( "__add__:", locals() )
            print()
       
        return Fraction( top, bottom )

    def __sub__( self, other ):

        # a/b - c/d  ==>  (ad-bc)/bd

        if type( other ) != Fraction:

            other = Fraction( other )
            
        top = (self.__numer * other.__denom) - (self.__denom * other.__numer)
        bottom = self.__denom * other.__denom

        if debug:
            print( "__sub__:", locals() )
            print()
        
        return Fraction( top, bottom )

    def __radd__( self, other ):

        # operands reversed as part of invocation

        if debug:
            print( "__radd__:", locals() )
            print()

        return Fraction( other ) + self

    def __rsub__( self, other ):

        # operands reversed as part of invocation

        if debug:
            print( "__rsub__:", locals() )
            print()

        return Fraction( other ) - self
    
    def __eq__( self, other ):

        # a/b == c/d  ==>  ad/bd == cb/db

        if type( other ) != Fraction:

            other = Fraction( other )
        
        top1 = self.__numer * other.__denom
        top2 = other.__numer * self.__denom

        if debug:
            print( "__eq__:", locals() )
            print()
       
        return top1 == top2

    def __lt__( self, other ):

        # a/b < c/d  ==>  ad/bd < cb/db

        if type( other ) != Fraction:

            other = Fraction( other )
        
        top1 = self.__numer * other.__denom
        top2 = other.__numer * self.__denom

        if debug:
            print( "__lt__:", locals() )
            print()
       
        return top1 < top2

    def __gt__( self, other ):

        # a/b < c/d  ==>  ad/bd < cb/db

        if type( other ) != Fraction:

            other = Fraction( other )
        
        top1 = self.__numer * other.__denom
        top2 = other.__numer * self.__denom

        if debug:
            print( "__gt__:", locals() )
            print()
        
        return top1 > top2
    
    def __reduce( self ):

        a, b = self.__numer, self.__denom

        if not a > b:
            a, b = b, a
            
        while b!=0:
            rem = a%b
            a, b = b, rem
        
        self.__numer = self.__numer // a
        self.__denom = self.__denom // a

        if (self.__numer < 0 and self.__denom < 0) \
          or (self.__numer > 0 and self.__denom < 0):

            self.__numer = -self.__numer
            self.__denom = -self.__denom
