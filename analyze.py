import numpy
import matplotlib.pyplot


frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")


backLegSensorValues = numpy.load("data/backLegSensorValues.npy")

matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()