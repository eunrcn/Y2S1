#include <stdio.h>

int main() {
  char operator;

  while (1) {
    printf("Enter an operator (+, -, *, /) or 'q' to quit: ");
    scanf(" %c", &operator);

    if (operator== 'q') {
      printf("Bye!\n");
      break;
    } else if (operator== '+' || operator== '-' || operator== '*' || operator==
               '/') {
      float num1, num2, result;
      printf("Enter the first number: ");
      scanf("%f", &num1);
      printf("Enter the second number: ");
      scanf("%f", &num2);

      if (operator== '+') {
        result = num1 + num2;
      } else if (operator== '-') {
        result = num1 - num2;
      } else if (operator== '*') {
        result = num1 * num2;
      } else if (operator== '/') {
        if (num2 == 0) {
          printf("Cannot divide by zero!\n");
          continue;
        }
        result = num1 / num2;
      }

      printf("Result: %.2f\n", result);
    } else {
      printf("Unrecognized operation. Please enter +, -, *, /, or q.\n");
    }
  }

  return 0;
}


