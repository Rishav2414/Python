#Naming a Variable in for loop
#example
# for green in greens:  # green is singular noun and greens is plural noun
    # print(green)

#printing intermediate results
#example:
w = range(10)
sum = 0
for i in w:
    print(i) 
    sum+=i
    print(sum)
print(sum)

#output:
# 0 : i
# 0 : sum
# 1 : i
# 1 : sum and so on...

a = range(10)
sum1 = 0
print("****Before the for loop****")
for i in a:
    print("****A new loop iteration****")
    print("value of a: ", i)
    sum1+=i
    print("value of sum: ", sum1)
print("****End of for loop****")
print("final total: ", sum1)

#output:
# ****Before the for loop****
# ****A new loop iteration****
# value of a:  0
# value of sum:  0
# ****A new loop iteration****
# value of a:  1
# value of sum:  1
# ****A new loop iteration****
# value of a:  2
# value of sum:  3
# ****A new loop iteration****
# value of a:  3

#note:
t = ["chair", "table", "couch", "washer", "dryer"]
for w in t:
    print(type(t)) #it will print Type "list"
    print(type(w)) #it will print Type "string"

s = [9, "chair", "table", 10, "couch", "washer", "dryer"]
for x in s:
    print(type(s)) #it will print Type "list"
    print(type(x)) #it will print Type "int"