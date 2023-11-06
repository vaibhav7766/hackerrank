#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
#!/bin/python3
import os
import sys

input=sys.stdin.readline
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def mult_of_5(grade):
    temp=grade
    while temp%5!=0:
        temp+=1
    return temp

def evaluate(grade):
    final_grade=0
    if grade<38:
        final_grade=grade
    else:
        mult=mult_of_5(grade)
        if mult-grade<3:
            final_grade=mult
        else:
            final_grade=grade
    return final_grade
    
def gradingStudents(grades):
    grades=list(map(evaluate,grades))
    return grades
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()