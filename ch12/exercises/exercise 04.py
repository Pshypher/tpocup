# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:07:58 2018

@author: Pshypher
"""

class Vehicle(object):
    
    def __init__(self, model_year, vehicle_id, epa_class, engine, transmission, 
                 options, epa_mileage=0, mileage=0):
        print('in vehicle constr')
        self.__model_year = model_year
        self.__vehicle_id = vehicle_id
        self.__epa_class = epa_class
        self.__engine = engine
        self.__transimission = transmission
        self.__options = options
        self.__epa_mileage = epa_mileage
        self.__mileage = mileage
        
    def get_vin(self):
        """Return Vehicle Identification Number."""
        return self.__vehicle_id
    
    def get_model_year(self):
        """Return the year model of vehicle was manufactured."""
        return self.__model_year
    
    def get_mileage(self):
        """Return total mileage of Vehicle instance."""
        return self.__mileage
    
    def get_epa_class(self):
        """Return EPA class."""
        return self.__epa__class
    
    def get_epa_mileage(self):
        """Return EPA mileage."""
        return self.__epa_mileage
    
    def get_engine(self):
        """Return engine specification."""
        return self.__engine
    
    def get_transmission(self):
        """Return Vehicle transmission."""
        return self.__transmission
    
    def get_options(self):
        """Get options in Vehicle."""
        return self.__options
        
    def __str__(self):
        """String representation for an instance of a Vehicle class."""
        result_str =  "vehicle information\n vin({:s})\n year: {:d}\n \
mileage: {:d}\n epa class: {}\n epa mileage: {}\n engine: {}\n\
 transmission: {}\n options: ".format(self.__vehicle_id,self.__model_year, 
 self.__mileage, self.__epa_class, self.__epa_mileage, self.__engine,
 self.__transmission, ', '.join(self.__options))
        return result_str
    
class Car(Vehicle):
    
    def __init__(self, model_year, vehicle_id, epa_class, engine, transmission, 
                 options, epa_mileage, mileage):
        print('in car constr')
        Vehicle.__init__(self, model_year, vehicle_id, epa_class, engine,
                         transmission, options, epa_mileage, mileage)

class Truck(Vehicle):
    
    def __init__(self, model_year, vehicle_id, epa_class, engine, transmission, 
                 options, epa_mileage, mileage):
        print('in truck constr')
        Vehicle.__init__(self, model_year, vehicle_id, epa_class, engine,
                         transmission, options, epa_mileage, mileage)
    

class SUV(Vehicle):
    
    def __init__(self, model_year, vehicle_id, epa_class, engine, transmission, 
                 options, epa_mileage, mileage):
        print('in suv constr')
        Vehicle.__init__(self, model_year, vehicle_id, epa_class, engine,
                         transmission, options, epa_mileage, mileage)
        
class Minivan(Vehicle):
    
    def __init__(self, model_year, vehicle_id, epa_class, engine, transmission, 
                 options, epa_mileage, mileage):
        print('in minivan constr')
        Vehicle.__init__(self, model_year, vehicle_id, epa_class, engine,
                         transmission, options, epa_mileage, mileage)
    