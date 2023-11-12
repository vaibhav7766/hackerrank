#https://www.hackerrank.com/challenges/best-divisor/problem?isFullScreen=true

import sys
input = sys.stdin.readline

def get_divisors(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

def digit_sum(n):
    s = str(n)
    sn = sum(map(lambda x: int(x), s))
    return sn

def best(n):
    divisors = get_divisors(n)
    temp = 0
    max_sum = 0
    for i in divisors:
        sn = digit_sum(i)
        if max_sum < sn:
            max_sum = sn
            temp = i
    return temp

n = int(input())
print(best(n))