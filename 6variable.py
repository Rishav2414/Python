#Variables: Python variables are the reserved memory locations used to store values with in a Python Program.

#set variable
message = "Whats's up doc?"
a = 17
pi = 3.14156

#Reference variable
print(message)
print(a)
print(pi)

#reference diagram:
#------------------
#   variable                       Values
#------------------------------------------------
#   message      --->          Whats's up doc?
#   n            --->          17
#   pi           --->          3.14156

#what happen when we actually over write the variable value?
x = 5
print(x)

x=10
print(x)

#reference diagram 
#   variable   Values
#--------------------
#   x    --->     5 --> this is no longer exist
#   x    --->     10 --> new value should be change now and print 10

# 1. every variable name should be start with letter.
# 2. variable name always conatin letters and numbers.
# 3. Underscore we can use.
# 4. variable name should not be reserved keywords.
#example
x = 10 #valid
myvariable = 50 #valid
XYZ = 567 #valid

print(x, myvariable, XYZ)

#variable are case sensitive 
#example
xyz = "other variable"
print(xyz) #XYZ and xyz both are treated as diffrent variable values

# print(xYz) #it is not present : error refect

# 2x = 50 #not valid varible : syntax error

my_variable = 5.5 
print(my_variable)