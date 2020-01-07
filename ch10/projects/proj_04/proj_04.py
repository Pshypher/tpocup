# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:34:27 2018

@author: Pshypher
"""
from operator import itemgetter

# Predicting religion with flags

# naming protocol
#   - each variable with the suffix "religion" is a dictionary
#   - each variable with a suffix "pairs"is a list of tuples

# Constants
NAME = "name"
RELIGION = "religion"
BARS = "bars"
STRIPES = "stripes"
COLOURS = "colours"
RED = "red"
BLUE = "blue"
GREEN = "green"
GOLD = "gold"
WHITE = "white"
BLACK = "black"
ORANGE = "orange"
MAINHUE = "mainhue"
CIRCLES = "circles"
CROSSES = "crosses"
SALTIRES = "saltires"
QUARTERS = "quarters"
SUNSTARS = "sunstars"
CRESCENT = "crescent"
TRIANGLE = "triangle"
ICON = "icon"
ANIMATE = "animate"
TEXT = "text"
TOPLEFT = "top-left"

QUIT = "done"

boolean_attr_tuple = (RED,BLUE,GREEN,GOLD,WHITE,BLACK,ORANGE,CRESCENT,TRIANGLE,
                     ICON,ANIMATE,TEXT)
nominal_attr_tuple = (MAINHUE,TOPLEFT)
# Attributes are classified into continuous, nominal and boolean
# every other attribute not found in both lists are continuous attributes

def make_training_set(input_file) -> dict:
    '''Parses the document containing the attributes for the flags of each 
    countries to a dictionary of attributes.Returns a list of dictionaries.'''
    training_set = []
    
    # make a dictionary of the flag attributes for each country in input_file   
    # and append the dictionary to the countries_attrs_list
    for line_str in input_file:
        country_dict = {}
        line_str = line_str.strip()
        line_list = line_str.split(',')
        religion_int = int(line_list[6])
        religion_str = "christian" if religion_int == 0 or religion_int == 1 \
        else "other"
        country_dict[NAME] = line_list[0].strip()
        country_dict[RELIGION] = religion_str
        country_dict[BARS] = int(line_list[7])
        country_dict[STRIPES] = int(line_list[8])
        country_dict[COLOURS] = int(line_list[9])
        country_dict[RED] = int(line_list[10])
        country_dict[GREEN] = int(line_list[11])
        country_dict[BLUE] = int(line_list[12])     
        country_dict[GOLD] = int(line_list[13])
        country_dict[WHITE] = int(line_list[14])
        country_dict[BLACK] = int(line_list[15])
        country_dict[ORANGE] = int(line_list[16])
        country_dict[MAINHUE] = line_list[17].strip()
        country_dict[CIRCLES] = int(line_list[18])
        country_dict[CROSSES] = int(line_list[19])
        country_dict[SALTIRES] = int(line_list[20])
        country_dict[QUARTERS] = int(line_list[21])
        country_dict[SUNSTARS] = int(line_list[22])
        country_dict[CRESCENT] = int(line_list[23])
        country_dict[TRIANGLE] = int(line_list[24])
        country_dict[ICON] = int(line_list[25])
        country_dict[ANIMATE] = int(line_list[26])
        country_dict[TEXT] = int(line_list[27])
        country_dict[TOPLEFT] = line_list[28].strip()
        training_set.append(country_dict)
        
    input_file.close()  # close the file
    # return list of flag attributes for all 194 countries
    return training_set

def parse_flag_attributes(religion_dict: dict, flag_dict: dict):
    '''Sums up each continuous attributes, increment each boolean attribute by
    1 if it exists in the flag and increases the count of each non-numeric 
    field of colors in the dictionary of color:count pairs mapped to the key,
    (i.e. the name of the non-numeric attribute).'''
    for attr in flag_dict:
        # for a boolean attr, count the number of times it is present 
        # within a flag for countries that are of a predominant religion
        if attr in boolean_attr_tuple and flag_dict[attr]:
            religion_dict[attr] = religion_dict.get(attr,0) + 1
            # increase the count of each non_numeric color field 
        elif attr in nominal_attr_tuple:
            if attr in religion_dict:
                religion_dict[attr][flag_dict[attr]] = religion_dict[attr].get(
                        flag_dict[attr],0) + 1
            else:
                religion_dict[attr] = {flag_dict[attr]: 1}
        else:   # sum up the values of each numeric continous attribute
            religion_dict[attr] = religion_dict.get(attr, 0) + flag_dict[attr]
            
def set_non_numeric_fields(religion_dict: dict):
    '''Sets the dominant color for non-numeric fields of the dictionary.'''
    for attr in religion_dict:
        if attr in nominal_attr_tuple:
            color_count_pairs = list(religion_dict[attr].items())
            color_count_pairs.sort(reverse=True,key=itemgetter(1))
            color_str,count = color_count_pairs[0]
            religion_dict[attr] = color_str
            
def set_average_numeric_attributes(religion_dict: dict, count: int):
    '''Calculates and set the average for all the numeric fields including 
    boolean fields.'''
    for attr in religion_dict:
        if attr == NAME or attr == RELIGION or attr in nominal_attr_tuple:
            continue
        religion_dict[attr] = religion_dict[attr] / count
                
def train_classifier(training_set: list):
    '''Finds the averages for each attribute of the flags for all countries 
    that are predominantly christians and countries with other predominant 
    religions.Returns a tuple of 2 dictionaries.'''
    christian_religion = {}
    other_religion = {}
    christian_count = 0
    others_count = 0
    
    for flag_dict in training_set:
        country_name = flag_dict.pop(NAME)   # remove country_name and religion 
        religion_str = flag_dict.pop(RELIGION)   # from dictionary, flag
        if religion_str == "christian":
            parse_flag_attributes(christian_religion, flag_dict)
            christian_count += 1
        else:
            parse_flag_attributes(other_religion, flag_dict)
            others_count += 1
        # add the name and predominant religion of the country back to the
        # details for each flag
        flag_dict[NAME] = country_name
        flag_dict[RELIGION] = religion_str
        
    # sort and select the most dominant color for countries of both predominant
    # religions(chrisitians, others)
    set_non_numeric_fields(christian_religion)
    set_non_numeric_fields(other_religion)
    
    # find the average of the numeric fields
    set_average_numeric_attributes(christian_religion,christian_count)
    set_average_numeric_attributes(other_religion,others_count)
    
    # return classifier(s)
    return christian_religion,other_religion

def classify_country_flag(flag_dict: dict, dict1: dict, dict2: dict) -> str:
    '''Classifies the country as christian or other religion based on the 
    attributes of its flag and the values of the classifiers in dict1 and 
    dict2. Returns a string'''
    
    # dict1 holds the classifier values for the countries that are 
    # predominantly christians, dict2 other religions
    christian_attrs_cnt = 0
    other_religion_attrs_cnt = 0
    
    for attr in flag_dict:
        if attr == NAME or attr == RELIGION:
            continue
        if attr in boolean_attr_tuple:
            if dict1[attr] > dict2[attr]:
                christian_attrs_cnt += 1
            else:
                other_religion_attrs_cnt += 1
        elif attr in nominal_attr_tuple:
            if dict1[attr] == flag_dict[attr]:
                christian_attrs_cnt += 1
            else:
                other_religion_attrs_cnt += 1
        else:
            if abs(flag_dict[attr] - dict1[attr]) < abs(
                    flag_dict[attr] - dict2[attr]):
                christian_attrs_cnt += 1
            else:
                other_religion_attrs_cnt += 1
                
    return "Christian" if christian_attrs_cnt >= other_religion_attrs_cnt else\
"not Christian"
            
def main():
    # open file
    input_file = open("flag.data.txt", 'r')
    # create training set
    training_set = make_training_set(input_file)
    dict1,dict2 = train_classifier(training_set)
    
    print("\nFlags")
    country_str = input("Enter a country: ")
    while country_str != QUIT:
        for flag_dict in training_set:
            if flag_dict[NAME] == country_str:
                result_str = classify_country_flag(flag_dict, dict1, dict2)
                print(country_str + " is " + result_str)
        country_str = input("Enter a country: ")
        
if __name__ == "__main__":
    main()