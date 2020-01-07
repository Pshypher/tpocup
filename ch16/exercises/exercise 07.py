# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:23:41 2018

@author: Pshypher
"""
import turtle

def drawRuler(x,y,height=50,width=300):
    
    if height <= 1:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        return
        
    else:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(width)
        turtle.backward(width/2)
        verticalTick(height)
        drawRuler(x+width/2,y,height/2,width/2)
        turtle.backward(width/2)
        verticalTick(height)
        drawRuler(x,y,height/2,width/2)
        
    
def verticalTick(height):
    """Draws the vertical tick marks towards the right."""
    turtle.left(90)
    turtle.forward(height)
    turtle.backward(height)
    turtle.right(90)

