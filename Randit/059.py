'''059 
Display five colours and ask the user to pick one. If they 
pick the same as the program has chosen, say “Well 
done”, otherwise display a witty answer which involves 
the correct colour, e.g. “I bet you are GREEN with envy” 
or “You are probably feeling BLUE right now”. Ask 
them to guess again; if they have still not got it right, 
keep giving them the same clue and ask the user to 
enter a colour until they guess it correctly. 
'''
import random
color=random.choice(['Red','Blue','Green','White','Yellow'])
tryagain=True
while tryagain==True:
    user=input( 'Choose one of the Colors, red,blue, green, white,yellow')
    user=user.lower()
    if color==user:
        print('well done')
    else:
        print('You areprobably feeling', color, 'right now')
   
      



