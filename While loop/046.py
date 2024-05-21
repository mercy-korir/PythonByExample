'''046 
Ask the user to enter a number. Keep 
asking until they enter a value over 5 and 
then display the message “The last number you entered 
was a [number]” and stop the program'''
total=0
while total <=5:
    number=int(input('Please input a number '))
    print('The last number you entered was a',number)
    if total>=5:
        break