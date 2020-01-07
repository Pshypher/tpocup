# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:14:38 2018

@author: Pshypher
"""

def open_file():
    '''Prompts user for the name of a file containing data for three species of
    Irises: setosa, virginica, and versicolor.'''
    found = False
    while not found:
        try:
            file_name = input("Enter name of file: ")
            file_pointer = open(file_name, 'r')
            found = True
        except IOError:
            print("*** unable to open file ***")
            
    return file_pointer

def get_average_values_iris_species(iris_file_obj, iris_species_dict):
    '''Reads each line of the file, and finds the average of the sepal length, 
    sepal width, petal length and petal width of each species of iris.'''
    for line_str in iris_file_obj:
        line_str = line_str.strip()
        if not line_str:
            continue
        sepal_length, sepal_width, petal_length, petal_width, iris_type = \
        line_str.split(',')
        if iris_type in iris_species_dict:
            iris_species_dict[iris_type][0] += float(sepal_length)
            iris_species_dict[iris_type][1] += float(sepal_width)
            iris_species_dict[iris_type][2] += float(petal_length)
            iris_species_dict[iris_type][3] += float(petal_width)
            iris_species_dict[iris_type][4] += 1  # the last field in the list is
            # used to count the number of a  particular iris species in the file
        else:
            iris_species_dict[iris_type] = [float(sepal_length), 
                             float(sepal_width), float(petal_length), 
                             float(petal_width), 1]
            
    # find the average of each of the parameters in each iris species, each of 
    # the fields in the list being the sum of sepals length and width, petals
    # length and width and the last being the total count of an iris type in 
    # the file
    for key, val in iris_species_dict.items():
        for i in range(len(val)-1):
            val[i] = val[i] / val[-1]
        # remove the last element (total count of an iris type) from the list
        val.pop()
        
def print_data_iris_species(iris_species_dict):
    '''Prints the average values of the sepal length, sepal width, petal length
    and petal width from the dictionary created using the file from 
    (http://archive.ics.uci.edu/ml).'''
    
    print("\n{:<16s} {:>13s} {:>13s} {:>13s} {:>13s}".format("Iris type",
          "Sepal length", "Sepal width","Petal length", "Petal width"))
    print('-'*72)
    for key, val in iris_species_dict.items():
        print("\n{:<15s}".format(key), end=': ')
        for data in val:
            print("{:>13.2f}".format(data), end=' ')
    
    
def main():
    # open file containing data of iris species
    iris_file_obj = open_file()
    iris_species_dict = {}
    # calculate the average value of each field for each iris type
    get_average_values_iris_species(iris_file_obj, iris_species_dict)
    # print out the values of the average for the sepal length and width, petal
    # length and width for each iris
    print_data_iris_species(iris_species_dict)
    
    
    