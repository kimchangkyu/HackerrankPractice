import numpy

a, b = map(int, input().split())
array1 = numpy.array([list(map(int, input().split())) for n in range(a)])
array2 = numpy.array([list(map(int, input().split())) for n in range(a)])

print(numpy.add(array1, array2))
print(numpy.subtract(array1, array2))
print(numpy.multiply(array1, array2))
print(array1 // array2)
print(numpy.mod(array1, array2))
print(numpy.power(array1, array2))