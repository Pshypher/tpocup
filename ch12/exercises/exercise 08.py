# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:18:24 2018

@author: Pshypher
"""

def is_valid_path(path_str:str):
    """Checks if the path to a file is valid. Returns a boolean."""
    try:
        open(path_str, 'r')
        found = True
    except IOError:
        found = False
        
    return found

def read_file(path_str:str)->str:
    """Reads the contents of the file in the path_str argument.
        Returns a string."""
    file_pointer = open(path_str, 'r')
    file_contents = ''
    for line in file_pointer:
        file_contents += line
        
    return file_contents

class TextDocument(object):
    
    def __init(self, path_str:str):
        """Constructor of the TextDocument class, takes in a file path, 
            validates the path and opens the file."""
        if is_valid_path(path_str):
            self.__file_path = path_str
            self.__file_content = read_file(path_str)
        else:
            print('***file {:s} not found.***'.format(path_str))
            
    def __add__(self, param_TextDocument):
        """Concatenates the content of two files and creates a new text 
            file."""
        path_str = '{}_and_{}.txt'.format(self.__file_path, 
                    param_TextDocument.__file_path)
        concatenated_files_obj = open(path_str, 'w')
        print(self.__file_content + param_TextDocument.__file_content, 
              file=concatenated_files_obj, end='')
        concatenated_files_obj.close()
        return TextDocument(path_str)
    
    def __str__(self):
        """String representation of an instance of the TextDocument class."""
        return "{:s} file\nContent\n{:s}".format(self.__file_path, 
                self.__file_content)
        