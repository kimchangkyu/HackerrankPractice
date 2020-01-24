import numpy

datas = list(map(int, input().split(' ')))
result = ((datas[0] + datas[1]), datas[2])
print(numpy.array([input().split() for _ in range(result[0])], int))