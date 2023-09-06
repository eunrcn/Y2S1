#include <stdio.h>

typedef unsigned char byte_t;

void printByte(byte_t);

// int main(void) {
//   byte_t a, b;

//   a = 5;
//   b = 22;
//   printf("a    = ");
//   printByte(a);
//   printf("\n");
//   printf("b    = ");
//   printByte(b);
//   printf("\n");
//   printf("a|b  = ");
//   printByte(a | b);
//   printf("\n");
//   return 0;
// }

void printByte(byte_t x) {
  printf("%c%c%c%c%c%c%c%c", (x & 0x80 ? '1' : '0'), (x & 0x40 ? '1' : '0'),
         (x & 0x20 ? '1' : '0'), (x & 0x10 ? '1' : '0'), (x & 0x08 ? '1' : '0'),
         (x & 0x04 ? '1' : '0'), (x & 0x02 ? '1' : '0'),
         (x & 0x01 ? '1' : '0'));
}

void swap(int *a, int *b) {
  if (a != b) { // Check if the addresses are not the same
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
  }
}

int main() {
  int x = 5;
  int y = 10;

  printf("Before swapping: x = %d, y = %d\n", x, y);

  swap(&x, &y); // Call the swap function

  printf("After swapping: x = %d, y = %d\n", x, y);

  return 0;
}