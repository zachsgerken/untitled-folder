#!/bin/bash

# Prompt for SSH host (e.g., user@hostname)
read -p "Enter the remote SSH host (e.g., user@hostname): " remote_host

# Optional: Exit if input is empty
if [[ -z "$remote_host" ]]; then
  echo "No host entered. Exiting."
  exit 1
fi

# Connect via SSH
ssh "$remote_host"

# Create the auto_ssh.sh file
output_file="auto_ssh.sh"

# Write SSH command to new script
cat <<EOF > "$output_file"
#!/bin/bash
ssh "$remote_host"
EOF

# Make the new script executable
chmod +x "$output_file"

echo "Created $output_file. Run './$output_file' to connect to $remote_host without prompting."
