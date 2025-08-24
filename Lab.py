import turtle

lines = int(input('Enter in the number of lines in the pyramid (1-10):'))

turtle.speed(0.5)

for num in range(1, 1 + lines):
    a = turtle.Turtle()      #instantiate a new turtle object called 'a'
    a.hideturtle()           #make the turtle invisible
    a.penup()                #don't draw when turtle moves
    a.goto(-100, -100)       #move the turtle to a location
    a.showturtle()           #make the turtle visible
    a.pendown()              #draw when the turtle moves
    a.goto(100, -100)#move the turtle to a new location
    a.hideturtle()
    a.penup()
    a.goto(-90, -90)       #move the turtle to a location
    a.showturtle()
    a.goto(90, -90)

turtle.textinput("Continue", "Press enter to continue.")
