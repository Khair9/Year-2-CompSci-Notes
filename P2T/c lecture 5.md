# [C lecture 5](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)

### Addresses
(Almost) all data is stored in a computer's memory, indexed by a unique number ("address") for each location.

### Pointer types
<img width="500" alt="image" src="https://github.com/user-attachments/assets/25c5e7de-7f55-4568-aa62-f66f5aa4e5e4" />
<Br>
int *p = NULL; //this pointer is set to point "nowhere!
<Br>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/4b44488f-c17e-43ef-990b-3706d4905803" />

### Pointers to stucts

``` c
struct mystruct *ptr; //given some struct with x,y elements

(*ptr).x  = 6.0; //set the value of the x element
printf("%f", (*ptr).y); //print the value of the y element
```
To print a pointer's value (the number of the address it points to), you can use the %p format specifier. This also works for addresses via &.
so:

``` c
double b = 7.0L;
double *p_to_b = &b;

printf("The value %f is stored in the location %p\n", *p_to_b, p_to_b);
//or, equivalently
printf("The value %f is stored in the location %p\n", b, &b);
```

### example
version that doesn't double the variable b
```c
#include <stdio.h>

void doublethis(int a) {
	a *= 2;
}

int main(void) {
	int b = 1;
	doublethis(b);
	printf("%d\n", b);

	return 0;
}
```
version that does double variable b
``` c
#include <stdio.h>

void doublethis(int *a) {
	*a *= 2;
}

int main(void) {
	int b = 1;
	doublethis(&b);
	printf("%d\n", b);

	return 0;
}
```
### segementation

Trying to access memory that your program does not "own" will result in the kernel forcibly killing your program.
This is a "segmentation fault" (from the model that memory is divided into "segments", owned by different processes).
### Functions, arrays, and pointers

 - When you pass an array to a function, the function does not copy the contents of the array to a new array inside the function.
 - Instead, it just copies the address that the array starts at ...  
 - We say that the array "decays" to a pointer
 - This means that 
if you pass an array to a function, it will be modified by anything inside the function.
The inside of the function has no way to know how "big" the array is.
    sizeof() will instead return the size of a pointer!





