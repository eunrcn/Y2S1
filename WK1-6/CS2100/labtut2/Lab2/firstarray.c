#include <stdio.h>

int main() {
  int array[] = {10, 20, 30, 40, 50};

  // Using array indexing
  printf("Stored value of the first element: %d\n", array[0]);
  printf("Address of the first element: %p\n", (void *)&array[0]);

  // Using pointer notation
  int *ptr = array; // Points to the first element of the array
  printf("Stored value of the first element: %d\n", *ptr);
  printf("Address of the first element: %p\n", (void *)ptr);

  return 0;
}