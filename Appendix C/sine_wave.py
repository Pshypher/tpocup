# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:20:06 2018

@author: Pshypher
"""

import math
import pylab
import numpy

# use numpy arange to get an array of float values.
step_float = 0.0174532951994329576923690768489
x_values = numpy.arange(0,math.pi*4,step_float)
y_values = [math.sin(x) for x in x_values]
pylab.plot(x_values,y_values)
pylab.xlabel('x values')
pylab.ylabel('sine of x')
pylab.title('Plot of sine from 0 to 4pi')
pylab.grid(True)
pylab.show()