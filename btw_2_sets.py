#!/bin/python3

import math
import os
import random
import re
import sys



def getTotalX(a, b):
    nmax,nmin,count = max(a),min(b),0
    for i in range(1,int(nmin/nmax)+1):
        if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b))==0:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
