#013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.
numb1=int(input('Please input a number less than 20'))
if numb1>20:
    print('Too high')
else:
    print('Thank you')
