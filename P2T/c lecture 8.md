# [c lecture 8](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)
### Pseudo Random Numbers
What we want are sequences which have statistical properties of a random sequence:
- each value is hard to predict from the ones before it (**uncorrelated**)
- the probability of any value is the same (**uniform**)
- an **advantage** of a PRNG is that it can be set by a seed to give the same sequence of outputs
  
### PRNGs in C

These functions are prototyped in stdlib.h, so you need to #include it to use them.

``` C
void srand(unsigned int seed);
```

(If not set with srand, the PRNG defaults to starting with seed = 0)

``` c
int rand(void);
```
Returns the next value in the current pseudorandom sequence. This value will be an unsigned int between 0 and RAND_MAX.
``` c
double zero_to_one(void) {
return rand()/ (double) RAND_MAX;
}
```
```time_t time(time_t *)``` returns the current time a
Generally, we don't care about getting the value via a
pointer, so we just call it as ```time(NULL)```

``` C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(void) {
srand(time(NULL));
//print 100 pseudo random
numbers in sequence
for(int i=0; i<100; i++) {
printf("%d\n", rand() );
}
return 0;
}
```

### Limitations of rand()
 - As srand() takes an unsigned int as a seed, there are only UINT_MAX (the largest unsigned int value) possible sequences that rand() can produce (one per seed).
 - The C Standard doesn't require rand() to have a particularly long sequence length, or be more than "adequately" uncorrelated.
 - In some versions of the library, rand() can have quite short repeat lengths, or fail some statistical tests.

### Pointers Arithmetic
 - What does it mean to "add one to a pointer"?
 - By analogy with arrays, adding one to a pointer moves it to the "next memory locationafter the value it points at"
 - This means that precisely where the pointer moves to depends on its base type -
moving 'one "char" over' moves less than moving 'one "double"', as doubles are
usually 8 times larger than a char in memory.

Usefulness: The document explains that while older C compilers benefited from using pointer movement for array loops to improve efficiency, this is generally not the case with modern compilers. The primary reason given is that using pointer arithmetic in this way can make the code harder to read and understand.   

However, it notes that pointer arithmetic is still useful in specific scenarios, such as when you need to access specific memory locations directly, given you know the exact memory size and structure.   

Example: The slides provide an example where a pointer ptr is used to assign values to an array. The *ptr++ = i; syntax is explained, where *ptr assigns the value of i to the current location pointed to by ptr, and then ptr++ increments the pointer to the next element in the array.   

### Memory Allocation

Allocation Methods: The lecture outlines two primary ways variables are allocated memory: static and automatic.   

Static allocation is for variables at the file scope or those marked as "static" within a block. Memory is allocated for these variables for the entire duration of the program's execution.   

Automatic allocation is for variables within a block of code. Memory is allocated when the block starts executing and is automatically released when the block finishes.   

Dynamic Allocation: The document discusses the necessity of dynamic allocation when a function needs to allocate memory (like for an array) and return it. This is not possible with automatic allocation because the memory is deallocated when the function ends.



