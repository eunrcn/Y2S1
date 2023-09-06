#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define BUFLEN  1024

int is_palindrome(char *str, int end) {
    int start = 0;

    while(end > start) {
        if(tolower(str[start]) != tolower(str[end]))
            return 0;
        start++;
        end--;
    }

    return 1;
}

int main() {
    char buffer[BUFLEN];
    int len;

    printf("Enter string: ");
    fgets(buffer, BUFLEN, stdin);

    len = strlen(buffer);

    if(buffer[len-1] == '\n') {
        buffer[len-1] = '\0';
        len--;
    }

    if(is_palindrome(buffer, len-1))
        printf("YES!\n");
    else
        printf("NO!\n");
}
