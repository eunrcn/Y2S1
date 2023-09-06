#include <stdio.h>
#define MAX 10


// instead of taking in int[], also can take in int *arr
// taking in pointer means expecting array

int readArray(int[], int);
void printArray(int[], int);
void reverseArray(int[], int);
void reverseArrayRecursive(int[], int, int);

// int main(void) {
//   int array[MAX], numElements;
//   numElements = readArray(array, MAX);
//   reverseArray(array, numElements);
//   printArray(array, numElements);
//   return 0;
// }

int main(void) {
  int array[MAX], numElements;
  numElements = readArray(array, MAX);
  reverseArrayRecursive(array, 0,
                        numElements - 1); // Using the recursive version
  printArray(array, numElements);
  return 0;
}

int readArray(int arr[], int limit) {
  int numElements = 0;
  int num;

  printf("Enter up to %d integers, terminating with a negative integer.\n",
         limit);

  while (numElements < limit) {
    scanf("%d", &num);
    if (num < 0) {
      break;
    }
    arr[numElements++] = num;
  }

  return numElements;
}

void reverseArray(int arr[], int size) {
  int left = 0;
  int right = size - 1;

  while (left < right) {
    // Swap arr[left] and arr[right]
    int temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;

    left++;
    right--;
  }
}

void reverseArrayRecursive(int arr[], int left, int right) {
  if (left >= right) {
    return;
  }

  // Swap arr[left] and arr[right]
  int temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;

  // Recur for the remaining elements
  reverseArrayRecursive(arr, left + 1, right - 1);
}

void printArray(int arr[], int size) {
  int i;
  for (i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}
