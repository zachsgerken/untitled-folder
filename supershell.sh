#!/bin/bash

# Create shelltemplate.sh file and give it read, write, execute permissions
touch shelltemplate.sh
chmod 777 shelltemplate.sh

touch shelltemplatecp1.sh
chmod 777 shelltemplatecp1.sh

touch shelltemplatecp2.sh
chmod 777 shelltemplatecp2.sh

# Append command to sudo.sh and sudo2.sh
echo '#!/bin/bash' >> shelltemplatecp1.sh
echo '' >> shelltemplatecp1.sh
echo 'sudo apt update && sudo apt upgrade -y' >> shelltemplatecp1.sh

echo '#!/bin/bash' >> shelltemplatecp2.sh
echo '' >> shelltemplatecp2.sh
echo '.\shelltemplatecp1.sh' >> shelltemplatecp2.sh

# Copy sudo.sh to sudo3.sh (once)
cp sudo.sh sudo3.sh

# Show contents of all shell scripts
echo -e "\n--- sudo.sh ---"
cat sudo.sh

echo -e "\n--- sudo1.sh ---"
cat sudo1.sh

echo -e "\n--- sudo2.sh ---"
cat sudo2.sh

echo -e "\n--- sudo3.sh ---"
cat sudo3.sh

./sudo.sh
#Notes:

#Using echo -e "\n--- filename ---" helps make the output readable when viewing script contents.

#This script avoids creating or copying files prematurely.

#Permissions are applied before file use.

#Let me know if you want the script to check whether each file exists first or if you need to avoid overwriting anything.
