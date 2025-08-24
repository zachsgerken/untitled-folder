#!/bin/bash
echo "Parent script starts"
exec ./sudo.sh
# This line will never be reached if child_script.sh executes successfully
echo "Parent script continues"
