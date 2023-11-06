#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k,m=map(int, input().split(' '))
ma=[]
l=(list(map(int, input().split(' ')))[1:] for _ in range(k))
l=product(*l)
sn=[sum(map(lambda x: x*x, i))%m for i in l]
print(max(sn))