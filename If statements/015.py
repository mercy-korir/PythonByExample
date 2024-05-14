#015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.
colour=input('What is your favorite colour')
if colour=='red' or colour=='Red' or colour=='RED':
    print('I like red too')
else:
    print('I dont like',colour, 'I prefer Red')