import os
#Julian C Meyer
# Jan 14, 2022
# Declare variables, print variables, print type of data, learn some operators 
# This symbol is for comments the computer will ignore
# Program is Average of 3 tests
# I want clear my terminal
os.system('cls')
#Declare and Assign values
test1=89
test2=78.5
test3=86
Flag=False
#to display things on the screen we use the funtion print()
# print(type(test1), type(test2), type(Flag))
#declar Sum to add tests symbofor addition is +
Sum = test1 + test2 + test3
#Average we will division....    /
Average=Sum/3

print (Average)

print ("The average of 3 tests is ", Average)
print("Test1=", test1)
print("Test2", test2)