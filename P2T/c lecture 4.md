# [c lecture 4](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/P2T/P2T.md)

### Using Scanf
 - Like printf, scanf takes a "format string" as its first argument. When it reads values from the user, it uses the format string as a pattern to try to convert the input into
values.
 - The remaining arguments to scanf are the variables you want to fill with values. These must be given with an & prefix, for reasons we will get to in the next lecture…
 - If the text scanf reads from the terminal cannot be matched to the given format string, scanf will stop reading immediately (potentially not filling some variables with values).
 - scanf returns a value equal to the number of variables it successfully filled...
``` c
float xcoord, ycoord;
puts("Enter two comma-separated floats: ");
scanf("%f,%f", &xcoord, &ycoord);
int i = scanf("%f,%f", &xcoord,
```
### Using Sscanf
sscanf is like scanf, except that the extra "s" indicates that, instead of parsing text from
the terminal, it will parse the text in a string we provide it with. 
``` c
char line[100];
puts("Enter two comma-separated integers: ");
fgets(line, sizeof(line), stdin);
sscanf(line, "%d,%d",&val1,&val2);
```

Note: You must distinguish between "float" (using %f) and "double" (using %lf) (printf uses %f for both)

| Approach               | Pros                                                                 | Cons                                                                 |
|------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| `scanf` (used directly) | - Fast parsing<br>- Simple to use                                    | - Stops parsing on unexpected input<br>- Hard to recover from errors |
| `fgets` + `sscanf`     | - More control over input<br>- Easier error recovery<br>- Always reads a full line | - More work to set up<br>- Requires additional parsing with `sscanf` |




