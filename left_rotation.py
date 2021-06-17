import math
import os
import random
import re
import sys

n, d = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

d %= n
print(*(arr[d:] + arr[:d]))