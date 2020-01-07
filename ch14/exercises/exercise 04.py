# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 23:16:14 2018

@author: Pshypher
"""
import csv

def read_file(file_pointer, call_records_list):
    '''Read file, using the reader constructor of the csv module.'''
    file_reader = csv.reader(file_pointer)
    for row in file_reader:
        call_records_list.append(row)
        
def fetch_longest_duration(call_records_list):
    '''Get the maximum duration of call made from the CDR list. 
    Returns a tuple.'''
    longest_duration = 0
    for record in call_records_list:
        try:
            duration = int(record[-1])
        except ValueError:
            print('Bad duration value!')
        else:
            if duration > longest_duration:
                longest_duration = duration
                try:
                    source,dest = record[1:-1]
                except ValueError:
                    source,dest = record[1].split(' ')
                    
    return source,dest,longest_duration

def incomplete_cdrs(call_records_list):
    '''Finds the number of garbled or incomplete records in the CDR.
    Returns an int.'''
    count = 0
    for record in call_records_list:
        if garbled_cdr(record):
            count += 1
            
    return count

def international_calls(call_records_list):
    '''Count the number of international calls made. Returns an int.'''
    local_calls = 0
    all_calls = 0
    
    for record_lst in call_records_list:
        record_str = ",".join(record_lst)
        try:
            record_str.index("null")
        except ValueError:
            local_calls += 1
        finally:
            all_calls += 1
            
    return all_calls - local_calls

def garbled_cdr(record_lst):
    '''Checks if a call record is garbled or incomplete.'''
    
    try:
        duration = int(record_lst[-1])
        source, dest = record_lst[1:-1]
        area_code, prefix, number = source.split('-')
        source_str = area_code + prefix + number
        source_int = int(source_str)
        area_code, prefix, number = dest.split('-')
        dest_str = area_code + prefix + number
        dest_int = int(dest_str)
    except ValueError:
        garbled_bool = True
    else:
        garbled_bool = False
        
    return garbled_bool

def call_date_records(call_records_list, date_lst):
    '''Query the CDR to get all calls made on a particular date.'''
    calls_lst = []
    for record_list in call_records_list:
        record_date, record_time = record_list[0].split(' ')
        record_date_lst = record_date.split('/')
        for i in range(len(record_date_lst)):
            if date_lst[i] != int(record_date_lst[i]):
                break
        else:
            if not garbled_cdr(record_list):
                calls_lst.append(record_list)
    
    return calls_lst

def call_hour_records(call_records_list, hour_int):
    '''Query the CDR to get all calls made during a particular hour.'''
    calls_lst = []
    for record in call_records_list:
        if not garbled_cdr(record):
            date,time = record[0].split(" ")
            call_record_hour_int = int(time.split(':')[0])
            if hour_int == call_record_hour_int:
                calls_lst.append(record)
                
    return calls_lst
         
def main():
    
    call_records_list = []
    
    while True:
        file_name = input("Enter file name: ")
        try:
            file_pointer = open(file_name, 'r')
        except IOError:
            print('Bad file name!')
        else:
            print('Opening file "{}"'.format(file_name))
            break
        
    read_file(file_pointer, call_records_list)
            
    source,dest,duration = fetch_longest_duration(call_records_list)
    print("Between {} and {} for {} minutes\n".format(source,dest,duration))
            
    num_bad_records = incomplete_cdrs(call_records_list)
    print("{:d} garbled or incomplete CDRs\n".format(num_bad_records))
    
    foreign_calls = international_calls(call_records_list)
    print("{:d} international call(s) were made.\n".format(foreign_calls))
            
    while True:
        date = input("Enter date in the format dd/mm/yyyy: ")
        try:
            date_lst = date.split('/')
            date_lst = [int(field) for field in date_lst]
            call_records = call_date_records(call_records_list, date_lst)
        except ValueError:
            print('wrong date format!')
        except IndexError:
            print('missing one or more fields in date!')
        else:
            for record in call_records:
                print(','.join(record))
            print()
            break
        
    while True: 
        hour = input('Enter hours between 00-23: ')
        try:
            hour_int = int(hour)
        except ValueError:
            print('wrong value for hour!')
        else:
            call_records = call_hour_records(call_records_list, hour_int)
            for record in call_records:
                print(','.join(record))
            break