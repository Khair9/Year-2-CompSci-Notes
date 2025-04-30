# [P2T](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/README.md)
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
