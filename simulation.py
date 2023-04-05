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
<<<<<<< HEAD
        name_list = ["A", "B"]
        self.robots = []
        for name in name_list:
            self.robots.append(ROBOT(SolutionID, name))
=======
        self.robotA = ROBOT(SolutionID, "A")
        self.robotB = ROBOT(SolutionID, "B")

>>>>>>> 1186aee1fe9cabde7f6885da0e4e2e1f0d1f50ce
        

    def Run(self):
        for t in range(c.runs):
            time.sleep(c.sleep)
            p.stepSimulation()
<<<<<<< HEAD
            for robot in self.robots:
                robot.Sense(t)
                robot.Think()
                robot.Act(t)
=======
            self.robotA.Sense(t)
            self.robotA.Think()
            self.robotA.Act(t)
            self.robotB.Sense(t)
            self.robotB.Think()
            self.robotB.Act(t)
>>>>>>> 1186aee1fe9cabde7f6885da0e4e2e1f0d1f50ce


    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        for robot in self.robots:
            robot.Get_Fitness()


