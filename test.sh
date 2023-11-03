#!/bin/bash

# Define the directory to list
dir_to_list="/bin"

# Use a for loop to iterate through the files in the directory
for command in "$dir_to_list"/*; do
  if [ -x "$command" ]; then
    # Check if the file is executable
    echo "Command: $(basename $command)"
  fi
done
