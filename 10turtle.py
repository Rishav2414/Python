# Turtle: **turtle** is a Python module used for basic graphics and drawing
# Methods: 
#---------
# Forward()
# right()
# left()

# Attribute
#----------
# color()
# heading()
# position() 
# width()

# import turtle # allows us to use turtles library(it defines the module turtle which will allow you to create a Turtle object and draw with it)
# wn = turtle.Screen # creates a graphic window
# alex = turtle.Turtle() # create a turtle name alex(The first "turtle" (before the period) tells Python that we are referring to the turtle module, which is where the object "Turtle" is found.)
# alex.forward(150) # tell alex to move forward by 150 units
# alex.left(90) # turn by 90 degrees
# alex.forward(70) # complete second side of rectangle, tell alex to move forward by 70 units
# turtle.done() # This keeps the window open
# alex.salary = 50000
# print(alex.salary)

# make rectangle
# import turtle
# wn=turtle.Screen()
# alex=turtle.Turtle()
# alex.forward(200)
# alex.left(90)
# alex.forward(100)
# alex.left(90)
# alex.forward(200)
# alex.left(90)
# alex.forward(100)
# turtle.done()

import turtle

wn = turtle.Screen() #wn is instance
wn.bgcolor("lightgreen")        # set the window background color
 
tess = turtle.Turtle() #tess is an instance
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen
  
tess.forward(50)
tess.left(120)
tess.forward(50)  
wn.exitonclick()    # wait for a user click on the canvas