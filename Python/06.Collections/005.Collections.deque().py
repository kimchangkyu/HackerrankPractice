from collections import deque

d = deque()

N = int(input())

for _ in range(N):
    command= input().split()
    if command[0] == "append":
        d.append(command[1])
    elif command[0] == "appendleft":
        d.appendleft(command[1])
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()

for i in d:
    print(i, end=" ")