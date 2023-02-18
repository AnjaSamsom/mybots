import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import world
import robot
class SIMULATION:


    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)
        #self.robotId = p.loadURDF("robot.urdf")

        
        #pyrosim.Prepare_To_Simulate(self.robotId)
        self.world = WORLD()    
        self.world = ROBOT()

    def Run(self):
        for i in range(c.runs):
            print(c.runs)
"""             time.sleep(1/60)
            p.stepSimulation()
            self.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            self.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = "Torso_BackLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = self.targetAnglesF[i], maxForce = 500)

            pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = "Torso_FrontLeg", 
controlMode = p.POSITION_CONTROL, targetPosition = self.targetAnglesB[i], maxForce = 500) """
    