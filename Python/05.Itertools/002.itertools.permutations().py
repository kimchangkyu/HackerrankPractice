from itertools import permutations

datas = list(map(str, input().split()))

print(*list(map("".join, permutations(sorted(datas[0]), int(datas[1])))), sep="\n")