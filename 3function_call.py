#Function
#for example : if function take three input(argument) --> function does some work --> give One Output(Result)
#you have to find square(retun value) of 4(argument) : square(4) --> go inside function(4 ** 2) --> Output (16)

#defination: Function is a named, reusable block of code designed to perform a specific task. Function can take one, two or any number of argument but it give only one output.

def square(x):
    return x * x

def sub(a, b):
    return a - b
print(square(4))
print(sub(6, 4))
print(sub(5, 10))

print(square(3) + 4) # 9 + 4 = 13
print(sub(square(4), square(1+2))) #(square(4), square(3)) -> sub(16, 9) -> 7

print(square)
print(square(9))