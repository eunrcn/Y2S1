#include <stdio.h>

int main() {
  int *p;  // Pointer to an int
  int **q; // Pointer to a pointer to an int.
  int x = 5, y = 6;

  p = &x;
  q = &p;

  printf("Initial Values:\n");
  printf("x = %d, y = %d, *p = %d, **q = %d\n", x, y, *p, **q);

  p++;
  printf("After p++:\n");
  printf("x = %d, y = %d, *p = %d, **q = %d\n", x, y, *p, **q);

  (*p)--;
  printf("After (*p)--:\n");
  printf("x = %d, y = %d, *p = %d, **q = %d\n", x, y, *p, **q);

  (**q)++;
  printf("After (**q)++:\n");
  printf("x = %d, y = %d, *p = %d, **q = %d\n", x, y, *p, **q);

  return 0;
}
