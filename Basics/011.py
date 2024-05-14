#011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
numb=int(input('Please enter a number over 100 denoted as A1'))
numb_2=int(input('Please enter a number under 10 denoted as A2'))
time=numb//numb_2
print('A2 is',time, 'times A1' )