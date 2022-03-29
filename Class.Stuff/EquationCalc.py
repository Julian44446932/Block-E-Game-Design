#Julian C. Meyer
#1/19/22
# Program to write and solve equation eitb 4 test values
#Other operators +-*/ ** expontent % modulus Format print
#             Format printing  escape character
# Program creating an equation, asking user input
#  and formatting the output
import os
os.system('cls')

#Declare variable:
var1=10
var2=2
var3=2.9
var4=5
#Calculate equation given
#** means exponent

result= (3*var1 - 2*(var2)**2/var3)/var4
# print(2**4)
print(result)
print("Var1= %5d"% var1")
print("Var2= %5d"% var2")
print("Var3= %5.8f"% var3")
print("Var4= %5d"% var4")
print("Result = %6.2f"% result, end=" ----")

print("\n The \" quotes\" tabs \t backslash \\")
