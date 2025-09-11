# The Python type for storing true and false values is called bool.

print(True) # print: True
print(type(True)) # it print : <class 'bool'>
print(type("True")) # print: <class 'str'>

# comparison operator: compare two values (==, <=, >=, !=, <, >) <-- All are comparison operator
# ---------------------
# A boolean expression is an expression that evaluates to a boolean value. The equality operator, ==, 
# compares two values and produces a boolean value related to whether the two values are equal to one another.
print(5 == 6) # print: False
print(5 == 5) # print: True

# Logical Operator:
# -----------------
# and, or, not : these are logical operator (comapre value with left and right)
# and : both value be true then true or both value be false then false, one is True and one is false then result: false
# or : both value be true then true or both value be false then false, one is True and one is false then result:True
# not : False! = True , True! = False
#Example:
x = 5
print(x>0 and x < 10) # print: true (true and true = true)

n = 25
print(n%2 == 0 or n%3 == 0) # print: false (false or false = false)

#Operator precedence: parenthesis(), Exponent x**2, multiple or division, add or sub, comparsion, not/or

# Smart Evaluation
# example1:
answer = input('Continue?')
if answer == 'Y' or answer == 'y':
   print('Continuing!')

# example2:
total_weight = int(input('Enter total weight of luggage:'))
num_pieces = int(input('Number of pieces of luggage?'))

if total_weight / num_pieces > 50:
   print('Average weight is greater than 50 pounds -> $100 surcharge.')

print('Luggage check complete.')

# 'in' and 'not in' operator
# example
print('p' in 'apple') # True
print('ap' in 'apple') # True
print('pa' in 'apple') # False
print('' in 'apple') #False
print('x' not in 'apple') #True

# 'in' work on list 
print("a" in ["a", "b", "c", "d"]) #print: True
print(9 in [3, 2, 9, 10, 9.0]) #print: True
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing']) #print: False
print("a" in ["apple", "absolutely", "application", "nope"]) #print: false (here list value is treated as one character)
