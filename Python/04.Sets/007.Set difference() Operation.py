i, m = input(), set(map(int, input().split()))
i, n = input(), set(map(int, input().split()))

print(len(m.difference(n)))