# [C lecture 7](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)

### File I/O
 - Reading and writing to files is often called "I/O"
 - All I/O functions are declared in stdio.h

### Streaming I/O
 - (what it means)C and the kernel provide several ways to think about I/O.
In this course, we will consider the "stream I/O" model.
 - Stream I/O imagines I/O against a file as a "stream" of
"data" (characters or bytes) flowing between the program
and the file itself.
 - A stream can connect to any file (or file-like thing - such as
the special stdout, stdin, stderr streams for
handling user input/ output, which connect to the
terminal).

### Opening a File - fopen

``` c
FILE * fopen(char filename[], char mode[]);
```
