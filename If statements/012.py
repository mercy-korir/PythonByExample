#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.
numb1=int(input('Please input the first number'))
numb2=int(input('Please input the secong number'))
if numb2>numb1:
    print(numb1,',',numb2)
else:
    print(numb2,',',numb1)