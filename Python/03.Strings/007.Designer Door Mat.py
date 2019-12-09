number = list(map(int, input().strip().split()))
ss = ".|."
string = "WELCOME"

num2, num3 = 1, number[0] - 2
for num in range(1, number[0] + 1):
    if int((number[0] - 1) / 2) > num - 1:
        print("-" * int((number[1] - (len(ss) * num2)) / 2) + ss * (1 * num2) + "-" * int((number[1] - (len(ss) * num2)) / 2))
        num2 += 2
    if int((number[0] - 1) / 2) == num:
        print("-" * int((number[1] - (len(string) - 1)) / 2) + string + "-" * int((number[1] - (len(string) - 1)) / 2))
    if int((number[0] - 1) / 2) < num + 1:
        print("-" * int((number[1] - (len(ss) * num3)) / 2) + ss * (1 * num3) + "-" * int((number[1] - (len(ss) * num3)) / 2))
        num3 -= 2
        if num3 <= 0:
            break
