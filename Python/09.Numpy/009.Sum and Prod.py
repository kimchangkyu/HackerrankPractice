import numpy

N, M = map(int, input().split())

array1 = numpy.array([list(map(int, input().split())) for n in range(N)])

print(numpy.prod(numpy.sum(array1, axis = 0), axis = 0))