import math
import os
import random
import re
import sys

def plusMinus(arr):
    p_count = n_count = z_count = 0

    for data in arr:
        if data > 0:
            p_count += 1
        elif data < 0:
            n_count += 1
        elif data == 0:
            z_count += 1

    print(p_count / len(arr), n_count / len(arr), z_count / len(arr), sep="\n")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
