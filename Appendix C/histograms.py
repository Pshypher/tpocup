# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:45:15 2018

@author: Pshypher
"""
import pylab
import random

x_values = [random.randint(0,1000) for x in range(10000)]

pylab.hist(x_values,100)
pylab.xlabel('bins of size 10')
pylab.ylabel('frequency')
pylab.title('plot of 10,000 random ints 0-1000, bins of size 10')
pylab.show()