#!/bin/bash

# Get a list of all untracked files (respecting .gitignore)
# Exclude the script itself so it doesn't push itself mid-run
files=()
while IFS= read -r line; do
    if [[ "$line" != "auto_push.sh" ]]; then
        files+=("$line")
    fi
done < <(git ls-files --others --exclude-standard)

total=${#files[@]}

if [ "$total" -eq 0 ]; then
    echo "No untracked files found to commit."
    exit 0
fi

echo "Found $total untracked files. Starting individual commit & push..."
echo "---------------------------------------------------------------"

count=0
for file in "${files[@]}"; do
    ((count++))
    echo "[$count/$total] Processing: $file"
    
    git add "$file"
    git commit -m "Add $file" --quiet
    git push origin main --quiet
    
    if [ $? -eq 0 ]; then
        echo "[$count/$total] Successfully pushed: $file"
    else
        echo "[$count/$total] ERROR pushing: $file"
        exit 1
    fi
done

echo "---------------------------------------------------------------"
echo "Done! All $total files committed and pushed."
