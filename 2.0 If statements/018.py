#018 Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.
numb1=int(input('Please enter a number'))
if numb1<10:
    print('Too low')
elif numb1>=10 and numb1<=20:
    print('Correct')
else:
    print('Too high')