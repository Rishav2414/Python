#Concatenation and Repetition

fruits = ["apple", "banana", "grape", "pine-apple"]

print([1,2] + [3,4]) #print: [1, 2, 3, 4]

print(fruits + [6,7,8,9]) #print: ['apple', 'banana', 'grape', 'pine-apple', 6, 7, 8, 9]

print([0] * 4) # it will print 4 times 0 : [0, 0, 0, 0] means 0 is 4 times

print([0, 1] * 4) # print : [0, 1, 0, 1, 0, 1, 0, 1]

print((fruits + [1]) * 4)