# Program designed to draw the flag of the United States of America with a
# total of 13 stars on its union. The stars are drawn around a circle

# Unless stated otherwise, variables are of the type float

import turtle
import math
    

# Dimensions of US flag in pixels
# Height and width of the flag are in the ratio 1:1.9

scale_factor_str = input("Enter a positive real number for the scale factor of the flag: ")
scale_factor = float(scale_factor_str)

height_of_flag = 98.17627455 * scale_factor
width_of_flag = height_of_flag * 1.9
height_of_canton = 7/13 * height_of_flag
width_of_canton = 2/5 * width_of_flag
E = height_of_canton/6
G = width_of_canton/6
diameter_of_star = height_of_flag/13
width_of_stripe = height_of_flag/13
    
def draw_star():
    """Function draws the image of a star using the turtle.py graphics library
        on a blank canvas."""
    length_of_edge_btw_vertices = diameter_of_star / (2 + math.sin(math.pi/5) \
                                      / math.sin(2*math.pi/5))
    
    vertex = 0
    turtle.down()
    turtle.right(72)
    while vertex < 5:
        turtle.forward(length_of_edge_btw_vertices)
        turtle.left(72)
        turtle.forward(length_of_edge_btw_vertices)
        turtle.right(144)
        vertex = vertex + 1
    
    turtle.up()
    turtle.right(-72)
    
    
def draw_rectangle(width, height):
    """Draws a rectangle using turtle graphics on a blank canvas."""
    turtle.down()
    
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        
    turtle.up()
    
def draw_union(x_top_left, y_top_left):
    """Draws 13 white stars arranged in a circular fashion
        on a blue rectangle."""
        
    turtle.up()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    x_pos = 0 - x_top_left + width_of_canton/2 
    y_pos = y_top_left + height_of_canton/2-diameter_of_star/2
    turtle.goto(x_pos, y_pos)
    draw_rectangle(width_of_canton, height_of_canton)
    turtle.end_fill()

    
    diameter = 4*E + diameter_of_star
    radius = diameter/2
    stars = 0
    theta = 0
    
    while stars < 13:
        theta += 2*math.pi/13
        x = (x_pos + width_of_canton/2) + radius * math.cos(theta)
        y = radius * math.sin(theta)
        turtle.goto(x, y + y_top_left)
        turtle.fillcolor("white")
        turtle.begin_fill()
        draw_star()
        turtle.end_fill()
        
        stars += 1
    
def draw_flag():
    """Using turtle graphics draws the flag of the United States on a blank
        canvas."""

    x_top_left = width_of_flag
    y_top_left = height_of_flag
    
    draw_union(x_top_left, y_top_left)
    x = (width_of_canton/2 + width_of_canton) - x_top_left
    y = y_top_left + height_of_canton/2-diameter_of_star/2
    turtle.up()
    turtle.goto(x, y)
    
    width = width_of_flag - width_of_canton
    row = 1
    while row <= 13:
        if row > 7:
            x =  0 - x_top_left + width_of_canton/2
            width = width_of_flag
        if row%2:
            turtle.goto(x, y)
            turtle.fillcolor("red")
            turtle.begin_fill()
            draw_rectangle(width, width_of_stripe)
            turtle.end_fill()
        else:
            turtle.goto(x, y)
            turtle.fillcolor("white")
            turtle.begin_fill()
            draw_rectangle(width, width_of_stripe)
            turtle.end_fill()
        y -= width_of_stripe
        row = row + 1