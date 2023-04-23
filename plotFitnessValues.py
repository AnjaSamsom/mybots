import numpy
import matplotlib.pyplot

MA = numpy.load("matrixA.npy")
MB = numpy.load("matrixB.npy")

MA = numpy.mean(MA, axis = 0)
MB = numpy.mean(MB, axis = 0)



matplotlib.pyplot.plot(MA, color = "red", label = "two legged robots")
matplotlib.pyplot.plot(MB, color = "blue", label = "four legged robot")

matplotlib.pyplot.legend(loc="upper left")
matplotlib.pyplot.show()
