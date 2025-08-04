#data Type : Python has several built-in data types used to categorize and store different kinds of values. 
#example:
print(type("Hello, World!")) #<class 'str'>
print(type(17)) #<class 'int'>
print("hello World") #hello World
print(type(3.2)) #<class 'float'>

print(type("17")) #<class 'str'>
print(type("7.4")) #<class 'str'>

#strings <class 'str'>
print(type('This is called string'))
print(type("This is called string"))
print(type("""This is called string"""))
print(type('''This is called string'''))

#important note 
# print('Rishav's watch') # syntax error because quotaion start at R and ends at v.
print("Rishav's watch") #use "" while using 's in string

# print("She said "Hi"") # syntax error
print('She said " Hi "')

print('''"Oh no", she exclaimed, "Ben's bike is locked!"''') # "Oh no", she exclaimed, "Ben's bike is locked!"

print("""This massage will span
      several lines
      of the text""")

print(23, 543) # it will print seprate value 23 543
print(42, 17, 56, 34, 11, 4, 35, 32) #42 17 56 34 11 4 35 32
print(3.4, "Hello", 45) #3.4 Hello 45