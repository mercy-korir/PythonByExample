'''057 
Update program 056so that it tells the user if they are too high or too low before they pick again.'''
import random
numb=random.randint(1,10)
correct= False
while correct== False:
    user=int(input('Choose a number between 1 and 10'))
    if numb==user:
        correct==True
    elif user<numb:
        print('Too low')
    else:
        print('Too high')
