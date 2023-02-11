import numpy
import matplotlib.pyplot


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
arrayDataF = numpy.load("data/arrayDataF.npy")
arrayDataB = numpy.load("data/arrayDataB.npy")




matplotlib.pyplot.plot(frontLegSensorValues, linewidth=3.5, label = "front leg")
matplotlib.pyplot.plot(backLegSensorValues, linewidth=1, label = "back leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()



matplotlib.pyplot.plot(arrayDataF, linewidth=3.5, label = "forward")
matplotlib.pyplot.plot(arrayDataB, linewidth=1, label = "backward")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
