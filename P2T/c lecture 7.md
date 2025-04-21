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

- A FILE is a special structured type which represents the (state of the)
stream of data flowing to or from a file. Confusingly, it is the stream,
not the file itself.

### File Access modes

| File Mode | Intent (a bit like in Bash) | Does:                                 |
|-----------|-----------------------------|----------------------------------------|
| "r"       | <                           | Just read the file, from the start.    |
| "w"       | >                           | Overwrite the file, truncating it first. |
| "a"       | >>                          | Append stuff to the file, from the end. |


### Reading from a file (Text Stream I/O)
``` c
char * fgets(char string[], int len, FILE *file);
```

### Reading from a file
 - fscanf is like sscanf, scanf except the first argument is the FILE* to read from.
``` c
fgets(buf, sizeof(buf), myfile);
```
<Br>

-----------------

<Br>

``` c
fscanf(stdin, "%d is an integer", &myint)
```
is identical to
``` c
scanf("%d is an integer", &myint)
```
-----------------

### Writing to a file (text representation)

``` c
int fputs(char string[], FILE *file);
int fprintf(FILE *file, char format[], …);
```
---------------
### Streams and Buffers
• Strictly, writes to a stream are not immediately reflected in the file they
represent.
• (Physical media like hard disks, or even SSDs, take real time to write stuff.)
• Instead, the writes are "queued up" in a buffer of things needing to be
written.
• Periodically, the buffer is emptied, and its contents actually committed to
the file.
• We can force the program to wait until the buffer is empty with:
``` c
int fflush(FILE * fp);
```
---------------
### Closing a File
``` c
int fclose(FILE * fp);
```
 - fclose does a flush, and then removes the connection between fp
and the file it's attached to.
     - If successful, it returns 0.


### General I/O Functions
<img width="1263" alt="image" src="https://github.com/user-attachments/assets/204b9790-92bb-4c64-9a47-cfc3e4b9e4bd" />


### Stream I/O (Example)
``` c
#include <stdio.h>
int main(void){
FILE *fp = fopen("testfile.txt", "w");// open a file for writing
fprintf(fp, "Number %d, %f", 5, 5.0);
fputs("String 1\n", fp);
fflush(fp); //ensure written to file,Strictly unneeded as the fclose will also flush
fclose(fp); //close file
fp = fopen("testfile.txt", "r");//Reuse fp to open file for reading
int a;
double b;
char input_str[50];
if (2!=fscanf(fp, "Number %d, %lf", &a, &b)) {//%lf needed for reading double with fscanf
//Checking validity of input by checking how many variables fscanf parsed
puts("Invalid input!");
return 1;
} ;
fgets(input_str, sizeof(input_str), fp);
fclose(fp);
printf("Double in file was %f\n", b);
if (0 == strcmp("String 1\n", input_str) )
puts("strings match");
return 0;
}
```
