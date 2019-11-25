import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    arr1 = 0
    arr2 = 0

    for i in range(len(arr)):
        arr1 += arr[i][i]
        arr2 += arr[i][-1-i]
    
    return abs(arr1 - arr2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
