#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
h,w=map(int,input().split(" "))
temp1=(w-3)//2
temp2=3
for i in range(1,(h//2)+1):
    print("-"*(temp1)+".|."*(2*i-1)+"-"*(temp1))
    temp1-=3
print("-"*((w-7)//2)+"WELCOME"+"-"*((w-7)//2))
for j in range(h//2,0,-1):
    print("-"*(temp2)+".|."*((2*j)-1)+"-"*(temp2))
    temp2+=3