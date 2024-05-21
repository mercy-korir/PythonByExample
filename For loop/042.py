'''042 
Set a variable called total to 0. Ask the user to enter 
five numbers and after each input ask them if they 
want that number included. If they do, then add the 
number to the total. If they do not want it included, 
don’t add it to the total. After they have entered all five
numbers, display the total.'''
total=0
for i in range(0,5):
    number1=int(input('Please input a number:'))
    ans = input("Would yo like to include this number? (y/n):")
    ans = str.lower(ans)
    if ans == "y":
        total += number1
    elif ans == "n":
        total = total
    else:
        print("You've entered a wrong input, I guess you mean No")
    
print(f"The total is {total}")

ask1=input('Do you want it included?')

    