#021 Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.
name1=input('What is your first name?')
name2=input('What is your surname')
length=len(name1+name2)
print(name1,name2,length)