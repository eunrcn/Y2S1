#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int hexToDecimal(char[], size_t);
int hexVal(char);

int main(void) {
  // As a basic requirement, translate just the first
  // two-digit hex number. As an extra exercise translate
  // all digits that have been input.

  char hex[10];
  size_t len;

  printf("Enter up to 8 hexadecimal digits (e.g. 091A2C, etc): ");
  fgets(hex, 10, stdin);
  len = strlen(hex);

  /* End-of-Line Check
adding a null at the end of the line */
  if (hex[len - 1] == '\n') {
    len = len - 1;
    hex[len] = '\0';
  }

  printf("You entered: %s\n", hex);
  printf("The value in decimal is: %d\n", hexToDecimal(hex, len));

  return 0;
}

int hexVal(char hex) {
  switch (toupper(hex)) {
  case '0':
    return 0;
  case '1':
    return 1;
  case '2':
    return 2;
  case '3':
    return 3;
  case '4':
    return 4;
  case '5':
    return 5;
  case '6':
    return 6;
  case '7':
    return 7;
  case '8':
    return 8;
  case '9':
    return 9;
  case 'A':
    return 10;
  case 'B':
    return 11;
  case 'C':
    return 12;
  case 'D':
    return 13;
  case 'E':
    return 14;
  case 'F':
    return 15;
  }
  return 0;
}

// int hexVal(char hex) {
//     if (hex >= '0' && hex <= '9') {
//         return hex - '0';
//     }
//     if (hex >= 'A' && hex <= 'F') {
//         return hex - 'A' + 10;
//     }
//     return 0; // Default case
// }


int hexToDecimal(char hex[], size_t size) {
  int decimal = 0;
  int position = 0;

  for (int i = size - 1; i >= 0; i--) {
    int value = hexVal(hex[i]);
    decimal += value * pow(16, position);
    position++;
  }

  return decimal;
}

// Modularity: By passing the size as an argument, you decouple the function
// from its usage context.
// The function becomes more reusable and can be used with different arrays of varying sizes.

// Flexibility: You might need to use the same conversion logic for arrays of
// different sizes.
// By passing the size as an argument, you avoid the need to rewrite the conversion logic for each array size.

// Performance: Calculating the size of the array inside the function involves
// iterating through the array to count the elements. This adds unnecessary
// overhead, especially if you are calling the function multiple times with different arrays.

// #include <stdio.h>

// int main() {
//   size_t size = 42;
//   printf("Size: %zu\n", size);
//   return 0;
// }


//Can you give 2 ways of displaying the stored value and 
//address value of the first element of an array?