# [Algorithms and Data](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/README.md)
### On paper lectures
 - lecutures 1-5
 - l6 on paper (Merge Sort)
 - l7 quicksort 
 - l8 heap sort done on paper
### github lecture notes
 - [l9 beyond comparision sort](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l9.md)
 - [l10 linked lists](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l10.md)
 - [l11 abstract data types](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l11.md)
 - [l12/13 Trees](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l12.md)
 - [l14 red&black trees, avl trees](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l14.md)
 - [l15 B-trees](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l15.md)
 - [l16 Hash tables](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l16.md)
 - [l17 Collision Resolution](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l17.md)
 - [l18 Matrix multiplication](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l18.md)
 - [l19 Advanced Design Techniques](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/AlgsData/l19.md)
### stuff i got wrong explained

##### Recurrsion Tree
A recursion tree is a visual tool used to represent how a recursive algorithm breaks down a problem into subproblems. It helps you:
 - Visualize each recursive call as a node in a tree.
 - Understand how the work is divided at each level.
 - Estimate the total work done (i.e., time complexity).
**visual representation:**
```
        fib(4)
       /      \
   fib(3)     fib(2)
   /   \       /   \
fib(2) fib(1) fib(1) fib(0)
 /   \
fib(1) fib(0)
```
##### Linear Recurrsion
Linear recursion is a type of recursion where a function makes at most one recursive call per execution. This means the problem is broken down into a single subproblem at each step, which simplifies things compared to multiple recursive calls (like in Fibonacci). Example factorial

#####
