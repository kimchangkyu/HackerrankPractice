a = input().split()
b = input().split()
c = set(input().split())
d = set(input().split())

l_1 = []
l_2 = []
for i in b:
    if i in c:
        l_1.append(i)
    if i in d:
        l_2.append(i)

print(len(l_1) - len(l_2))
