# draw squares, change the pen size and color
# just to show off

from turtle import *
import time

colormode(255)  # colors in range 0-255

def square(length, fill_tuple):
    ''' Draw a square, side length, color fill_tuple '''
    fillcolor(fill_tuple)
    begin_fill()
    for i in range(4):
        forward(length)
        right(90)
    end_fill()
    
# init values, fun to change
red = 100
green = 0
blue = 50
color_inc = 10
side_length = 50
pen_width = 1
pen_inc = 1
pen_limit = 5

speed(0)
for i in range(36):
    square(side_length, (red,green,blue))
    right(10)
    red = (red + color_inc) % 255   # range 0-254
    blue = (blue + color_inc) % 255
    green = (green + color_inc) % 255
    side_length += 3
    # range 1-pen_limit
    pen_width = ((pen_width + pen_inc) % pen_limit) + 1
    pensize(pen_width)
    
time.sleep(5)