# Repetition with a For Loop
# print("This will execute first")

# for _ in range(3):
#     print("this line will execute three times")
#     print("this line will also execute three times")

# print("This is the end of loop")

# # example2:
# # ---------
# import turtle

# wn = turtle.Screen()

# rishav = turtle.Turtle()

# distance = 50
# angle = 90
# for _ in range(10):
#     rishav.forward(distance)
#     rishav.right(angle)
#     distance += 10
#     angle -=3

# wn.exitonclick()

# more Methods in Turtle

import turtle
wn = turtle.Screen()

wn.bgcolor("orange")
rishav = turtle.Turtle()
rishav.color("blue")
rishav.shape("turtle") #it will show shape ex: turtle
#Every turtle can have its own shape. 
# The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle

dist = 5 #start by 5
rishav.up() # lift up the pen above the paper
for _ in range(50):
    rishav.stamp() # it will stamp the turtle shape
    rishav.forward(dist)
    rishav.right(24)
    dist += 2 #start by five and increase by 2 in each line
# You can speed up or slow down the turtle’s animation speed
rishav.speed(10)
wn.exitonclick()