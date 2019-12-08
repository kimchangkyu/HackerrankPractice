#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for num in range(1, n + 1):
        print(" " * (n - num) + "#" * num)

if __name__ == '__main__':
    n = int(input())
    staircase(n)