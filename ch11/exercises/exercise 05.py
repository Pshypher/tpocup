# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 12:30:41 2018

@author: Pshypher
"""

class Ticket(object):
    
    def __init__(self,start_str,destination_str,date_str,mode_int,
                 price_flt,num_persons,name_str):
        """Initializes an instance of the Ticket class."""
        self.__start = start_str
        self.__destination = destination_str
        self.__date = date_str
        self.__modes = ["Economy","First","Business"]
        self.__passenger_class = self.__modes[mode_int]
        self.__price = price_flt
        # number of person(s) admitted by ticket
        self.__num_persons = num_persons
        self.__name = name_str
        
    def get_start(self):
        """Returns the location a passenger is travelling from."""
        return self.__start
    
    def get_destination(self):
        """Returns the destination the passenger is travelling to."""
        return self.__destination
    
    def get_date(self):
        """Returns the date the passenger is scheduled to travel."""
        return self.__date
    
    def get_travel_class(self):
        """Returns the class booked by the passenger."""
        return self.__passenger_class
    
    def get_price(self):
        """Returns ticket price."""
        return self.__price
    
    def get_num_persons(self):
        """Return the number of persons admitted by the ticket."""
        return self.__num_persons
    
    def get_name(self):
        """Returns the name of passenger who booked the ticket."""
        return self.__name
    
    def __str__(self):
        """String representation of an instance of the Ticket class."""

        return "{} scheduled to travel from {} to {} under the {} class \
on {}.\nTicket sold for ${:.2f} admits only {} person(s).".format(self.__name,
self.__start,self.__destination,self.__passenger_class,self.__date,self.__price,
self.__num_persons)

 
    
    
        