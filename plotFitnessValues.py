import numpy
M = numpy.load("matrixA.npy")
import matplotlib.pyplot


for i in range(10):
    row = M[i,:]
    matplotlib.pyplot.plot(row)

matplotlib.pyplot.show()
