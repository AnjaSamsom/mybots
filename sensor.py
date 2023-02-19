import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import numpy
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.runs)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.runs -1:
            print(self.values)
