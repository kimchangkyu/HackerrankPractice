import math
import os
import random
import re
import sys

def reverse(arr):
    arr = arr[::-1]
    return " ".join(map(str, arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = reverse(arr)
    print(result)