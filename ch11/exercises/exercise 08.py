# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 08:46:29 2018

@author: Pshypher
"""

class Medal(object):
    
    def __init__(self,name: str,country: str,event: str,medal_int: int):
        """Initialises an instance of the Medal class."""
        self.__name = name
        self.__country = country
        self.__event = event
        self.__medals_list = ["gold","silver","bronze"]
        self.__medal = self.__medals_list[medal_int]
        
    def get_name(self):
        """Return name of athlete."""
        return self.__name
    
    def set_name(self, name: str):
        """Sets the name of the athlete."""
        self.__name = name
        
    def get_country(self):
        """Returns the nationality of the athlete."""
        return self.__country
    
    def set_country(self,country):
        """Sets the nationality of the athlete."""
        self.__country = country
        
    def get_medal(self):
        """Returns the medal won by athete."""
        return self.__medal
    
    def set_medal(self, medal_int: int):
        """Sets the medal given out to athlete."""
        self.__medal = self.__medals_list[medal_int]
        
    def __str__(self):
        """String representation of the Medal class."""
        return "{} medal won by {} from {} at the {} event".format(self.__medal,
                self.__name, self.__country, self.__event)