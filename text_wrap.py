#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap

def wrap(string, max_width):
    count=0
    s=''''''
    for i in string:
        if count==max_width-1:
            s=s+i
            s=s+"\n"
            count=0
        else:
            s=s+i
            count+=1
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)