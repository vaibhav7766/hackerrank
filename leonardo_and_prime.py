#https://www.hackerrank.com/challenges/leonardo-and-prime/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.

def primeCount(n):
    primes =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    count=0;prod=1
    while n>=prod:
        prod*=primes[count]
        count+=1
    return count-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
