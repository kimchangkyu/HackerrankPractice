import numpy

N, M = map(int, input().split())

array = numpy.array([input().split() for _ in range(N)], int)

numpy.set_printoptions(sign = ' ')

print(numpy.mean(array, axis = 1))
print(numpy.var(array, axis = 0))
print(round(numpy.std(array), 12))