'''056 
Randomly pick a whole number between 1 
and 10. Ask the user to enter a number and 
keep entering numbers until they enter the 
number that was randomly picked. '''
import random
numb=random.randint(1,10)
correct= False
while correct== False:
    user=int(input('Choose a number between 1 and 10'))
    if numb==user:
        correct==True


