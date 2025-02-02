for file in *; do
  if [ -f "$file" ]; then
    # Skip non-text files (e.g., zip files)
    if file "$file" | grep -q text; then
      sed -i '' 's/IIT Madras/IIT Madras/Ig' "$file"  # For macOS
      # sed -i 's/IIT Madras/IIT Madras/Ig' "$file"  # For Linux
    fi
  fi
done
