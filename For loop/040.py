'''040  Ask for a number below 50 and then count down from 
50 to that number, making sure you show the number 
they entered in the output.'''
number=int(input('Please input a number below 50'))
for i in range(50,number-1,-1):
    print(i)

