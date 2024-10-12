#009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
name=int(input('How many days did you spend your time in Nairobi?'))
Hours=name*24
Minutes= Hours*60
seconds=Minutes*60
print('You spent', Hours,'hours', Minutes,'minutes',seconds,'seconds', 'in Nairobi','.')