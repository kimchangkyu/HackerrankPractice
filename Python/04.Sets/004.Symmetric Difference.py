num1, num2 = int(input()), set(map(int, input().split()))
num3, num4 = int(input()), set(map(int, input().split()))

result1 = num2.union(num4)
result2 = num2.intersection(num4)
result3 = result1 - result2
print(*sorted(result3), sep = "\n")