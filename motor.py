import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset
        """
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesF[i], maxForce = 500)

        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesB[i], maxForce = 500)
"""