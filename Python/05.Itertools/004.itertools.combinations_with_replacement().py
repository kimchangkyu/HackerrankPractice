from itertools import combinations_with_replacement

datas = list(map(str, input().split()))

print(*list(map("".join, combinations_with_replacement(sorted(datas[0]), int(datas[1])))), sep="\n")