import os
import sys
import time

def timeConversion(s):
    return (time.strftime('%H:%M:%S', time.strptime(s, '%I:%M:%S%p')))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()