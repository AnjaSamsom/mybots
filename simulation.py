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

    def __init__(self, direct_or_GUI, SolutionID):
        if direct_or_GUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            c.sleep = 1/1000
        elif direct_or_GUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  
        self.world = WORLD()
        self.robot = ROBOT(SolutionID)
        

    def Run(self):
        for t in range(c.runs):
            time.sleep(c.sleep)
            p.stepSimulation()
            #self.robot.Sense(t)
            #self.robot.Think()
            #self.robot.Act(t)


    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()


