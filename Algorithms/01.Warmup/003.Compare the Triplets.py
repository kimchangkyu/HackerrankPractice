import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    a_count = 0
    b_count = 0

    for num in range(len(a)):
        if a[num] > b[num]:
            a_count += 1
        elif b[num] > a[num]:
            b_count += 1
    
    return (a_count, b_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
