'''034 
Display the following message: 
1) Square
2) Triangle
Enter a number:
If the user enters 1, then it should ask them for 
the length of one of its sides and display the 
area. If they select 2, it should ask for the base 
and height of the triangle and display the area. If 
they type in anything else, it should give them a 
suitable error message.'''
import math
print('1) square')
print('2) Triangle ')
number=float(input('Enter a number:'))
if number==1:
    length=float(input('Please input the legth of one of its sides '))
    area=length*length
    print(area)
elif number==2:
    base=float(input('Please input the base of the triangle'))
    height=float(input('Please input the height of the triangle'))
    area=0.5*base*height
    print(area)
else:
    print('Error')
