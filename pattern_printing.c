//https://www.hackerrank.com/challenges/printing-pattern-2/problem?isFullScreen=true
#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int size = 2 * n - 1;
    int matrix[size][size];
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            int minDist = i < j ? i : j;
            minDist = minDist < size - i ? minDist : size - i - 1;
            minDist = minDist < size - j ? minDist : size - j - 1;
            matrix[i][j] = n - minDist;
        }
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
