import math
import os
import random
import re
import sys

def Calc(number):
    for num in range(1, 11):
        print('{} x {} = {}'.format(number, num, (number * num)))

if __name__ == '__main__':
    number = int(input())
    result = Calc(number)
