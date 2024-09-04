'''054 Randomly choose either heads or tails (“h” or “t”). 
Ask the user to make their choice. If their choice is the same 
as the randomly selected value, display the message “You win”, 
otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.'''
import random
coin=random.choice(['h','t'])
guess=input('Kindly choose head(h) or tail(t')
if guess==coin:
    print('You win')
else:
    print('You loose')
if coin == 'h':
    print('The computer chose heads')
else:
    print('The computer chose tails')


