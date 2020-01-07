# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 11:03:38 2018

@author: Pshypher
"""
import csv

class CommandException(Exception):
    pass

class InsertException(Exception):
    pass

def open_file():
    '''Opens a file, reprompts user for filename if bad file name is given.'''
    found = False
    while not found:
        file_name = input('Enter file name: ')
        try:
            file_pointer = open(file_name, 'r')
        except IOError:
            print('Bad file name!')
        else:
            found = True
            
    return file_pointer

def display(sheet_list):
    '''Displays the records in a csv file.'''
    for row in sheet_list:
        print(','.join(row))
        
def write(sheet_list):
    '''Outputs the spreadsheet data in sheet_list to a CSV file.'''
    file_name = input("Enter file name: ")
    file_desc = open(file_name + '.csv', 'w')
    file_Writer = csv.writer(file_desc)     # create csv writer object
    for row in sheet_list:
        file_Writer.writerow(row)
        
    file_desc.close()
    
def change(cell_tuple,sheet_list):
    '''Change the contents of a cell.'''
    row,col = cell_tuple
    val_str = input("Value to be inserted: ")
    try:
        sheet_list[row][col] = val_str
    except IndexError:
        print('could not change cell value')
        print('outside the range of values for the spreadsheet (row,column)')
        
def delete(line_str,sub_int,sheet_list):
    '''Removes a row or column from the spreadsheet.'''
    if line_str == 'r':
        try:
            sheet_list.pop(sub_int)
        except IndexError:
            print('row out of spread-sheet range')
    elif line_str == 'c':
        try:
            for row in sheet_list:
                row.pop(sub_int)
        except IndexError:
            print('column out of range')
    else:
        raise CommandException


def insert(line_str,sub_int,sheet_list):
    '''Insert a row or column of data into a spreadsheet.'''
    
    try:
        strip_str = input("Insert row or column(a comma seperated list of \
values): ")
        strip_lst = strip_str.split(',')
    
        if line_str == 'r':
            row_size = len(sheet_list[0])
            pad_int = row_size-len(strip_lst)
            if pad_int < 0:
                raise InsertException
            strip_lst = strip_lst + pad_int * ['']
            try:
                sheet_list.insert(sub_int, strip_lst)
            except IndexError:
                sheet_list.insert(-1, strip_lst)
        elif line_str == 'c':
            col_size = len(sheet_list)
            pad_int = col_size - len(strip_lst)
            if pad_int < 0:
                raise InsertException
            strip_lst = strip_lst + pad_int * ['']
            for i in range(len(sheet_list)):
                try:
                    sheet_list[i].insert(sub_int, strip_lst[i])
                except IndexError:
                    sheet_list[i].insert(-1, strip_lst[i])
        else:
            raise CommandException
    except InsertException:
        print('more values passed in than spreadsheet size')
        
def parse_cmd(cmd_str,sheet_list):
    '''Modifies the csv reader object "file_Reader", using cmd_str
    accordingly.'''
    cmd_lst = cmd_str.split(' ')
    try:
        if cmd_lst[0] == 'c':
            row = int(cmd_lst[1])
            col = int(cmd_lst[2])
            
            change((row,col),sheet_list)
        elif cmd_lst[0] == 'd':
            sub_int = int(cmd_lst[2])
            # delete(line,sub,spread_sheet)
            delete(cmd_lst[1],sub_int,sheet_list)
        elif cmd_lst[0] == 'i':
            sub_int = int(cmd_lst[2])
            # insert(line,sub,spread_sheet)
            insert(cmd_lst[1],sub_int,sheet_list)
        else:
            raise CommandException
    except IndexError:
        print('one or more missing arguments in command')
    except ValueError:
        print('wrong argument type!')
    except CommandException:
        print('')

def main():
    file_pointer = open_file()
    file_Reader = csv.reader(file_pointer)
    sheet_list = [row for row in file_Reader]
    help_str = """Responses are:
        'd c [column number]' to delete a column
        'd r [row number]' to delete a row
        'i c [column number]' to insert a column
        'i r [row number]' to insert a row
        'c [row number] [column number]' to insert a value in a cell
        'w' to write data to a .csv file
        'q' to quit """
    
    while True:
        display(sheet_list)
        print()
        print(help_str)
        cmd_str = input('\n\nCommand:(type \'h\' for help) ')
        if cmd_str == 'q':
            break
        elif cmd_str == 'h':
            print(help_str)
        elif cmd_str == 'w':
            write(sheet_list)
        else:
            parse_cmd(cmd_str,sheet_list)

if __name__ =="__main__":
    main()