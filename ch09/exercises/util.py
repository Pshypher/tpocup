# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 02:06:24 2018

@author: Pshypher
"""

fp = open("duplicate.txt", 'r')
wfp = open('book_titles.txt', 'w')
for line in fp:
    line = line.strip()
    print(line, file=wfp)
    
fp.close()
wfp.close()