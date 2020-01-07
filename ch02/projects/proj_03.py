# Program written to draw colored turtle polygons
# unless stated otherwise, varables are assumed to be of type int

import time
from turtle import *

total_num_sides_str = input("Enter the number of sides of the polygon: ")
total_num_sides = int(total_num_sides_str)

color_str = input("Enter the color to fill the polygon: ")

# calculate interior angle in a regular polygon (num_sidess - 2) * 180 / num_sidess
angle_flt = (total_num_sides - 2) * 180 / total_num_sides
print(angle_flt)

fillcolor(color_str)
begin_fill()

num_sides = 0
while num_sides < total_num_sides:
    forward(100)
    left(180-angle_flt)
    num_sides = num_sides + 1
    
end_fill()

time.sleep(5)

