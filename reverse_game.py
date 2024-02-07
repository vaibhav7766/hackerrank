#https://chat.openai.com/c/e45f7435-e1c0-448e-bdba-9a80c0ee8cc8
#!/bin/python3

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k>=(n-1)//2:
        print(2*(n-k-1))
    else:
        print(2*k+1)