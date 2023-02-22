from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR

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
            time.sleep(1/60)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
        self.MOTOR.Save_Values()


    def __del__(self):
        p.disconnect()