# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 01:34:48 2018

@author: Pshypher
"""
import os

class FileTypeException(Exception):
    pass

class FilePathException(Exception):
    pass


def copy(in_file, out_file):
    '''Makes an exact copy of a file in_file.'''
    file_contents_lst = in_file.readlines()
    out_file.writelines(file_contents_lst)
    in_file.close()
    out_file.close()
    
def overwrite_add(source_file, dest_file_name):
    '''Overwrites or adds to the contents of dest_file_name.'''
    if os.path.exists(dest_file_name):
        res = input("Do you want to overwrite file?(y/n) ")
        while res not in 'NnYy':
            print('wrong response')
            res = input("Do you want to overwrite file?(y/n) ")
            if res in 'Yy':
                dest_file = open(dest_file_name,'w')
    else:
        dest_file = open(dest_file_name,'a+')
        
    copy(source_file, dest_file)
    
def main():
    # fetch name of text file from user
    source_file_path = input("Source file path: ")
    file_path, extension = os.path.splitext(source_file_path)
    if extension != '.txt':
        raise FileTypeException
        
    if os.path.exists(source_file_path):
        source_file = open(source_file_path, 'r')   # open file if it exists
        dest_file_path = input("File destination path: ")
        dir_path,dest_file_name = os.path.split(dest_file_path)
        
        if not dir_path:    # path not specified
            overwrite_add(source_file, dest_file_name)
        else:
            if not(os.path.exists(dir_path)):   # generate an error if path 
                raise FilePathException         # doesn't exist
            os.chdir(dir_path)
            overwrite_add(source_file, dest_file_name)
    else:
        print('File not found!')
        
if __name__ == "__main__":
    main()
        
    
            
        
    
    
