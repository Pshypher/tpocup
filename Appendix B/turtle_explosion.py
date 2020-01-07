from turtle import *
import time

class NewTurtle(Turtle):
    def __init__(self, shape='classic', color='red'):
        ''' store boom color, call parent with the rest '''
        Turtle.__init__(self, shape=shape)
        self.boom_color = color
        
    def explode(self, x, y):
        ''' quick animation, draw expanding dots, then clear'''
        self.dot(5, self.boom_color)
        self.dot(20, self.boom_color)
        self.dot(50, self.boom_color)
        self.dot(50, 'white')       # clear the color
        self.write('    boOOOM!', font=("Arial", "14", "normal"))
        
t1 = NewTurtle(shape='turtle')
t1.onclick(t1.explode)
t1.forward(100)

time.sleep(4)

