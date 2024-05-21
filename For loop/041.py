'''041 
Ask the user to enter their 
name and a number. If the 
number is less than 10, then 
display their name that 
number of times; otherwise 
display the message “Too 
high” three times.'''
name=input('What is your name?')
number=int(input('Choose a number'))
if number< 10:
    for i in range(0,number):
      print(name)
else:
    for x in range(0,3):
       print('Too high')
