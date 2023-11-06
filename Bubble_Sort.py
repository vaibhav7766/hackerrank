#https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    numberofswaps=0

    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numberofswaps+=1
    print("Array is sorted in",numberofswaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])