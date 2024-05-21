'''048 
Ask for the name of somebody the user wants to invite 
to a party. After this, display the message “[name] has 
now been invited” and add 1 to the count. Then ask if 
they want to invite somebody else. Keep repeating this 
until they no longer want to invite anyone else to the 
party and then display how many people they have 
coming to the party.'''
count=0
name ='y'
while name=='y':
    name1=input('Who do you want to invite?')
    print(name1,'has been invited')
    count=count+1
    name3=input('Do you wish to add another person? y/n')
    print(count,'have been invited to a party')




