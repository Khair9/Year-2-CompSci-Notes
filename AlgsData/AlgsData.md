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

##### Merge Sort
**Step by step:**
###### Step 1 --> Divide
- keep splitting the array in half untill you have single element arrays
``` ruby
[38, 27, 43, 3, 9, 82, 10]

=> [38, 27, 43]        [3, 9, 82, 10]
=> [38] [27, 43]       [3, 9] [82, 10]
=>     [27] [43]       [3] [9] [82] [10]
```


##### i think most of the problem of understanding is coming from not understanding the merge part, heres the best explaination i could find
**psuedo code:**
```function merge(left, right):
    result = empty list      // This will store the merged sorted elements
    i = 0, j = 0              // i tracks index in left, j in right

    while i < length of left and j < length of right:
        if left[i] <= right[j]:      // Compare elements at current indexes
            append left[i] to result // If left is smaller, take it
            i = i + 1                // Move to next element in left
        else:
            append right[j] to result // Else, take from right
            j = j + 1                // Move to next element in right

    while i < length of left:        // Add remaining elements from left
        append left[i] to result
        i = i + 1

    while j < length of right:       // Add remaining elements from right
        append right[j] to result
        j = j + 1

    return result                    // Final merged sorted list
```
**python code**
``` python
def merge(left, right):
    result = []  # This list will contain the merged result
    i = j = 0    # Pointers to track positions in left and right

    # Compare elements from left and right, one at a time
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Add the smaller element to result
            i += 1                  # Move pointer in left
        else:
            result.append(right[j]) # Add the smaller element to result
            j += 1                  # Move pointer in right

    # If anything is left in left list, add it to result
    result.extend(left[i:])

    # If anything is left in right list, add it to result
    result.extend(right[j:])

    return result  # Return the fully merged and sorted list

```

##### !! Recurrence Equations
A recurrence equation describes the total time (or cost) of a recursive function.

It breaks the time into:
 - Work done to divide the problem (outside recursion)
 - Work done by recursive calls

###### 🧱 Example: Merge Sort
Let’s say we have T(n) as the time to sort n elements.

T(n) = 2T(n/2) + O(n)

###### 🔍 What does this mean?
2T(n/2): We split the array into two halves, and recursively sort each → two recursive calls

+ O(n): Then we merge the two sorted halves (takes linear time)

###### 🔽 Visual Tree of Work
Imagine the recursive calls as a tree, where each node represents a subproblem and the work at that level.


            T(n)
          /     \
     T(n/2)     T(n/2)
     /   \       /   \
T(n/4) T(n/4) T(n/4) T(n/4)
... and so on ...
Each level:

Has more subproblems, but

Each subproblem is smaller

Total work at each level is about O(n)

###### 🧠 Work by Level:
css
Copy
Edit
Level 0:      T(n)        → O(n)
Level 1:   2 x T(n/2)     → O(n)
Level 2:   4 x T(n/4)     → O(n)
...
Level log n: n x T(1)     → O(n)
🔚 There are about log n levels → so total work is O(n log n)

###### 🧮 Visual Formula Summary
bash
Copy
Edit
T(n) = aT(n/b) + f(n)
Where:

a: number of recursive calls

n/b: size of each subproblem

f(n): work done outside the recursion (like merging)

###### 🧠 For Merge Sort:
a = 2, b = 2, f(n) = n → "divide in half, two parts, merge takes linear time"
