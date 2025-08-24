#Zach Gerken, Chapter 3 Lab 1, September 5 2022
#Numeric Workday Translator
print('Numeric Workday Translator')
print()
#int statement followed by input statement asking worker the day of the week
day_of_week = int(input('Enter in the numeric value ' +
                        'of the workday you wish to translate: '))
#if else statements dictating what will be displayed according to user input
if day_of_week == 0:
    print('The workday is a Weekend')
if day_of_week == 1:
    print('The workday is a Monday')
if day_of_week == 2:
    print('The workday is a Tuesday')
if day_of_week == 3:
    print('The workday is a Wednesday')
if day_of_week == 4:
    print('The workday is a Thursday')
if day_of_week == 5:
    print('The workday is a Friday')
if day_of_week == 6:    
    print('The workday is a Weekend')
if day_of_week == 7:    
    print('The workday is a Weekend')   
if day_of_week >= 8:
    print('Your entry is an invalid workday')
    

