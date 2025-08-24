#!/bin/bash

echo "Enter your name:"
read name

# Print greeting with newline
echo -e "Hello, $name!\n"

# Append the name to list.txt
echo "$name" >> list.txt

# Inform the user
echo "Your name has been added to list.txt in this directory: $(pwd)"

