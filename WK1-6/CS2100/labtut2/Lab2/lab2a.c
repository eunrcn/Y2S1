#include <stdio.h>

void display(int);

int main() {
    int ageArray[] = { 2, 15, 4, 23 };
    display(ageArray[2]);

    // Calculate the number of elements in ageArray
    int numElements = sizeof(ageArray) / sizeof(ageArray[0]);

    // Print the element and the size of the array
    printf("Size of the array is %d\n", numElements);

    return 0;
}

void display(int age) {
    printf("%d\n", age);
}

// original output is 4
// What is the purpose of the operator sizeof? What datatype will sizeof
// always give “1” value for on all architectures?
// The sizeof operator provides the size of the given data type or
//     expression in terms of the number of bytes it occupies in memory.This is
//         extremely useful for allocating memory,
//     ensuring proper data alignment,
//     and writing code that works on different systems without hardcoding
//     specific
//             byte sizes
//                 .

//         The data type for which sizeof will always give a value
//             of 1 is the char data type
//                 .The char data type is defined to always occupy exactly one
//                     byte in memory on all architectures.Therefore,
//     sizeof(char) will always be 1 regardless of the system.

