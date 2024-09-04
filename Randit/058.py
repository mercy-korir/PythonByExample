'''058 
Make a maths quiz that asks five questions by randomly 
generating two whole numbers to make the question 
(e.g. [num1] + [num2]). Ask the user to enter the 
answer. If they get it right add a point to their score. At 
the end of the quiz, tell them how many they got correct 
out of five. '''
import random
score=0
for i in range(0,5):
    numb1=random.randint(1,100)
    numb2=random.randint(1,50)
    total=numb1+numb2
    print(numb1,'+',numb2,'=...')
    numb=(int(input('Please input the answer')))
    if numb==total:
        score= score + 1
        print('You scored', score, 'Out of 5')