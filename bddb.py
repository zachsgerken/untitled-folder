#Zach Gerken
#Chapter 4 Lab 2
#September 18 2022
import turtle
keep_going = 'y' 
while keep_going == 'y':  #to keep the loop going
    lines = int(input('Enter in the number of lines in the pyramid (1-10):'))
    turtle.clear() #clears previous pyramid
    if lines >= 11:  #invalid number entry
        print('Not a valid number')
        continue
    if lines <= 0:
        print('Not a valid number')
        continue
 
    for num in range(1, (lines + 1) * 10, 10):   #turtle loop with range
        turtle.forward(num)
        turtle.penup()
        turtle.goto(-num / 2, -num)
        turtle.pendown()

    #input for another pyramid
    keep_going = input('Do you wish to draw another pyramid (y or n)?')  


