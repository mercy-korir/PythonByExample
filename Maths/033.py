'''033 
Ask the user to enter two numbers. 
Use whole number division to divide 
the first number by the second and 
also work out the remainder and 
display the answer in a user-friendly 
way (e.g. if they enter 7 and 2 display 
“7 divided by 2 is 3 with 1 
remaining”)'''
import math
number1=float(input('Please enter the first number'))
number2=float(input('Please enter the second number'))
number3=number1//number2
number4=number1%number2
print(number1,'divided by',number2,'is',number3,'with',number4,'remaining')