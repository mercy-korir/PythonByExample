'''051 
Using the song “10 green bottles”, display the lines “There are [num] green bottles 
hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle 
should accidentally fall”. Then ask the question “how many green bottles will be 
hanging on the wall?” If the user answers correctly, display the message “There will be 
[num] green bottles hanging on the wall”. If they answer incorrectly, display the 
message “No, try again” until they get it right. When the number of green bottles gets 
down to 0, display the message “There are no more green bottles hanging on the wall”.'''
bottles=10
while bottles>0:
    print('There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall')
    bottles=bottles-1
    user=int(input(' How many green bottles will be holding the wall'))
    if user==bottles:
        print ('There will be', bottles ,'green bottles hanging on the wall')
    else:
        while user!=bottles:
            print('no, Try again')
print('There are no more green bottles hangging on the wall')