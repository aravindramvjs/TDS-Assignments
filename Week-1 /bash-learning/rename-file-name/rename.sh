#!/bin/bash

# Function to replace digits with the next digit
# Special handling for 9 to wrap around to 0
replace_digits() {
    local filename="$1"
    local new_filename=""
    local i

    # Iterate through each character in the filename
    for ((i=0; i<${#filename}; i++)); do
        char="${filename:$i:1}"
        
        # Check if the character is a digit
        if [[ "$char" =~ [0-9] ]]; then
            # Handle 9 special case (wrap to 0)
            if [[ "$char" == "9" ]]; then
                new_filename+="0"
            else
                # Increment the digit
                new_filename+=$((char + 1))
            fi
        else
            # Non-digit characters remain unchanged
            new_filename+="$char"
        fi
    done

    echo "$new_filename"
}

# Function to recursively rename files and subdirectories
rename_contents() {
    local dir="$1"

    # First, rename all files and subdirectories within this directory
    find "$dir" -depth | while read -r path; do
        # Skip if it's the current or parent directory
        if [[ "$path" == "." || "$path" == ".." ]]; then
            continue
        fi

        # Get the directory and filename separately
        parent_dir=$(dirname "$path")
        filename=$(basename "$path")

        # Generate the new filename
        new_filename=$(replace_digits "$filename")

        # Only rename if the filename actually changes
        if [[ "$filename" != "$new_filename" ]]; then
            # Use full path to prevent conflicts
            mv -n "$path" "$parent_dir/$new_filename"
            echo "Renamed: $path -> $parent_dir/$new_filename"
        fi
    done
}

# Main processing function
process_directories() {
    local current_path=$(pwd)
    
    # First pass: rename directories
    for dir in */; do
        # Remove trailing slash
        dir=${dir%/}
        
        # Check if it's actually a directory
        if [[ -d "$dir" ]]; then
            # Generate new directory name
            new_dir=$(replace_digits "$dir")
            
            # Rename directory if name changes
            if [[ "$dir" != "$new_dir" ]]; then
                mv -n "$dir" "$new_dir"
                echo "Renamed directory: $dir -> $new_dir"
                # Update dir variable to new name for further processing
                dir="$new_dir"
            fi
        fi
    done

    # Second pass: process contents of renamed directories
    for dir in */; do
        # Remove trailing slash
        dir=${dir%/}
        
        # Check if it's actually a directory
        if [[ -d "$dir" ]]; then
            echo "Processing directory: $dir"
            rename_contents "$dir"
        fi
    done

    echo "Digit replacement rename process completed."
}

# Execute the main processing
process_directories