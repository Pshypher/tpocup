# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:50:55 2018

@author: Pshypher
"""
# Prompt user for file_name, open file if found otherwise re-prompt for 
# file_name

# Iterate through each line of the .csv, split each row on a comma (',') and 
# assign the resulting list to a variable for each row in the .csv file

# Create a dictionary indexed by states, each state maps to a value that is a 
# list of dictionaries
    # {"Illinois": [{"crop":"corn", "year":2000, "value":13},
    #               {"crop":"corn", "year":2001, "value":12}, {...}, ...],
    #  "Indiana": [{"crop":"corn", "year":2000, "value":13}], {...}, ...],
    # ...}
    
# To display the data for each crop of "All GE varieties", build a dictionary
# indexed by the crop name
    # Each crop (key) maps to a dictionary, the inner dictionary has as its keys 
    # the names of some states. Each state maps to a list of tuples containing  
    # the % of CM adoption of each crop, and the year.

from operator import itemgetter
import string


STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 
              'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
              'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
              'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
              'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
              'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
              'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
              'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
              'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
              'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


def open_file():
    '''Opens a file and returns the file pointer object.'''
    found = False
    while not found:
        try:
            file_name = input('Enter the name of file(e.g "data.csv"): ')
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("*** unable to open file ***")
            
    return file_pointer


def read_file(file_pointer, gm_crops_per_state_dict):
    '''Reads each line of the file and modifies the state_gm_crop dictionary,
    mapping each state to a list of dictionaries of each genetically engineered
    crop adopted over the years 2000-2016 and the percentage adopted.'''
    
    for line_str in file_pointer:
        line_str = line_str.strip().strip(string.punctuation)
        if "All GE varieties" in line_str:
            gm_crop_list = line_str.split(',')
            try:
                state = gm_crop_list[0].strip()
                crop = gm_crop_list[1].strip()
                year = gm_crop_list[4].strip()
                percentage = gm_crop_list[6].strip()
            except IndexError:
                continue
            
            if state in STATES: # is the state amongst the states in the USA
                # append a dictionary to the list each time for each state 
                # after mapping the key (state) with an empty list
                if state in gm_crops_per_state_dict:
                    gm_crops_per_state_dict[state].append({"crop":crop, 
                                           "year":year, "%age":percentage})
                else:   # map a state with an [] if its not in the dictionary
                    gm_crops_per_state_dict[state] = [{"crop":crop, "year":year,
                                      "%age":percentage}]
        
 
def index_by_crop_name(state_gm_crop_dict, gm_crops_dict):
    '''Build a map such that each key is the name of a crop and the 
    corresponding value is a list of tuples, each tuple containing the name of 
    a state, the year and the %age of adoption.'''
    # each state maps to a list of dictionaries
    for state,gm_crop_list in state_gm_crop_dict.items():
        # For each dictionary within the list get the crop,year & %age adoption
        for crop_dict in gm_crop_list:
            crop_name = crop_dict["crop"]
            year_int = int(crop_dict["year"])
            percentage_int = int(crop_dict["%age"])
            
            # a nested dictionary, the crop being the outer key, the inner keys
            # are the states indexing a list of tuples (%age, year)
            
            # append the tuple to the list if the state & the name of the crop
            # are already inner and outer keys in the dictionary repectively
            if crop_name in gm_crops_dict and state in gm_crops_dict[
                    crop_name]:
                gm_crops_dict[crop_name][state].append(
                        (percentage_int,year_int))
            # assign to a list of (%age, year) tuple, 1 item long if the state
            # isn't already in the inner dictionary mapped to each crop
            elif crop_name in gm_crops_dict:
                gm_crops_dict[crop_name][state] = [(percentage_int,year_int)]
            # otherwise, empty inner dictionary for crops not in the dictionary
            else:
                gm_crops_dict[crop_name] = {}
                

def display_gm_adoption(gm_crops_per_state_dict):
    '''Displays the minimum, maximum %age of the genetically engineered crop
    for each state and the corresponding year of the highest and lowest %age
    adoption of the gm crop.'''
    gm_crops_dict = {}
    index_by_crop_name(gm_crops_per_state_dict, gm_crops_dict)   
    crops_list = [key for key in gm_crops_dict]
    crops_list.sort()
    
    # group the display per crop
    for crop in crops_list:
        print("Crop:", crop)
        print("{:<20s}{:<8s}{:<6s}{:<8s}{:<6s}".format("State","Max Yr","Max",
              "Min Yr","Min"))
        gm_crop_adoption_in_states_dict = gm_crops_dict[crop]
        states_list = [key for key in gm_crop_adoption_in_states_dict]
        states_list.sort()
        for state in states_list:
            # sort the list based on the percentage of gm crops planted per 
            # year in descending order
            adoption_in_state_per_year_list = gm_crops_dict[crop][state]
            # sort based on the year also so that the year with the lower value
            # is selected if the adoptions of gm crops are the same
            adoption_in_state_per_year_list.sort(key=itemgetter(0,1),reverse=True)
            # select the values with the highest %age of gm crops planted 
            max_percentage,max_year = adoption_in_state_per_year_list[0]
            # select the values with the lowest adoption %age
            min_percentage,min_year = adoption_in_state_per_year_list[-1]
            print("{:<20s}{:<8d}{:<6d}{:<8d}{:<6d}".format(state,max_year,
                  max_percentage,min_year,min_percentage))
        
        print()


def main():
    # Get file to be read from
    file_pointer = open_file()
    # Read each line from the file and build a dictionary mapping each state to
    # the adoption %age per year of gm crops planted and what crop was planted
    gm_crops_per_state_dict = {}
    read_file(file_pointer, gm_crops_per_state_dict)
    # Output gm adoption of each crop in a nicely formatted manner
    display_gm_adoption(gm_crops_per_state_dict)


if __name__=="__main__":
    main()
    
    