
import math
import os
import random
import re
import sys



x=int(input())
if(x%2==1):
    print("Weird")
elif(x<=20):
    if(x>=2 and x<=5):
        print("Not Weird")
    else:
        print("Weird")
elif(x%2==0):
    print("Not Weird")
