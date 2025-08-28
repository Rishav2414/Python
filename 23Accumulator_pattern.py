# Accumulator Pattern: The accumulator pattern in Python is a common programming construct used to process a sequence of data and build up a single, cumulative result. 
# This result is stored in a variable called an "accumulator".
# The anatomy of the accumulation pattern includes:
# initializing an “accumulator” variable to an initial value (such as 0 if accumulating a sum)

# iterating (e.g., traversing the items in a sequence)

# updating the accumulator variable on each iteration (i.e., when processing each item in the sequence)

nums = [1,2,3,4,5,6,7,8,9,10]
accum = 0 #accumulator varible initilize with 0
for a in nums:
    accum = accum + a
print(accum) # output = 55

#RANGE : sequence of items you have to print with iteration 

for i in range(5):
    print(i) #O/P:0,1,2,3,4

for i in range(1, 5): #it will print upto 5
    print(i) #O/P:1,2,3,4 

#skip items :
for i in range(1, 10, 2):
    print(i) #O/P:1,3,5,7,9


print(range(5)) #O/P: range(0, 5)

#if you want to print in list:
print(list(range(5))) #O/P: [0, 1, 2, 3, 4]

#Accumulator with range
#from above 1st example
accu = 0
for i in range(11): # or for i in range(1, 11)
    accu = accu + i
print(accu) # 55

#example: 
n = int(input("How many odd number would you like to add together: "))
number = 0
odd_num = 1
for i in range(n):
    number = number + odd_num
    odd_num = odd_num + 2
print("sum of odd number :", +number) 

#QUESTIONS:
#Create a list of numbers 0 through 40 and assign this list to the variable numbers. 
# Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

numbers = list(range(41))
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
sum1 = 0
for i in numbers:
    sum1 = sum1 + i
print(sum1) #820

#Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for _ in str1:
    numbs +=1
print(numbs) #90

s = "python"
for idx in range(len(s)):
   print(s[idx % 2])