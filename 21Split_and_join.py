#Split and Join

# Split: The split method breaks a string into a list of words
# delimiter: used to specify which characters to use as word boundaries.

a = "The rain is spain..." 
print(a.split()) # print : ['The', 'rain', 'is', 'spain...']

print(a.split('ai')) # print : ['The r', 'n is sp', 'n...'] : it will split from "ai"

# Join: join the list with the glue between each of the elements
# "/".join(["leaders", "and", "best"]) => "leaders/and/best"

wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print(s) # print: red;blue;green
print(wds) # print: ['red', 'blue', 'green']

print("***".join(wds)) # print: red***blue***green
print("".join(wds)) # print: redbluegreen