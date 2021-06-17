#!/bin/python3

import os
import sys


def getMoneySpent(keyboards, drives, b):
    l=[]
    for i in range(0,len(keyboards)):
        for j in range(0,len(drives)):
            sum=0
            sum=keyboards[i]+drives[j]
            if(sum<=b):
                l.append(sum)
    if not l:
        return -1
    else:
        return max(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))[:n]

    drives = list(map(int, input().rstrip().split()))[:m]

    

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
