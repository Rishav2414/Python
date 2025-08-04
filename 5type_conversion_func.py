#Type Conversion Functions:
#--------------------------
# Python provides several built-in functions for explicit type conversion, also known as type casting. 
# These functions allow a programmer to convert data from one type to another when needed.

#integer:
#--------
print(3.14, int(3.14)) #here it will print integer i.e., 3
print(3.9999, int(3.9999)) #here it will print integer i.e., 3
print(3.0, int(3.0)) #here it will print integer i.e., 3
print(-3.99, int(-3.99)) #here it will print integer i.e., -3

print("2345", int("2345")) #string converted to int and print: 2345
print(17, int(17)) #string converted to int and print: 17
#print(int("23bottels")) #ValueError: invalid literal for int()

#Float:
#------
print(float("123.345")) #string to float i.e., 123.345
print(type(float("123.345"))) #<class 'float'>

#String:
#-------
print(str(18)) # int to string : 18 is string 
print(str(18.34)) # float to string : 18.34 is string
print(type(str(18.34))) #print <class 'str'>

val = 50 + 6
# print("The value is "+ val) #it will show errro(TypeError: must be str, not int)
print("The value is "+ str(val)) # the correct string value