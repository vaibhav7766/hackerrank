//https://www.hackerrank.com/challenges/reverse-array-c/problem?isFullScreen=true
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i, temp;
    scanf("%d", &num);
    int p=0, q=num-1;
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
    while(p<=q){
        temp=*(arr+p);
        *(arr+p)=*(arr+q);
        *(arr+q)=temp;
        p++,q--;
    }

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
    free(arr);
}