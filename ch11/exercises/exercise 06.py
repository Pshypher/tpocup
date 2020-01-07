# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:09:04 2018

@author: Pshypher
"""

class OnlineBook():
    
    def __init__(self,title_str,publisher_str,price_flt,author_list,isbn):
        """Initialize an instance of the class."""
        self.__title = title_str
        self.__publisher = publisher_str
        self.__price = price_flt
        self.__authors = author_list
        self.__isbn = isbn
        
    def get_title(self):
        """Returns the title of the book."""
        return self.__title
    
    def get_publisher(self):
        """Returns the publisher of the book."""
        return self.__publisher
    
    def get_price(self):
        """Returns the cost at which each copy of the book is sold."""
        return self.__price
    
    def get_author(self):
        """Returns the  list of authors who wrote the book."""
        return self.__authors
    
    def get_ISBN(self):
        """Returns the ISBN(International Standard Book Number)."""
        return self.__isbn
    
    def __str__(self):
        """String representation of an instance of the OnlineBook class."""
        authors_str = ', '.join(self.__authors)
        return "{} written by author(s) {} and published by {} costs ${:.2f}.\
\nISBN {}".format(self.__title,authors_str,self.__publisher,self.__price,
self.__isbn)
    
    