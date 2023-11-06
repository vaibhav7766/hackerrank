#https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    a=int(s[:2])
    if "AM" in s:
        if a>12:
            a-=12
            return str(a)+s[2:len(s)-2]
        elif a==12:
            return "00"+s[2:len(s)-2]
        else:
            return s[:len(s)-2]
    else:
        if a==12:
            return s[:len(s)-2]
        else:
            a+=12
            return str(a)+s[2:len(s)-2]
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()