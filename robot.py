import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class ROBOT:

    def __init__(self):
        self.sensors = {}
        self.motors = {} 
        self.robotId = p.loadURDF("robot.urdf")