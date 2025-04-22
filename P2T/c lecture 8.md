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
