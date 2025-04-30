#!/bin/bash

# --- Variables ---
name="User"
age=0

# --- Command-line Arguments ---
echo "Script name: $0"
echo "First argument: $1"
echo "Total arguments: $#"

# --- User Input ---
read -p "Enter your name: " name
read -p "Enter your age: " age

# --- Conditional Logic ---
if [[ $age -ge 18 ]]; then
    echo "Welcome, $name. You are an adult."
elif [[ $age -gt 0 ]]; then
    echo "Hi $name, you're a minor."
else
    echo "Invalid age!"
fi

# --- Arrays ---
fruits=("apple" "banana" "cherry")
echo "Favorite fruit: ${fruits[1]}"
echo "All fruits: ${fruits[@]}"

# --- For Loop ---
echo "Listing fruits:"
for fruit in "${fruits[@]}"; do
    echo "- $fruit"
done

# --- While Loop ---
count=1
while [[ $count -le 3 ]]; do
    echo "Count: $count"
    ((count++))
done

# --- Function ---
greet_user() {
    echo "Hello, $1!"
}

greet_user "$name"

# --- Reading a File ---
file="sample.txt"
if [[ -f "$file" ]]; then
    echo "Reading contents of $file:"
    while IFS= read -r line; do
        echo "Line: $line"
    done < "$file"
else
    echo "$file does not exist."
fi

# --- Redirection ---
echo "This is a log entry." >> logfile.txt

# --- Exit Code ---
if [[ $age -lt 0 ]]; then
    echo "Negative age not allowed!"
    exit 1
else
    echo "Script finished successfully."
    exit 0
fi
