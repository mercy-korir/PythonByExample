'''055 
Randomly choose a number between 1 and 5. Ask the user to pick a 
number. If they guess correctly, display the message “Well done”, 
otherwise tell them if they are too high or too low and ask them to pick a 
second number. If they guess correctly on their second guess, display 
“Correct”, otherwise display “You lose”'''
import random
numb=random.randint(1,5)
numb1=int(input('Choose a number between 1 and 5'))
if numb==numb1:
    print('well done')
elif numb1<numb:
    print('Too low')
    numb2=int(input('Choose a second number'))
    if numb2==numb:
        print('Correct')
    else:
        print('You loose')
else:
    print('Too high')
    numb2=int(input('Choose a second number'))
    if numb2==numb:
        print('Correct')
    else:
        print('You loose')