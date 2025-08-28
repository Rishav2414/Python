# String: 
# -------
# -> Strings can be defined as sequential collections of characters
# -> A string that contains no characters, often referred to as the empty string, is still considered to be a string.
# -> It is simply a sequence of zero characters and is represented by ‘’ or “”
#String imutable: cannot be change

n = "" # Empty String 
m = "Rishav" #sequence of character(12 character), start from index '0' and ends at index '5' 
p = 'M'
a = '5' # this is also string
print(type(a))
# print(type(a+5)) # this is error "can only concatenate str (not "int") to str" -> Runtime error
#if you want to add the number we have to type cast the string: 
print(int(a) + 5)

q = ''' # multiline string code with single 3 quotes or double 3 quotes
This is 
Multi line 
String code'''
print(n)
print(m)
print(p)
print(q)

b = "5 hundread"
# print(float(b) + 5) # could not convert string to float: '5 hundread'
print(b)

#concatenate existing string
c = "Rishav"
d = "Singh"
e = c +" "+d # print: Rishav Singh
print(e)

#Index the string
print(c[4]) # print: a

# print length of string
print(len(c))

# Slice operator : print string between two given index
x = c[2:6]
print(x) #shav

#count method: to count similar character in string 
y = c.count("s")
print (y) # Rishav : s is only one : output: 1

# Index operator: find index of character from string
print(c.index("i")) # print : 1

#Upper and Lower case
print(c.upper()) #print: RISHAV
print(c.lower()) #print: rishav

# strip : remove extra space from the string 
e = "      Rishav Singh       "
print(e.strip()) #print: Rishav Singh

#split : breaking up string 
print(e.split()) #print: ['Rishav', 'Singh']

print(e.split(" ")) # print : ['', '', '', '', '', '', 'Rishav', 'Singh', '', '', '', '', '', '', '']
print(e.split(' ')) # print : ['', '', '', '', '', '', 'Rishav', 'Singh', '', '', '', '', '', '', '']

# List:
# -----
# -> A list is a sequential collection of Python data values, where each value is identified by an index.
# -> The values that make up a list are called its elements.
# -> Lists are mutable: can be change
 
myList = ["Rishav", 27, 'Singh']
print(myList) #print: ['Rishav', 27, 'Singh']

myList1 = [] # Empty list
# below all three are diffrent
# myList1 = [100]
# i = 100 
# s = "100"

print(type(myList)) # print: <class 'list'>
print(myList1) # print: []
print(myList) # print: ['Rishav', 27, 'Singh']

#Append funtion: to add object in the list

myList.append("Kumar")
print(myList) # print: ['Rishav', 27, 'Singh', 'Kumar']

#another way to add item in list: Using concatenation operator
myList2 = ["gurugram", "Haryana"]
g = myList + myList2
print(g) # print : ['Rishav', 27, 'Singh', 'Kumar', 'gurugram', 'Haryana']

# Index oprator in list:
f = myList.index(g[1])
print(f)

#for replace value
myList[1] = 10
print(myList) # print: ['Rishav', 10, 'Singh', 'Kumar']

print(len(myList)) # print: 4

# Tuples:
# -------
# -> A tuple, like a list, is a sequence of items of any type.
# -> The representation is just like lists, except with parentheses () instead of square brackets [].
# ex: julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# tuples is that a tuple is immutable

myTuple = ("Rishav", 2, "Singh")
print(myTuple) #print : ('Rishav', 2, 'Singh')

# single item in tuple
myTuple1 = (100)
print(type(myTuple1)) # print: <class 'int'>

#for type Touple we have to define extra comman
myTuple2 = (100,)
print(type(myTuple2)) # print: <class 'tuple'>

#touple with zero item
myTuple3 = () # zero item
print(type(myTuple3)) #print : <class 'tuple'>
