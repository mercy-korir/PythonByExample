'''039 
Ask the user to enter a number between 1 
and 12 and then display the times table for 
that number.'''
number=int(input('Please input a number between 1 and 12'))
for i in range(0,12):
    ans=i*number
    print(i,'X', number,'=',ans)
