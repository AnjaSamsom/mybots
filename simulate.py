import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

# This creates an object, physicsClient, which handles the physics, 
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("robot.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)


frontLegSensorValues = numpy.zeros(c.runs)
backLegSensorValues = numpy.zeros(c.runs)

numsArray = 2*c.pi*(numpy.arange(c.runs) / c.runs)


targetAnglesF = c.amplitudeF*numpy.sin(c.frequencyF * numsArray + c.phaseOffsetF)
targetAnglesB = c.amplitudeB*numpy.sin(c.frequencyB * numsArray + c.phaseOffsetB)


for i in range(c.runs):
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesF[i], maxForce = 500)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesB[i], maxForce = 500)

p.disconnect()


with open('data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)

with open('data/arrayDataF.npy', 'wb') as f:
    numpy.save(f, targetAnglesF)

with open('data/arrayDataB.npy', 'wb') as f:
    numpy.save(f, targetAnglesB)