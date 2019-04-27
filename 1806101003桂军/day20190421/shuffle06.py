import numpy

print("Before Shufflling 2-dimensional array in Python")
sampleArray = numpy.arange(100, 240, 10)
sampleArray = sampleArray.reshape(7,2)
print (sampleArray)

print("After Shufflling 2-dimensional array in Python")
newArray = numpy.random.shuffle(sampleArray)
print (sampleArray)