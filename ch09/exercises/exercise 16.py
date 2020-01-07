# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:54:05 2018

@author: Pshypher
"""

QUIT = ''
countries_dict = {}

country_str = input("Enter country name or enter to quit: ")
while country_str != QUIT:  # populate dictionary with countries and 
                            # their capitals
    capital_str = input("Capital of {}: ".format(country_str))
    countries_dict[country_str] = capital_str  
    country_str = input("Enter country name or enter to quit: ")

# display the capitals in alphabetical order
print()
capitals_list = list(countries_dict.values())
capitals_list.sort()
for capital in capitals_list:
    print(capital)