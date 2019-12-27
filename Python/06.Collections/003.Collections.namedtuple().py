from collections import namedtuple

N = int(input()) # 총 학생수
Student = namedtuple('Student', input())

total = 0
for _ in range(N):
    xyz = Student(*input().split())
    total += sum([int(xyz.MARKS)])

print(total / N)