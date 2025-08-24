

tempc = float(input('What is the current temperature?'))

tempt = input("Did you enter your temperature in (c)elsius or (f)ahrenheit?")


def cel_far(deg_f):
    deg_c =(tempc * 1.8) + 32
    print('The current temperature is', deg_c)
    print('Fahrenheit')
    print('This temperature in Celsius is', deg_c)

def far_cel(deg_c):
    deg_f =(tempc - 32) *.5556
    print('The current temperature is', deg_f)
    print('Celsius')
    print('This temperature in Fahrenheit is', deg_f)

    
cel_far(tempc)

far_cel(tempc)
