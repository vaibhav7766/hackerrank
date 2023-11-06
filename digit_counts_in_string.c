//https://www.hackerrank.com/challenges/frequency-of-digits-1/problem?isFullScreen=true
#include <stdio.h>
#include <string.h>

int main() {
    int count[10] = {0};
    char s[1000];

    scanf("%s", s);

    for (int i = 0; s[i] != '\0'; i++) {
        char digit = s[i];
        if (digit >= '0' && digit <= '9') {
            int index = digit - '0';
            count[index]++;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ",count[i]);
    }

    return 0;
}