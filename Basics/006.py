#006 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user friendly format.
quiz1=int(input('How many slices of pizza did you start with?'))
quiz2=int(input('How many slices have you taken?'))
if quiz1>quiz2:
    print('The remaining pizza is', quiz1-quiz2)
else:
    print(" Error")
