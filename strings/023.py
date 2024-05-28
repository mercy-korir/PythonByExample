#023 Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).
rhyme=input('Input the first line of your nursery rhyme')
l_rhyme=len(rhyme)
print('The nursery rhyme has',l_rhyme,'number of characters')
numb=int(input('Please input the starting number'))
numb2=int(input('Please input the ending number'))
display=rhyme[numb:numb2]
print(display)
