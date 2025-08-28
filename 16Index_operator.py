# Index Operator:
s = "Python"
print(s[0]) #print: P
print(len(s)) #print: 6
print(s[len(s)-1]) #print: n (last index)

# P: 0, y:1, t:2, h:3, o:4, n:5

print(s[-4]) # print: t (it will count from last)
print(s[-1]) #print: n (last character)

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2]) # print: 87
print(numbers[9-8]) # print: 123
print(numbers[-2]) # print: 8398

s = "python rocks"
print(s[2] + s[-4]) # print: to

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[5]) # print: 3.14

#print last charcter 
lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."

output = lst[-1] # print: .
print(output)