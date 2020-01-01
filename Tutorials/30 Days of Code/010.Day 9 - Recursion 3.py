import math
import os
import random
import re
import sys

def factorial(n):
    a = n
    for i in range(n, 1, -1):
        a *= (i - 1)
    return a
if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)