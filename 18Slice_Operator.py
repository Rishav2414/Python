#Slice Operator : Slicing uses a colon within the braces
# ex: S[(start):(end)], here include the start index but not include the last index
# diffrence between list ans slice : Both use square braces. Slicing uses a colon within the braces, while indexing does not

# List Slice
singers = "Arjit, Sonu and Lata"
print(singers[0:5]) # print: Arjit

print(singers[7:11]) # print: Sonu
print(singers[12:20]) # print: and Lata

fruits = "banana"
print(fruits[:4]) #print:  bana
print(fruits[4:]) # print: na

list = ["rishav", 27, "singh", 828111, 23.43]
print(list[1:3]) #print: [27, 'singh']

print(list[:4]) #print: ['rishav', 27, 'singh', 828111]
print(list[3:]) #print: [828111, 23.43]
print(list[:]) #print: ['rishav', 27, 'singh', 828111, 23.43] 

# more example of slice operator

# Tuple Slice : We can’t modify the elements of a tuple, 
# but we can make a variable reference a new tuple holding different information

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2]) #print: 1967
print(julia[2:6]) #print: 1967, "Duplicity", 2009, "Actress"

print(len(julia)) #print: 7

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:] 
print(julia) #print: "Julia", "Roberts", 1967, "Eat Pray Love", 2010, "Actress", "Atlanta, Georgia"

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))