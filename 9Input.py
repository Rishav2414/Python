#Input : get input from the user.
#------

n = input("please enter you name : ") #it will ask to enter name: Rishav/9999, it take number as string
print("hello,",n) # print: hello, Rishav

# for Example:
str_second = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_second)

hours = total_secs // 3600 #it will display hours -> 4000 // 3600 = 1 hours
remaining_sec = total_secs % 3600 # it will show remaining seconds -> 4000 % 3600 = 400 seconds

minutes = remaining_sec // 60 #it will display minutes -> 400 // 60 = 6 minutes
remaining_sec = remaining_sec % 60 # 400 % 60 = 40

seconds = remaining_sec # 40 seconds

print("Hours:",hours,"Minutes:",minutes,"Seconds:",seconds)

#important note
n = input("Please enter your age: ")
# user types in 18
print(type(n)) # print: String only