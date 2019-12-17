from itertools import combinations

datas = list(map(str, input().split()))

for i in range(1, int(datas[1]) + 1):
    print(*list(map("".join, combinations(sorted(datas[0]), i))), sep="\n")