# Zach Gerken, Chapter 4 Lab 2, September 8 2022

import turtle
keep_going = 'y'
while keep_going == 'y':
    lines = int(input('Enter in the number of lines in the pyramid (1-10):'))
    for num in range(10, (lines + 1) * 10, 10):
        turtle.forward(num)
        turtle.penup()
        turtle.goto(-num / 2, -num)
        turtle.pendown()

    keep_going = input('Do you wish to draw another pyramid (y or n)?')
turtle.textinput("Continue", "Press enter to continue.")
