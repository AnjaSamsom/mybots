import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy


# This creates an object, physicsClient, which handles the physics, 
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = numpy.zeros(500)
backLegSensorValues = numpy.zeros(500)


for i in range(500):
    time.sleep(1/60)
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

p.disconnect()


with open('data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)