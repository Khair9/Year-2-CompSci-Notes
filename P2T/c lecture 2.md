# [c lecture 2](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)

### printf conversion
<img width="539" alt="image" src="https://github.com/user-attachments/assets/4264eb74-6e3c-4915-ba6d-04c42e608167" />

### File Scope
 - The variable **a** has **file scope**
 - The variable **b** has **block scope**
```c
int a = 5;
int main(void) {
  // do some stuff
  {
    int b = 6;
    // do some more stuff
  }
  // do some more stuff
  return 0;
  }
```
### Branching
```c
if (test1) {
  some statements;
}
else if (test2) {
  more statements;
}
else {
  further statements;
}
```
