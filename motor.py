import constants as c
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        if("Front" in str(self.jointName)):
            self.frequency = self.frequency/2

        self.numsArray = 2*c.pi*(numpy.arange(c.runs) / c.runs)


        self.motorValues = self.amplitude*numpy.sin(self.frequency * self.numsArray + self.offset)




    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, 
        jointName = self.jointName, 
        controlMode = p.POSITION_CONTROL, 
        targetPosition = desiredAngle,
        maxForce = 500)

    
    def Save_Values(self):
        with open('data/' +self.jointName+ 'SensorValues.npy', 'wb') as f:
            numpy.save(f, self.jointName+ 'SensorValues')


