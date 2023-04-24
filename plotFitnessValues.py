import numpy
import matplotlib.pyplot

two = numpy.load("matrixA1.npy")
four = numpy.load("matrixB1.npy")

two = numpy.mean(two, axis = 0)
four = numpy.mean(four, axis = 0)

s2 = numpy.std(two)
s4 = numpy.std(four)



matplotlib.pyplot.plot(two-s2, color = "red", label = "two legged robots -stdev")
matplotlib.pyplot.plot(two, color = "orange", label = "two legged robots")
matplotlib.pyplot.plot(two+s2, color = "yellow", label = "two legged robots + stdev")

matplotlib.pyplot.plot(four-s4, color = "green", label = "four legged robot - stdev")
matplotlib.pyplot.plot(four, color = "blue", label = "four legged robot")
matplotlib.pyplot.plot(four+s4, color = "purple", label = "four legged robot + stdev")


matplotlib.pyplot.legend(loc="upper left")
matplotlib.pyplot.show()
