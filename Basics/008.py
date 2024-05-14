#008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.
bill=int(input('What is the total price of the bill?'))
diners=int(input('How many diners were there?'))
bill2=bill/diners
print('Each person is supposed to pay','Ksh', bill2)