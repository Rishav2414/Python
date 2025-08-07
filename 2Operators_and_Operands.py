#Operators and Operands

# 1. Addition Operator
print(100+200) #experation uses addtion operator 

# 2. Substraction Operator
print(200-100)

# 3. Multiplication Operator
print(100*200)

# 4. Division Operator
print(100/200) #by divide two integer here always we get floating point as a result.

#if you don't want floating value you can use Truncating division 
# 5. Truncating division: division where a fractional result is converted to an integer by rounding towards zero
#example

print(100//200) # use extra'/' print: 0

# 6. Modular Operator(remendir operator: gives reminder)
print(100%200) # print: 100

# 6. Exponential Operator: This operator raises the left operand (base) to the power of the right operand (exponent)
print(4**2) # 4 to the power of 2

#highest presedence of these operator:
#1. prenthesis ()
#2. exponential 4**2
#3. Multiplication & Division or Modulus (/ or // or %) 4*2 or 2*2
#4. Additon & substraction 4+2 or 4-2

#for example: if you want average of 10 and 20
print(10+20/2) #Division 1st then addition (20/2 = 10.0 -> 10 + 10.0 = 20.0)
#correct value
print((10+20)/2) # print: (30/2) = 15

#practice Question:
print(16 - 2 * 5 // 3 + 1) 
    #16 - 10 // 3 + 1
    #16 - 3 + 1
    #16 - 2
    #14

