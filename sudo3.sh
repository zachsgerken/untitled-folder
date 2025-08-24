#!/bin/bash

#send text to sudo.sh and sudo2.sh
echo 'cp sudo.sh sudo3.sh' >> sudo.sh
echo 'cp sudo.sh sudo3.sh' >> sudo2.sh

#show contents of all shell scripts
cat sudo.sh
cat sudo1.sh
cat sudo2.sh
cat sudo3.sh

#create sudo1.sh file and give it read write execute permissions
touch sudo1.sh
chmod 777 sudo1.sh

#copy sudo.sh to sudo3.sh (once!)
cp sudo.sh sudo3.sh

#Your current Bash script has some ordering and logic issues. Here's a breakdown of what it's doing and what might go wrong:
#Issues:

#Appending to sudo.sh and sudo2.sh before sudo.sh or sudo2.sh even exists — if they don’t exist, they'll be created with just that one line.

#cat runs before creating sudo1.sh or copying to sudo3.sh, so the output might not show what you expect.

#sudo3.sh gets created twice — once via the echo commands (appended), and again with a direct copy at the end.

#sudo1.sh is touched and chmod'd after it’s already been displayed with cat, which means it will show as empty.

#Suggested Improved Version

#If your goal is to:

    #Append cp sudo.sh sudo3.sh to sudo.sh and sudo2.sh

    #Create sudo1.sh and give it permissions

    #Copy sudo.sh to sudo3.sh once

    #Then show all contents afterward

#Then this script is more logically sound:

#!/bin/bash

# Create sudo1.sh file and give it read, write, execute permissions
#touch sudo1.sh
#chmod 777 sudo1.sh

# Append command to sudo.sh and sudo2.sh
#echo 'cp sudo.sh sudo3.sh' >> sudo.sh
#echo 'cp sudo.sh sudo3.sh' >> sudo2.sh

# Copy sudo.sh to sudo3.sh (once)
#cp sudo.sh sudo3.sh

# Show contents of all shell scripts
#echo -e "\n--- sudo.sh ---"
#cat sudo.sh

#echo -e "\n--- sudo1.sh ---"
#cat sudo1.sh

#echo -e "\n--- sudo2.sh ---"
#cat sudo2.sh

#echo -e "\n--- sudo3.sh ---"
#cat sudo3.sh

cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
cp sudo.sh sudo3.sh
