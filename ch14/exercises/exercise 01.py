# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:12:38 2018

@author: Pshypher
"""

isbn_dict = {"Python for Everyone": "978-1-119-05655-3", 
             "Fundamentals of Python": "1-4239-0218-1"}

try:
    book_title = input("Book title: ")
    isbn_str = isbn_dict[book_title]
except KeyError:
    print("No such book in dictionary!")