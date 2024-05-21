'''044 
Ask how many people the user wants to invite to a party. If they enter a number below 
10, ask for the names and after each name display “[name] has been invited”. If they 
enter a number which is 10 or higher, display the message “Too many people”.'''
user=int(input('How many users do you want to invite to a party?'))
if user<=10:
    for i in range(0,user):
        name =input('What is the name for the invited guest?')
        print(name,'has been invited')
else:
   print('Too many people')


