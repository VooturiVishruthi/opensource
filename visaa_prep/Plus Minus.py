#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    nc=0
    pc=0
    zc=0
    for i in arr:
        if i<0:
            nc+=1
        elif i>0:
            pc+=1
        elif i==0:
            zc+=1
    print(pc/len(arr))
    print(nc/len(arr))
    print(zc/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
