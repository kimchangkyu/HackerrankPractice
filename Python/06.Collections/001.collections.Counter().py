from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
counter_arr = Counter(arr)

total = 0
for _ in range(int(input())):
    size, price = map(int, input().split())

    if counter_arr[size]:
        total += price
        counter_arr[size] -= 1

print(total)