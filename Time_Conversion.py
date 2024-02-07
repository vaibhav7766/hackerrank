#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

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
    flag = 1 if s[-2:] == "PM" else 0
    s = s[:-2]
    hh, mm, ss = map(int, s.split(":"))
    
    if flag == 1 and hh != 12:
        hh += 12
    elif flag == 0 and hh == 12:
        hh = 0
        
    return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)

if __name__ == '__main__':
    # Instead of reading from os.environ['OUTPUT_PATH'], we can directly print the result
    s = input("Enter the time in 12-hour format: ")
    result = timeConversion(s)
    print("Time in 24-hour format:", result)