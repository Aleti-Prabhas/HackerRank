
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min=scores[0]
    max=scores[0]
    m=0
    n=0
    l=[]
    for i in range (1,len(scores)):
        if scores[i]<min :
            n=n+1
            min=scores[i]
        elif scores[i]>max :
            m=m+1
            max=scores[i]
    l.append(m)
    l.append(n)
    return l
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
