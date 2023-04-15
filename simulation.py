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

            robotA = self.robots[0]
            robotB = self.robots[1]


            difference = robotA.coordinates[0] - robotB.coordinates[0]

            # when running through, robot A and robot B both take the distance between
            # the two robots for their hat sensor

            for robot in self.robots:
                robot.Sense(t)
                robotA.sensors["Hat"].Rewrite_Sensor(t, difference)
                robotB.sensors["Hat"].Rewrite_Sensor(t, difference)
                robot.Think()
                robot.Act(t)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        for robot in self.robots:
            robot.Get_Fitness()


            robotA = self.robots[0]
            robotB = self.robots[1]
            
            difference = robotA.coordinates[0] - robotB.coordinates[0]

            fitnessFileName = "fitness_" + robot.name + str(robot.ID) + ".txt"

            f = open("tmp_" + fitnessFileName + ".txt", "w")

            f.write(str(difference))
        
            f.close()






