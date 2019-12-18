from collections import Counter

a = int(input())
b = list(input().split())

for k, v in Counter(b).items():
    if v == 1:
        print(k)