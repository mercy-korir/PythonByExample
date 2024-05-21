'''049 
Create a variable called compnum and set the value 
to 50. Ask the user to enter a number. While their guess 
is not the same as the compnum value, tell them if 
their guess is too low or too high and ask them to have another guess. If they enter 
the same value as compnum, display the message “Well done, you 
took [count] attempts”.'''
compnum=50
count=1
user=int(input('Guess a number'))
while user != compnum:
    if user <compnum:
        print('Too low')
    elif:
        user> compnum
        print('Too high')
        count=count+1
    else:
        user = int(input('Guess a number'))
        print('well done you took',count,'attempts')


    