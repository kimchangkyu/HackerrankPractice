import math
import os
import random
import re
import sys

def func(n):
    return n[2:]

if __name__ == '__main__':
    n = int(input())
    print(max(func(bin(n)).split("0")).count("1"))