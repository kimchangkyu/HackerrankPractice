import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    for idx in range(len(arr)):
        result = sum(arr)
    print((result - max(arr)), (result - min(arr)))
   
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
