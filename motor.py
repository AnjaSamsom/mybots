import constants as c
import numpy

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset

        self.numsArray = 2*c.pi*(numpy.arange(c.runs) / c.runs)


        self.motorValues = self.amplitude*numpy.sin(self.frequency * self.numsArray + self.phaseOffset)


        """
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesF[i], maxForce = 500)

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesB[i], maxForce = 500)
"""

    def Set_Value(self):
        pass