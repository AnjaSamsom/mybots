import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
pi = math.pi

def scale(num):

    if num < 0.5:    
        num = num*(-1*pi/2.0)
    else:
        num = num*(pi/2.0)
    return num/8

for i in range(500):
    print(scale(random.random()))

# This creates an object, physicsClient, which handles the physics, 
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

runs = 1000
amplitude = pi/4
frequency = 1
phaseOffset = 0


frontLegSensorValues = numpy.zeros(runs)
backLegSensorValues = numpy.zeros(runs)

numsArray = 2*pi*(numpy.arange(runs) / runs)
#targetAngles = (pi/4)*numpy.sin(numsArray)
#targetAngles = numpy.sin(numsArray)

targetAngles = numpy.zeros(runs)
for i in range(len(numsArray)):
    targetAngles[i] = amplitude * numpy.sin(frequency * i + phaseOffset)

for i in range(runs):
    time.sleep(1/240)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 500)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 500)

p.disconnect()


with open('data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)

with open('data/arrayData.npy', 'wb') as f:
    numpy.save(f, targetAngles)