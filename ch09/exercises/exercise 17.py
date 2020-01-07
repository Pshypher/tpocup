# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:32:34 2018

@author: Pshypher
"""

# reads a file with the format of every line City,Country, records the 
# information in a dictionary and displays the number of cities in each 
# country

file_pointer = open("cities.txt", 'r')
city_country_dict = {}

for line_str in file_pointer:
    city, country = line_str.split(', ')
    city = city.strip()
    country = country.strip()
    city_country_dict[city] = country
    
# count the number of cities in the city country dictionary
country_cities_count_dict = {}
for key,val in city_country_dict.items():
    country_cities_count_dict[val] = country_cities_count_dict.get(val, 0) + 1
    
print()
# display the number of cities in each country
for country in country_cities_count_dict:
    print(country,':',country_cities_count_dict[country])
    

        

