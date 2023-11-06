//https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=true
#include <stdio.h>

int main() {
    int n,sum=0,l;
    scanf("%d",&n);
    int arr[n];
    for(int i=0; i<n; i++){
        scanf("%d",&arr[i]);
        sum+=arr[i];
    }
    printf("%d",sum);
    return 0;
}