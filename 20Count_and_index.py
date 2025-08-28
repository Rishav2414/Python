#Count and Index
# Count: It requires that you provide one argument, which is what you would like to count.


a = "i have had an apple on my desk before"
print(a.count("e")) # print: 5
print(a.count("ha")) # print: 2

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4")) # print: 0 because here value("4") is a string and it is not present
print(z.count(4)) # print: 3 
print(z.count("a")) # print: 0 because the program is looking for items in the list that are just the letter “a”
print(z.count("electron")) # print : 2

# Inder: It will print the index value of the 1st character 
# For both strings and lists, index returns the leftmost index where the argument is found.

music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))