# Program designed to draw the flag of the United States of America with a
# total of 13 stars on its union. The stars are drawn in rows

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
diameter_of_star = height_of_flag/7.5
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
    """Draws 13 white stars arranged in horizontal rows on a blue rectangle."""
    
    turtle.up()
    turtle.goto(x_top_left, y_top_left)
    
    turtle.fillcolor("blue")
    turtle.begin_fill()
    draw_rectangle(width_of_canton, height_of_canton)
    turtle.end_fill()
    
    turtle.up()
    
    vertical_dist = y_top_left + math.ceil(width_of_stripe - E)
    row = 1
    while row <= 5:
        if row % 2:
            horizontal_dist = x_top_left + G
            fill_odd_row(horizontal_dist, vertical_dist)
            vertical_dist -= E
        else:
            horizontal_dist = x_top_left + 2*G
            fill_even_row(horizontal_dist, vertical_dist)
            vertical_dist -= E
        row += 1
            
def fill_odd_row(horizontal_dist, vertical_dist):
    stars = 0
    while stars < 3:
        turtle.up()
        turtle.goto(horizontal_dist, vertical_dist)
        turtle.down()
        turtle.fillcolor("white")
        turtle.begin_fill()
        draw_star()
        turtle.end_fill()
        horizontal_dist += 2*G
        stars += 1
        
def fill_even_row(horizontal_dist, vertical_dist):
    stars = 0
    while stars < 2:
        turtle.up()
        turtle.goto(horizontal_dist, vertical_dist)
        turtle.down()
        turtle.begin_fill()
        draw_star()
        turtle.end_fill()
        horizontal_dist += 2*G
        stars += 1
    
def draw_flag():
    """Using turtle graphics draws the flag of the United States on a blank
        canvas."""
    
    x_top_left = 0 - width_of_flag
    y_top_left = height_of_flag
    draw_union(x_top_left, y_top_left)
    
    x = x_top_left + width_of_canton
    y = y_top_left
    turtle.up()
    turtle.goto(x, y)
    
    width = width_of_flag - width_of_canton
    row = 1
    while row <= 13:
        if row > 7:
            x = x_top_left
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
        