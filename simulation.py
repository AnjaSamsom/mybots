from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.runs):
            print(t)
            time.sleep(1/60)
            p.stepSimulation()
            ROBOT.Sense(self, t)
        """ 
            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesF[i], maxForce = 500)

            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", 
    controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesB[i], maxForce = 500)
 """


    def __del__(self):
        p.disconnect()