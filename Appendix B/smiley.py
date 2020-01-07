# draw a smiley face

from turtle import *
import time

speed(10)          # draw fast

penup()            # right side of face
forward(75)

pendown()          # draw an eye
right(90)
circle(25)
circle(10)

penup()            # left side of face
right(90)
forward(150)

pendown()          # draw an eye
right(90)
circle(25)
circle(10)

penup()            # center and down
right(90)
forward(75)
right(90)
forward(50)

pendown()          # draw a nose
left(45)
forward(40)
right(135)
forward(56.56)
right(135)
forward(40)

penup()            # center, down, then 100 left
right(135)
forward(50)
right(90)
forward(100)
left(90)           # need to face east

pendown()
circle(100, 180)   # smile

time.sleep(3)      # hold for 3 seconds so we can see