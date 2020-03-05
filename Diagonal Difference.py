#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    j=0
    Sum1=0
    Sum2=0
    k=len(arr[0])-1
    for i in range(len(arr)):
        Sum1+=arr[i][j]
        j+=1

    for i in range(len(arr)):
        Sum2+=arr[i][k]
        k-=1
    
    diff=abs(Sum1-Sum2)
    return diff
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
