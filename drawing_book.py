import os
import sys


def solve(n, p):
    pages_to_back = n-p
    turns_from_front = -(-(p-1) // 2)
    if n % 2 != 0:
        turns_from_back = -(-(pages_to_back - 1) // 2)
    else:
        turns_from_back = -(-(pages_to_back) // 2) 
    turns = [turns_from_front, turns_from_back]
    return min(turns)
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = solve(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
