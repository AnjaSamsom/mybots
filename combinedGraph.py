import numpy
import matplotlib.pyplot

# A is the bipeds
# B is the quadrupeds
# the number after is the trial, a trial is using the same random placement of the two robts for fairness

A1 = numpy.load("matrixA1.npy")
B1 = numpy.load("matrixB1.npy")
A2 = numpy.load("matrixA2.npy")
B2 = numpy.load("matrixB2.npy")
A3 = numpy.load("matrixA3.npy")
B3 = numpy.load("matrixB3.npy")
A4 = numpy.load("matrixA4.npy")
B4 = numpy.load("matrixB4.npy")
A5 = numpy.load("matrixA5.npy")
B5 = numpy.load("matrixB5.npy")

A1 = numpy.mean(A1, axis = 0)
B1 = numpy.mean(B1, axis = 0)
A2 = numpy.mean(A2, axis = 0)
B2 = numpy.mean(B2, axis = 0)
A3 = numpy.mean(A3, axis = 0)
B3 = numpy.mean(B3, axis = 0)
A4 = numpy.mean(A4, axis = 0)
B4 = numpy.mean(B4, axis = 0)
A5 = numpy.mean(A5, axis = 0)
B5 = numpy.mean(B5, axis = 0)

matplotlib.pyplot.plot(A1, color = "red", label = "two legged robots")
matplotlib.pyplot.plot(A2, color = "red")
matplotlib.pyplot.plot(A3, color = "red")
matplotlib.pyplot.plot(A4, color = "red")
matplotlib.pyplot.plot(A5, color = "red")



matplotlib.pyplot.plot(B1, color = "blue", label = "four legged robots")
matplotlib.pyplot.plot(B2, color = "blue")
matplotlib.pyplot.plot(B3, color = "blue")
matplotlib.pyplot.plot(B4, color = "blue")
matplotlib.pyplot.plot(B5, color = "blue")



matplotlib.pyplot.legend(loc="upper left")
matplotlib.pyplot.show()
