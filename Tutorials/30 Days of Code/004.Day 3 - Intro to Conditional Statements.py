#!/bin/python3

import math
import os
import random
import re
import sys

def odd(N):
    
    if (N % 2 == 0) and (N > 20):
        return "Not Weird"
    elif N % 3 == 0:
        return "Weird"
    elif (N % 2 == 0) and (2 <= N <= 5):
        return "Not Weird"
    elif (N % 2 == 0) and (6 <= N <= 20):
        return "Weird"
    else:
        return "Weird"

if __name__ == '__main__':
    N = int(input())
    result = odd(N)
    print(result)
