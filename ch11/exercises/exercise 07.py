# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 19:11:04 2018

@author: Pshypher
"""
import datetime

class Patient(object):
    
    def __init__(self,unique_id,name,gender,age,address,phone_num,birth_date,
                 height,weight):
        """Initialises an instance of the Patient class."""
        self.__id = unique_id
        self.__name = name
        self.__sex = ["male","female"]
        self.__gender = self.__sex[gender]
        self.__age = age
        self.__address = address
        self.__phone_num = phone_num
        self.__birth_date = birth_date
        self.__height = height
        self.__weight = weight
        
    def get_id(self):
        """Returns the unique id of the patient."""
        return self.__id
    
    def set_id(self, unique_id):
        """Set new Patient ID."""
        self.__id = unique_id
    
    def get_name(self):
        """Returns the name of the patient."""
        return self.__name
    
    def set_name(self, name):
        """Change Patient name."""
        self.__name = name
    
    def get_gender(self):
        """Returns the gender of the patient."""
        return self.__gender
    
    def set_gender(self, gender):
        """Alter Patient gender."""
        self.__gender = self.__sex[gender]
        
    def get_age(self):
        """Returns the patient's age."""
        return self.__age
    
    def set_age(self, age):
        """Set Age of Patient."""
        self.__age = age
    
    def get_address(self):
        """Returns the address of the Patient."""
        return self.__address
    
    def set_address(self, address):
        """Set new address of Patient."""
        self.__address = address
    
    def get_phone_num(self):
        """Returns the phone number of the Patient."""
        return self.__phone_num
    
    def set_phone_num(self, phone_num):
        """Set phone number of Patient."""
        self.__phone_num = phone_num
    
    def get_birth_date(self):
        """Returns the date of birth of the Patient."""
        return self.__birth_date
    
    def set_birth_date(self, birth_date):
        """Change the Patient's birth date."""
        self.__birth_date = birth_date
    
    def get_height(self):
        """Returns the height of the Patient."""
        return self.__height
    
    def set_height(self, height):
        """Sets the Patient's height."""
        self.__height = height
    
    def get_weight(self):
        """Returns the weight of the Patient."""
        return self.__weight
    
    def set_weight(self, weight):
        """Adjust the weight of the Patient."""
        self.__weight = weight
    
    def __str__(self):
        """String representation of an instance of the Patient class."""
        return "ID: " + self.__id + "\nName: " + self.__name + "\nGender:" + \
    self.__gender + "\nAge: " + self.__age + "\nHeight: " + self.__height + \
    "\nWeight: " + self.__weight
    
    
class Doctor(object):
    
    def __init__(self,name: str,reg_no: str,qualification: int,field: int,
                 phone_num: str,office_hours: set,location: str):
        """Initialises an instance of the Doctor class."""
        self.__name = name
        self.__reg_no = reg_no
        self.__medical_qualification = ["DO","MD"]
        self.__qualification = self.__medical_qualification[qualification]
        self.__field = ["surgery","pediatrics","obstetrics","gynecology"]
        self.__specialization = self.__field[field]
        self.__phone_num = phone_num
        # office_hours is a set of tuple pair containing an interval of time
        # objects from the datetime module (start_shift_time, end_shift_time)
        self.__office_hours = office_hours
        self.__location = location
        
    def get_name(self):
        """Returns the doctor's name."""
        return self.__name
    
    def get_reg_no(self):
        """Returns the doctor's registration number."""
        return self.__reg_no
    
    def get_qualification(self):
        """Returns the qualification of the doctor."""
        return self.__qual
    
    def get_specialization(self):
        """Returns the specialization of the doctor."""
        return self.__spec
    
    def get_phone_num(self):
        """Returns the phone number of the doctor."""
        return self.__phone_num
    
    def get_office_hours(self):
        """Returns each doctor's office hours."""
        return self.__office_hours
    
    def set_office_hours(self,start_time: datetime.time,
                         end_time: datetime.time):
        """Set new office hour interval for an instance of the Doctor class."""
        self.__office_hours.add((start_time, end_time))
        
    def delete_hours(self, start_time: datetime.time,
                     end_time: datetime.time):
        """Deletes a time interval in the sequence of office hours interval
        from an instance of the Doctor class."""
        self.__office_hours.remove((start_time, end_time))
    
    def get_location(self):
        """Return a string, location of an instance of the Doctor class."""
        return self.__location
    
    def set_location(self,location):
        """Changes the prior location of an instance of the Doctor class."""
        self.__location = location
        
    def __str__(self):
        """String representation of an instance of the Doctor class."""
        return "Doctor {} with registration number {} and {} qualification, \
    specializes in {}, contact  {}".format(self.__name,self.__reg_no,
    self.__qual,self.__spec,self.__phone_num)
    
    
class PatientRecord(object):
    
    def __init__(self,last_checkup: datetime.date, ailments: list, 
                 medicines: list, checkup_cost: float, report: str):
        """Initialises an instance of the PatientRecord class."""
        self.__last_checkup = last_checkup
        self.__health_problems = ailments
        self.__prescribed_drugs = medicines
        self.__checkup_cost = checkup_cost
        self.__final_report = report
        
    def get_checkup_date(self):
        """Returns the date of last checkup."""
        return self.__last_checkup
    
    def get_ailments(self):
        """Returns a list of ailments of a patient.""" 
        return self.__health_problems
    
    def get_prescribed_drugs(self):
        """Returns the drugs prescribed to a patient."""
        return self.__prescribed_drugs
    
    def add_drug(self, drug: str):
        """Add some drugs to the list of prescribed drugs."""
        self.__prescribed_drugs.append(drug)
        
    def get_checkup_cost(self):
        """Returns the cost of the checkup."""
        self.__checkup_cost
        
    def adjust_cost(self, cost: float):
        """Adjust the price of patient checkup."""
        self.__checkup_cost = cost
        
    def get_report(self):
        """Return the final report generated for the patient after checkup."""
        return self.__final_report
    
    def set_report(self,report):
        """Alter the report generated for a patient."""
        self.__final_report = report  