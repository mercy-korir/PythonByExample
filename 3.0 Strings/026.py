'''026 
Pig Latin takes the first consonant of a word, 
moves it to the end of the word and adds on an 
“ay”. If a word begins with a vowel you just add 
“way” to the end. For example, pig becomes igpay, 
banana becomes ananabay, and aadvark becomes 
aadvarkway. Create a program that will ask the 
user to enter a word and change it into Pig Latin. 
Make sure the new word is displayed in lower case.'''
word=input('Please input a word')
characters=len(word)
first=word[0] 
remaining=word[1:characters]
if first== 'a' or first== 'e' or first=='i' or first=='o' or first=='u' or first=='A' or first=='E' or first=='I' or first=='O' or first=='U':
    word2=remaining+first+'way'
    print(word2)
else:
    word3=remaining+first+'ay'
    print(word3)



