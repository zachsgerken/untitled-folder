#!/bin/bash

# Ask the user for the remote host (IP or domain)
read -p "Enter the remote SSH host (e.g., user@hostname): " remote_host

# Start the SSH connection
ssh "$remote_host"
