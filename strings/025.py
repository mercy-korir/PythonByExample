'''025 Ask the user to enter their first name.
 If the length of their first name is under 
five characters, ask them to enter their surname and join them 
together (without a space) and display the name 
in upper case. If the length of the first name is five
or more characters, display their first name in 
lower case.'''

name=input('What is your first name?')
length=len(name)
if length < 5 :
    name2=input('What is your surname?')
    name=str.upper(name)
    name2=str.upper(name2)
    print(name+' '+name2)
else:
    name=name.lower()
    print(name)


