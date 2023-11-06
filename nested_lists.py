#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    n=int(input())
    l=[]
    sc=[]
    req=[]
    for _ in range(n):
        name = input()
        score = float(input())
        l.append([score,name])
        sc.append(score)
    d=list(set(sc))
    d.sort()
    x=d[1]
    for i in range(n):
        if l[i][0]==x:
            req.append(l[i][1])
    req.sort()
    for j in req:
        print(j)