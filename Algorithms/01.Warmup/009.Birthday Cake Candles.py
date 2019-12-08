import math
import os
import random
import re
import sys
from collections import Counter

def birthdayCakeCandles(ar):
    result = [v for k, v in Counter(ar).items()]
    return (max(result))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
