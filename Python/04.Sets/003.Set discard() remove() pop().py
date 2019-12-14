n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    data = input().split()
    if data[0] == "pop":
        s.pop()
    elif data[0] == "remove":
        s.remove(int(data[1]))
    elif data[0] == "discard":
        s.discard(int(data[1]))

print(sum(s))