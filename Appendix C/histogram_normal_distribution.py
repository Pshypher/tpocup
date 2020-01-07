# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:43:47 2018

@author: Pshypher
"""
import numpy
import pylab

ones_array = numpy.ones((10000))
ones_array = ones_array * 100
# standard distribtion, 10,000 elements, mu = 0, std = 1
sigma = numpy.random.standard_normal(10000)
sigma = sigma*15
# generate a standard distribution, mu = 100, std = 15
ones_array = ones_array + sigma
pylab.hist(ones_array,100)
pylab.show()
