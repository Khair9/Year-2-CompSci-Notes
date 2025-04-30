# [P2T](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/README.md)
#### Tips for exam
 -  make sure you dont confuse C and bash
 -  remeber how declar shit in both laguages
#### Basic Bash Script
``` bash
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
```

[C lecture 1](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%201.md)

[C lecture 2](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%202.md)

[C lecture 3](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%203.md)

[C lecture 4](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%204.md)

[C lecture 5](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%205.md)

[C lecture 6](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%206.md)

[C lecture 7](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%207.md)

[C lecture 8](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/c%20lecture%208.md)

[Useful Linux info](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/useful_linux.md)


### Knowledge Gaps fro past papers
#### history 45!
This is valid and executes the 45th command in your shell history (as shown by the history command output).
#### Git branching
typical branches in git
```
main
│
├─── feature/awesome-feature
│
├─── bugfix/typo-fix
│
└─── hotfix/critical-patch
```
##### Hotfix Branches
Hotfixes are used to quickly patch production issues.
Created directly from main or master.
Example:

```bash
git checkout main
git pull
git checkout -b hotfix/fix-login-bug
```

After the fix, it’s merged into both main and develop (or other working branches), and a tag is often created for release.

You need to merge this back into the main branch so that everyone else gets it.

```bash
git checkout main
git merge hotfix/fix-login-bug
```

#### Commandline and standard inputs
##### Commandline inputs
- Passed when you run a script or command

- Accessed using special variables: ```$1, $2, ..., $@, $#```

- Used to parameterize behavior at the time of invocation
**code:**
``` bash
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
```
**Running:**
``` bash
./myscript.sh apple banana
```
**Output:**
``` sql
First argument: apple
Second argument: banana
```
##### Standard Input(stdin):
 - Input that comes from a **pipe, redirection, or user typing**
 - Read using commands like read, cat, or while loops
 - Useful when input is streamed or read interactively

```bash
#!/bin/bash
read fruit
echo "You entered: $fruit"
```
```bash
echo "mango" | ./myscript.sh
```

| Feature              | Command-Line Arguments      | Standard Input (stdin)         |
|----------------------|-----------------------------|--------------------------------|
| Provided via         | Arguments at script launch  | Piping, redirection, or typing |
| Accessed via         | `$1`, `$2`, `$@`, etc.      | `read`, `cat`, `stdin`         |
| Order sensitivity    | Positional ($1 = first)     | Not positional (streamed data) |
| Use case             | Configuration, options      | Data content, bulk input       |


