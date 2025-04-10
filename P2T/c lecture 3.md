# [C Lecture 3](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)
### Switch Case
```c
switch (expression) {
  case value1:
  some statements;
  break;
  case value2:
  more statements;
  default:
  further statements;
```
### While
```c
while (test) {
  //things to repeat here
}
```
```c
do {
  //some things to repeat here
} while (test) ;
```
### For
```c
for (init ; test ; iter )
{
  //some statements
}
```
 - A "for" statement contains three expressions, separated by semicolons.
 - The first expression - the init expression - is executed the first time we encounter the loop.
 - The idea is to use it to set up the initial conditions for the loop - setting a counter to zero, for example. E.g. for (i = 0; … ; …)
 - In C99 and later, we can additionally declare a variable in the init statement - this variable's scope will then be limited to that of the loop itself. E.g. for (int i = 0; … ; …)

#### For example:

```c
#include <stdio.h>
int main(void) {
  for(int i=0; i<4; i++) {
    printf("The value of i is: %d\n", i);
  }
  return 0;
}
```
 - Sometimes you need to "get out of a loop" early or skip to the end of an iteration. The break statement does the same thing in a loop as it does in a switch statement: ```
   ```break;```
- The ```continue``` statement does something similar - but skips to the next test for the loop (skipping any other instructions remaining in the block and then letting the loop structure itself decide if it needs to keep looping).
### Declaring an Array
```c
double a[5];
int b[4];
//a holds 5 doubles
//b holds 4 ints
```
### Initialising an Array
• We can give all of the elements of the array initial values, provided in a comma-separated list, surrounded by { }
• If we don't, the array could contain any values, until we set them somewhere.
• If we do specify an initialiser list, we can leave out the explicit size of the array between the [ ]s; the compiler will make an array exactly big enough to hold the list (and no larger).
```c
double myarr[5]; // uninitialised
int myarr2[4] = {0,-5,3,29}; // initialised
double q[] = { 0.1, 4e-5}; //q has size 2
```
- strcmp - compare two strings (asks ‘are they different?’) strcmp(string1, string2) 0 if strings are identical (i.e., ‘false’ if they are ‘not different’) Positive if string1 > string2, negative if string1 < string2 (alphabetically: D > A)
- strlen - length of a string (the number of characters before a '\0')
strlen("Hello") == 5;
- strcpy - copy a string from one char array or string literal into a char array. strcpy(destination, source); strcpy(destination, "This is a string");
- strcat - concatenate (join together) two strings, adding the second to the end of the first. (The array storing the string must be large enough to store the resulting
new string…). strcat(string1, string2); //result is string1string2

<img width="534" alt="image" src="https://github.com/user-attachments/assets/ee0085d6-f62f-4cd8-9af2-9c88a4aa23db" />

```c
#include <stdio.h>
#include <string.h>
int main(void) {
char line[100];
puts("Enter a line of text: ");
fgets(line, sizeof(line), stdin);
printf("The line was of length: %d\n", strlen(line));
return 0;
}
```
#### output
```
Enter a line of text:
One Two
The line was of length: 8
```

