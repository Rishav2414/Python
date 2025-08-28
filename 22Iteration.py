#Iteration: A basic building block of all programs is to be able to repeat some code over and over again

#For Loop:
#---------
# the for statement allows us to write programs that implement iteration
# syntax: for <loop variable name> in <item want to iterate>:

#Flow of Execution of the for Loop
# the interpreter always keeps track of which statement is about to be executed. 
# We call this the control flow, or the flow of execution of the program.

#Sequential : Control flow until now has been strictly top to bottom, one statement at a time. We call this type of control sequential.

#example:

for name in ["joe", "Amy", "Rishav", "Raj"]:
    print("Hi, "+name+" come and join the party, tonight!")
# output:
# Hi, joe come and join the party, tonight!
# Hi, Amy come and join the party, tonight!   
# Hi, Rishav come and join the party, tonight!
# Hi, Raj come and join the party, tonight!

# Strings and for loops
# Since a string is simply a sequence of characters, the for loop iterates over each character automatically.

for arc in "Go spot Go":
    print(arc)
# output:
# G
# o

# s
# p
# o
# t

# G
# o

a = "python for loop"
# for b in a:
    # print("hello") # 15 times hello will print

for b in a[3:9]:
    print("hello") #6 times hello

# Lists and for loops
# A list is a sequence of items, so the for loop iterates over each item in the list automatically.

fruits = ["apple", "banana", "Grapes", "pine-apple", "jack-fruit"]
for afruit in fruits:
    print(afruit) # all fruits print

#for loop using in turtle to print square.

import turtle
wn = turtle.Screen()
rishav = turtle.Turtle()

for a in [0,1,2,3]:
    rishav.forward(50)
    rishav.left(90)

#here will print colored square:
for acolor in ["red", "yellow", "blue", "green"]:
    rishav.color(acolor)
    rishav.forward(50)
    rishav.left(90)
wn.exitonclick()

# Using the range Function to Generate a Sequence to Iterate Over
print("This will execute first")
for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")
print("Now we are outside of the for loop!")