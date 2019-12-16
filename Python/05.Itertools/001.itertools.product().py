from itertools import product

a, b = list(map(int, input().split())), list(map(int, input().split()))

print(*list(product(a, b)))