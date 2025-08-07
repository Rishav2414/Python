#Module: A module is a file containing Python definitions and statements intended for use in other Python programs. 
# There are many Python modules that come with Python as part of the standard library.

import random

# prob = random.random() # range between 0 and 1 always (floating point number)
# print(prob) 

# diceThrow = random.randrange(1,10) # will include numbers from 1-9
# print(diceThrow) #random is a module and randrange is the function
# OR

#if you dont want to write random then you can follow below step
from random import randrange, random #here you defined then not to use random.randrange(1,10)
prob = random()
print(prob)

diceThrow = randrange(1, 10)
print(diceThrow)
