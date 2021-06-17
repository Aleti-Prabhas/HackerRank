from collections import Counter
import math
import os
import random
import re
import sys



def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum

n,m = map(int,input().split())
queries = [list(map(int,input().split())) for _ in range(m)]
print(arrayManipulation(n, queries))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
