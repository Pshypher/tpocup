# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 13:22:28 2018

@author: Pshypher
"""
import pylab

values = [10,20,50,100,200,1000]
pie_labels = ['first','second','third','fourth','fifth','sixth']

# these are the default colors. You get these if you do not provide any
color_list = ('b','g','r','c','m','y','k','w')

pylab.pie(values, labels=pie_labels,colors=color_list)
pylab.title('Pie chart of 6 values')
pylab.show()