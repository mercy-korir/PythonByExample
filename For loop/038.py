'''038 
Change program 037 to also ask for a number. Display their name (one letter at a time on 
each line) and repeat this for the number of times they entered.'''
name=input('What is your name?')
number=int(input('Kindly imput a number'))
for i in range(0,number) :
    print(name)

