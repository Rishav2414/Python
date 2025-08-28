#Length:
# ------
# To find length of string, List and touples.

fruit = "banana"
print(len(fruit)) # print: 6

#print last item:
sz = len(fruit) # it will print 6
# last = fruit[sz] #shows error "IndexError: string index out of range"
#error because index is start from 0 and we have (sz value = 6) and here (last = fruit[sz]) is searching 
# for 6th item in fruit so it can find 6th item so reflect error (fruit having index size 5)

last = fruit[sz-1] # print : a
print(last)

# or also we can write:
last = fruit[len(fruit) - 1] #print: a
print(last)

#print middle of item
fruit = "grape"
midchar = fruit[len(fruit)//2]
print(midchar) # print: a

# list with len function
list = ["rishav", 27, "singh"]
print(len(list)) # print: 3

#for print length of item in a list
print(len(list[0]))