#Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
name1=input('what is your first name in lower case?:')
name2=input('What is your surname in lower case?:')
name1=name1.title()
name2=name2.title()
name=name1 +' '+ name2
print(name)
