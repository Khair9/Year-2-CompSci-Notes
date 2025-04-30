#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 50   // Macro definition

// --- Function definitions before main ---

// Greet the user
void greet(const char *name) {
    printf("Hello, %s!\n", name);
}

// Return sum of two integers
int add(int a, int b) {
    return a + b;
}

// Swap values using pointers
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

// --- Struct definition ---
struct Person {
    char name[MAX_NAME_LEN];
    int age;
};

int main() {
    // --- Variables ---
    int a = 5, b = 10;
    char name[MAX_NAME_LEN];

    // --- Input/Output ---
    printf("Enter your name: ");
    fgets(name, MAX_NAME_LEN, stdin);
    name[strcspn(name, "\n")] = '\0'; // Remove newline

    printf("Enter two integers:\n");
    scanf("%d %d", &a, &b);

    // --- Function call ---
    greet(name);
    printf("Sum of %d and %d is %d\n", a, b, add(a, b));

    // --- If-else ---
    if (a > b) {
        printf("%d is greater\n", a);
    } else if (a < b) {
        printf("%d is greater\n", b);
    } else {
        printf("They are equal\n");
    }

    // --- Switch ---
    switch (a) {
        case 1: printf("a is 1\n"); break;
        case 2: printf("a is 2\n"); break;
        default: printf("a is something else\n");
    }

    // --- For loop ---
    printf("For loop (0 to 4):\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // --- While loop ---
    int count = 0;
    printf("While loop (until 3):\n");
    while (count < 3) {
        printf("Count = %d\n", count++);
    }

    // --- Arrays ---
    int nums[] = {10, 20, 30};
    printf("Array elements:\n");
    for (int i = 0; i < 3; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

    // --- Pointers and swap function ---
    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After  swap: a = %d, b = %d\n", a, b);

    // --- Struct usage ---
    struct Person p1;
    strcpy(p1.name, name);
    p1.age = b;

    printf("Struct -> Name: %s, Age: %d\n", p1.name, p1.age);

    // --- File I/O ---
    FILE *fp = fopen("output.txt", "w");
    if (fp == NULL) {
        perror("File opening failed");
        return 1;
    }
    fprintf(fp, "Name: %s, Age: %d\n", p1.name, p1.age);
    fclose(fp);
    printf("Data written to file.\n");

    return 0;
}
