# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 12:04:36 2018

@author: Pshypher
"""

import csv
workbook_file = open('Workbook1.csv', 'r')
workbook_reader = csv.reader(workbook_file)

for row in workbook_reader:
    print(row)
    
workbook_file.close()