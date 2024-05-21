'''043 
Ask which direction the user wants to count (up or down). If they select up, then ask 
them for the top number and then count from 1 to that number. If they select down, ask 
them to enter a number below 20 and then count down from 20 to that number. If they 
entered something other than up or down, display the message “I don’t understand”.'''
user=input('Which direction do you want to count? Up or down?, u/d')
user=str.lower(user)
if user=='u':
  top_n=int(input('Please input the top number'))
  for i in range(1,top_n+1):                           
    print(i)
elif user=='d':
  no_2=int(input('Please input a number below 20'))
  if no_2<20:
    for i in range(20,no_2-1,-1):
      print(i)
  else:
    print('Invalid Entry')
else:
  print('I dont understand')


