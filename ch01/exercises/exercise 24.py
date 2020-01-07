import turtle

# Draw a six pointed star

# Draws an equilateral triangle turned upside down
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

# moves the turtle to an absolute position without drawing a line
turtle.penup()
turtle.goto(0,-60)
turtle.pendown()

# Draws an equilateral triangle 
turtle.right(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
