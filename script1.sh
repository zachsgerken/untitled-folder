# Defining the interpreter
#!/bin/bash

# Asking the user to enter a value
echo "Please enter your name first:"

# Storing the user input value in a variable
read name

# Checking if the name the user entered is equal to our required name
if [ "$name" = "Zach" ]; then

# If it equals the required name, the following line will be displayed"
	echo "Welcome Zach! Here is the secret: THM_Script"

# Defining the sentence to be displayed if the condition fails.
else
	echo "Sorry! You are not authorized to access the secret."
fi

