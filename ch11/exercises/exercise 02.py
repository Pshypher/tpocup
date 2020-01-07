# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:25:45 2018

@author: Pshypher
"""

class ShoppingCart(object):
    """A shopping cart class."""
    
    def __init__(self):
        """Initializes an instance of the ShoppingCart class."""
        self.__cart = []
        
    def add_item(self, item: object):
        """Adds an item to cart."""
        self.__cart.append(item)
        
    def remove_item(self, category_str: object, item_id: int):
        """Removes selected item from the cart."""
        for i,item in enumerate(self.__cart):
            if item_id == item.get_id() and type(item)==eval(category_str):
                self.__cart.pop(i)
                break
        else:
            print("***Item {} id {} not found.***".format(category_str,
                  item_id))
                
    def purchase(self):
        """Calculates the total sum of items in cart, empties the cart and
        returns the total sum."""
        total_sum_flt = 0.0
        
        for item in self.__cart:
            total_sum_flt += item.get_cost()
    
        return total_sum_flt
    
    def empty_cart(self):
        """Remove all items from the cart."""
        self.__cart.clear()
        
    def __str__(self):
        """Returns a string representation of items in cart."""
        shopping_cart_str = ''
        
        for item,amount_qty_pair in self.__cart.items():
            amount_flt,qty_int = amount_qty_pair
            shopping_cart_str+=item+" x{d} ".format(qty_int)+"each costs "+ \
            "${:.2f}".format(amount_flt)+'\n'
            
        return shopping_cart_str
    
class TV(object):
    
    _id = 0
    
    def __init__(self,brand_str,model_str,amount_float):
        """Initializes an instance of the TV class."""
        self.__id = TV._id
        TV._id += 1
        self.__brand = brand_str
        self.__model = model_str
        self.__cost = amount_float
        
    def get_cost(self):
        """Returns the cost of TV."""
        return self.__cost
        
    def get_id(self):
        """Returns TV identifier."""
        return self.__id
        
    def __str__(self):
        return self.__brand + " TV, model " + self.__model + " costs ${:.2f}"\
        .format(self.__cost)
        
class BoomBox(object):
    
    _id = 0 

    def __init__(self,brand_str,amount_float):
        """Initializes an instance of the BoomBox class."""
        self.__id = BoomBox._id
        BoomBox._id += 1
        self.__brand = brand_str
        self.__cost = amount_float
        
    def get_cost(self):
        """Returns the cost of BoomBox item."""
        return self.__cost
        
    def get_id(self):
        """Return BoomBox object id."""
        return self.__id
        
    def __str__(self):
        return self.__brand + " boombox " + "costs ${:.2f}".format(self.__cost)
        
class iPod(object):
    
    _id = 0
    
    def __init__(self,model_str,amount_float):
        """Initializes an instance of the iPod class."""
        self.__id = iPod._id
        iPod._id += 1
        self.__model = model_str
        self.__cost = amount_float
        
    def get_cost(self):
        """Returns the cost of iPod."""
        return self.__cost
        
    def get_id(self):
        """Returns an iPod identifier."""
        return self.__id
        
    def __str__(self):
        return "Ipod {} ".format(self.__model) + "costs ${:.2f}".format(self.__cost)
        
class Camcorder(object):
    
    _id = 0
    
    def __init__(self,brand_str,model_str,amount_float):
        """Initializes an instance of the CamCorder class."""
        self.__id = Camcorder._id
        Camcorder._id += 1
        self.__brand = brand_str
        self.__model = model_str
        self.__cost = amount_float
        
    def get_cost(self):
        """Returns the cost of the Camcorder."""
        return self.__cost
        
    def get_id(self):
        """Returns id of Camcorder."""
        return self.__id
        
    def __str__(self):
        return self.__brand + " cam, model " + self.__model + " costs ${:.2f}"\
        .format(self.__cost)
    