# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:42:56 2018

@author: Pshypher
"""

class Bill(object):
    
    def __init__(self, items_lst=[]):
        self.__items_lst = items_lst
        self.__total = self.compute_total()
        
    def compute_total(self):
        """Calculate the grand total of the prices in the items list."""
        total = 0
        for item in self.__items_lst:
            total += item.get_price() * item.get_quantity()
            
        return total
            
    def __add__(self, other_Bill):
        """Add Bills together and eliminate duplicates."""
        items_list = []
        for item in self.__items_lst + other_Bill.__items_lst:
            # is item already in the list of items for the new Bill?
            item_names_lst = [elem.get_name() for elem in items_list]
            if item.get_name() in item_names_lst:
                index = item_names_lst.index(item.get_name())
                items_list[index].set_quantity(items_list[index].get_quantity()
                + item.get_quantity())
            else:
                items_list.append(item)
                
        return Bill(items_list)
    
    def __str__(self):
        """String representation of a Bill."""
        result_str = "items\n"
        for item in self.__items_lst:
            result_str += ' ' + str(item) + '\n'
        result_str += '\ngrand total: ${:.2f}'.format(self.__total)
        
        return result_str
            
            
class Item(object):
    
    def __init__(self, name_str='', price_flt=0.0, quantity=0):
        """Initialize attributes of an instance of the Item class."""
        name_str = name_str.capitalize()
        self.__name = name_str + 's' if quantity > 1 else name_str
        self.__price = price_flt
        self.__quantity = quantity
        
    def get_name(self):
        """Return the name of Item."""
        return self.__name
    
    def get_price(self):
        """Return the unit price of Item."""
        return self.__price
        
    def get_quantity(self):
        """Return the quantity of Item acquired."""
        return self.__quantity
        
    def set_quantity(self, quantity):
        """Increase or decrease the number of Items."""
        self.__quantity = quantity
        
    def __str__(self):
        """String representation of an Item."""
        return  '{:d} {} @${:.2f} each'.format(self.__quantity, 
                 self.__name, self.__price)