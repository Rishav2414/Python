# Statement: A statement is an instruction that the Python interpreter can execute.
# Some other kinds of statements that you’ll see in future chapters are while statements, 
# for statements, if statements, and import statements.

#Expression: An expression is a combination of literals, variable names, operators, and calls to functions. 
#Expressions need to be evaluated. The result of evaluating an expression is a value or object.
# ex: x= 1 + 2 + 3 -> statement => "1+2+3" -> expression => and result x = 6 (6 is value)

print(1+2*(1+3)) #print: 9

# len() function: len function returns a count of how many characters are in the string, the string’s length.
print(len("Hello")) #print: 5

x = 3.14 # variable: x,  value: 3.14   
y = len("hello") # variable: y, value: 5
print(x) # print 3.14
print(y) # print 5

# literal
# e.g., “Hello” or 3.14

# variable name
# e.g., x or len

# operator expression
# <expression> operator-name <expression>

# function call expressions
# <expression>(<expressions separated by commas>)


print(2 * len("hello") + len("goodbye")) # len("hello"): 5, len("goodbye"): 7 => (2*5+7) = (10+7) = 17

a=1
b=3
def square(z):
    return z*z
def sub(a, b):
    return a-b

print(square(a+2)) # square(1+2) = square(3) = 9
print(square(b + square(a))) # square(3 + square(1)) = square(3 + 1) = square(4) = 16
print(sub(square(b), square(a))) # sub(9, 1) = 8

p=5
q=6

def add(x,y):
    return x+y

print(add(square(p), square(q))) 
# add(square(5),square(q)) 
# add(25, square(q))
# add(25, square(6))
# add(25, 36) = 61

# CALCULATE TIME
#----------------
total_sec = 7684
hours = total_sec // 3600
sec_still_remaining = total_sec % 3600
minutes = sec_still_remaining // 60
sec_still_remaining = sec_still_remaining % 60
second = sec_still_remaining
print("hours:",hours," minutes:",minutes," seconds:",second)