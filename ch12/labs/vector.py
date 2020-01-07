# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 18:46:39 2018

@author: Pshypher
"""
import math

###########################################################################
## Class Vector
###########################################################################

class Vector(object):
    
    def __init__(self,x=0,y=0):
        """Construct a Vector type."""
        self.__x = x
        self.__y = y
        
    def __str__(self):
        """String representation of a Vector, used for printing."""
        return "({:.2f}, {:.2f})".format(self.__x, self.__y)
    
    def __repr__(self):
        """Vector display in the Python shell."""
        return "Vector" + self.__str__()
    
    def __add__(self, param_Vector):
        """Adds two Vectors together. Returns a new Vector."""
        x_sum = self.__x + param_Vector.__x
        y_sum = self.__y + param_Vector.__y
        return Vector(x_sum, y_sum)
    
    def __sub__(self, param_Vector):
        """Subtracts two Vector. Returns a new Vector."""
        x = param_Vector.__x * -1
        y = param_Vector.__y * -1
        return self.__add__(Vector(x,y))
    
    def __mul__(self, param):
        """Multiplies two Vectors(dot product), or a Vector and a float(cross
        product). A dot product between two Vectors yields a scalar, while a 
        cross product between a float and a Vector returns a new Vector."""
        if type(param) == float or isinstance(param,int):
            x_scaled = self.__x * param
            y_scaled = self.__y * param
            result = Vector(x_scaled, y_scaled)
        elif isinstance(param,Vector):
            x = self.__x * param.__x
            y = self.__y * param.__y
            result = x + y
        else:
            print('wrong type')
            raise(TypeError)
            
        return result
    
    def __rmul__(self, param):
        """Multiplies a Vector and a float type (reversed). Returns a new 
        Vector object."""
        return self.__mul__(param)
    
    def __eq__(self, param):
        """Compares two Vector objects for equality. Returns True or False"""
        return self.__x == param.__x and self.__y == param.__y
    
    def magnitude(self):
        """Calculates the magnitude of the Vector. Returns a float."""
        return round(math.hypot(self.__x, self.__y), 2)
    
    def unit(self):
        """Conversion to a unit vector. Scales the Vector by the inverse of the
        magnitude."""
        magnitude_float = self.magnitude()
        if magnitude_float == 0:
            raise ValueError(self)
        self.__x = self.__x / magnitude_float
        self.__y = self.__y / magnitude_float
        
def main():
    # demonstrates the creation and use of all the methods of the Vector class.
    A = Vector(10,45)
    print("A.__str__() returns",A)
    print("A.__repr__() returns",repr(A))
    print()
    # scale Vector (cross product of Vector and a float type)
    print("A * 1/4 =", A * (1/4))
    print("6 * A =",6 * A)
    
    # add, subtract, and find the dot product between two Vectors
    B = Vector(15,9)
    print("B.__str__() returns", B)
    print("A + B =",A + B)
    print("B - A =",B - A)
    print("A * B =", A * B)
    print()
    
    # Calculate the magnitude of Vector(4,3)
    C = Vector(4,3)
    print("Vector.magnitude(C) returns",Vector.magnitude(C))
    # Convert Vector C to a unit vector
    print("C =",C)
    Vector.unit(C)
    print("C.unit() =", C)
    
    # zero vector cannot be scaled down to a unit vector
    zero_Vector = Vector()
    try:
        zero_Vector.unit()
        print(zero_Vector)
    except ValueError:
        print("Cannot convert zero vector to a unit vector")
    
    
    
    
    
        
        
