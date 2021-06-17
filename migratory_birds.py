import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(n, arr):
    ids = [0] * 5
    maxN = 0
    id = 1
    for i in range(n):
        ids[arr[i] - 1] += 1
        if(ids[arr[i] - 1] > maxN):
            maxN = ids[arr[i] - 1]
            id = arr[i]
        elif(ids[arr[i] - 1] == maxN and arr[i] < id):
            id = arr[i]
    return id

       




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr_count,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
