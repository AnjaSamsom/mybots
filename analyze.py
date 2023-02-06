import numpy
import matplotlib.pyplot


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
arrayData = numpy.load("data/arrayData.npy")


matplotlib.pyplot.plot(frontLegSensorValues, linewidth=3.5, label = "front leg")
matplotlib.pyplot.plot(backLegSensorValues, linewidth=1, label = "back leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()



matplotlib.pyplot.plot(arrayData, linewidth=1, label = "")
matplotlib.pyplot.show()