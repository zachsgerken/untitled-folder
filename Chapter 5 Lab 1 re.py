#Zach Gerken, CYB-210-002, August 20th 2025

def main():
    # Get current temp from user
    current_temp = float(input('What is the current temperature? '))

    # Get unit type
    degree_type = input("Did you enter your temperature in (c)elsius or (f)ahrenheit? ").lower()

    # If the user entered Fahrenheit, call the Fahrenheit to Celsius conversion function
    if degree_type == 'f':
        fahrenheit_celsius(current_temp)

    # If the user entered Celsius, call the Celsius to Fahrenheit conversion function
    elif degree_type == 'c':
        celsius_fahrenheit(current_temp)
    # If they typed something else, show an error message
    else:
        print("Invalid choice. Please enter 'c' or 'f'.")

def fahrenheit_celsius(f_temp):
    # Perform the conversion
    c_conversion = (f_temp - 32) * 0.5556
    # Print out the converted value, formatted to 2 decimal places
    print(f"The current temperature is {c_conversion:.2f} Celsius")
    print(f"This temperature in Fahrenheit is {f_temp:.2f}")

def celsius_fahrenheit(c_temp):
    # Perform the conversion
    f_conversion = (c_temp * 1.8) + 32
    # Print out the converted value, formatted to 2 decimal places
    print(f"The current temperature is {f_conversion:.2f} Fahrenheit")
    print(f"This temperature in Celsius is {c_temp:.2f}")

main()

