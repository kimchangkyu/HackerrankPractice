def mutations(a):
    word = input().split()[0]
    b = set(map(int, input().split()))

    if word == "intersection_update":
        a.intersection_update(b)
    
    if word == "update":
        a.update(b)

    if word == "symmetric_difference_update":
        a.symmetric_difference_update(b)

    if word == "difference_update":
        a.difference_update(b)

number, a = input(), set(map(int, input().split()))
for i in range(int(input())):
    mutations(a)

print(sum(a))