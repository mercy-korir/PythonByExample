'''050 
Ask the user to enter a number between 
10 and 20. If they enter a value under 10, 
display the message “Too low” and ask 
them to try again. If they enter a value 
above 20, display the message “Too high” 
and ask them to try again. Keep repeating 
this until they enter a value that is 
between 10 and 20 and then display the 
message “Thank you”.'''
numb=int(input('Input a number between 10 and 20'))
while numb<20 or numb>10:
    if numb>20:
        print('Too High')
    else:
        numb<10
        print('Too Low')
    numb2=int(input('Input a number between 10 and 20'))
    print('Thank you')


