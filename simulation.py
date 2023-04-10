from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import math

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
        name_list = ["A", "B"]
        self.robots = []
        for name in name_list:
            self.robots.append(ROBOT(SolutionID, name))        

    def Run(self):
        for t in range(c.runs):
            time.sleep(c.sleep)
            p.stepSimulation()
            for robot in self.robots:
                robot.Sense(t)
                robot.Think()
                robot.Act(t)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        for robot in self.robots:
            robot.Get_Fitness()

        robotA = self.robots[0]
        robotB = self.robots[1]

        difference = [0,0]
        for num in range(2):
            difference[num] = robotA.coordinates[num] - robotB.coordinates[num]

        print("cartesian:")
        print(difference)
        print()

        x = difference[0]
        y = difference[1]

        r = math.sqrt(x*x + y*y)
        theta = math.atan(y/x)

        polar = [r, theta]

        print("polar: ")
        print(polar)
        print()
        exit()

