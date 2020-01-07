# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:15:52 2018

@author: Pshypher
"""


# find the manufacturer with the maximum number of worst cars made
def get_worst_manufacturer(cars_and_manufacturer_dict):
    '''Returns the name of the manufacturer with the highest number of bad cars
    made.'''
    num_cars_made = 0
    manufacturer_cars_dict = group_cars_by_manufacturer(
            cars_and_manufacturer_dict)
    for key, val in manufacturer_cars_dict.items():
        if len(val) > num_cars_made:
            manufacturer_str = key
            num_cars_made = len(val)
            
    return manufacturer_str, num_cars_made


def group_cars_by_manufacturer(cars_and_manufacturer_dict):
    '''Returns a dictionary with the collection of cars model made indexed by a
    key, the name of the manufacturer.'''
    manufacturer_cars_dict = {}
    for key,val in cars_and_manufacturer_dict.items():  
        if val in manufacturer_cars_dict:   # name of manufacturer already in 
                                            # dictionary?
            manufacturer_cars_dict[val].append(key)
        else:   # otherwise add the name of manufacturer as a key in the new
                # dictionary
            manufacturer_cars_dict[val] = [key]
        
    return manufacturer_cars_dict
    
             
# The company that has made the maximum number of worst cars is gotten from the 
# cars_and_manufacturer dictionary
cars_and_manufacturer_dict = {(1899,"Horsey Horseless"):"Uriah Smith",
                              (1990,"Ford Model T"):"Ford",
                              (1911,"Overland OctoAuto"):"Milton Reeves",
                              (1913,"Scripps-Booth Bi-Autogo"):\
                              "James Scripps-Booth",
                              (1920,"Briggs and Stratton Flyer"):"A.O. Smith \
                              Company",
                              (1934,"Chrysler/Desoto Airflow"):"Chrysler",
                              (1949,"Crosley Hotshot"):"Crosley Motors",
                              (1956,"Renault Dauphine"):"Renault",
                              (1957,"King Midget Model III"):\
                              "Claud Dry and Dale Orcutt",
                              (1957,"Waterman Aerobile"):" ‎Watermann \
                              Arrowplane Co.",
                              (1958,"Ford Edsel"):"Ford",
                              (1958,"Lotus Elite"):"Lotus",
                              (1958,"MGA Twin Cam"):"Morris Garages",
                              (1958,"Zunndapp Janus"):"Zundapp",
                              (1961,"Amphicar"):"Quandt Group",
                              (1961,"Corvair"):"Chevrolet",
                              (1966,"Peel Trident"):"General Motors",
                              (1970,"AMC Gremlin"):"American Motors",
                              (1970,"Triumph Stag"):"British Leyland",
                              (1971,
                               "Chrysler Imperial LeBaron Two-Door Hardtop"):\
                               "Chrysler",
                              (1971,"Ford Pinto"):"Ford",
                              (1974,"Jaguar XK-EV12 Series III"):"Jaguar",
                              (1975,"Bricklin SV1"):"Malcolm Bricklin",
                              (1975,"Morgan Plus 8 Propane"):"Morgan Motor \
                              Company",
                              (1975,"Triumph TR7"):"Triumph Motor Company",
                              (1975,"Trabant"):"VEB Sachsenring \
                              Automobilwerke Zwickau",
                              (1976,"Aston Martin Lagonda"):"Aston Martin",
                              (1976,"Chevy Chevette"):"Chevrolet",
                              (1978,"AMC Pacer"):"American Motors",
                              (1980,'Corvette 305 "California"'):"Chevrolet",
                              (1980,"Ferrari Mondial 8"):"Ferrari",
                              (1981,"Cadillac Fleetwood V-8-6-4"):"General Motors",
                              (1981,"De Lorean DMC-12"):"John Z. De Lorean",
                              (1982,"Cadillac Cimarron"):"General Motors",
                              (1982,"Camaro Iron Duke"):"Chevrolet",
                              (1984,"Maserati Biturbo"):"Maserati",
                              (1985,"Mosler Consulier GTP"):"Warren Mosler",
                              (1985,"Yugo GV"):"Malcolm Bricklin",
                              (1986,"Lamborghini LM002"):"Lamborghini",
                              (1995,"Ford Explorer"):"Ford",
                              (1997,"GM EV1"):"General Motors",
                              (1997,"Plymouth Prowler"):"Chrysler",
                              (1998,"Fiat Multipla"):"Fiat",
                              (2000,"Ford Excursion"):"Ford",
                              (2001,"Jaguar X-Type"):"Jaguar",
                              (2001,"Pontiac Aztek"):"General Motors",
                              (2002,"BMW 7-series"):"BMW",
                              (2003,"Hummer H2"):"General Motors",
                              (2004,"Chevy SSR"):"General Motors"}

manufacturer_str,num_cars = get_worst_manufacturer(cars_and_manufacturer_dict)

print("Company with maximum number of worst cars:",manufacturer_str,"with",
      num_cars,"car models.")
      
