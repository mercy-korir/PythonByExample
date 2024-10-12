#014 Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.
numb=int(input('Please input a number between 10 and 20'))
if numb>=10 and numb<=20:
    print('Thank you')
else:
    print('Incorrect answer')
    