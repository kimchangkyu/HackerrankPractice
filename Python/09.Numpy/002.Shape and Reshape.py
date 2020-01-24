import numpy

array = list(map(int, input().split(" ")))
array = numpy.reshape(array, (3, 3))
print(array)