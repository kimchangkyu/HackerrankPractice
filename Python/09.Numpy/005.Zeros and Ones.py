import numpy

number = list(map(int, input().split()))

print(numpy.zeros(number, dtype = numpy.int))
print(numpy.ones(number, dtype = numpy.int))