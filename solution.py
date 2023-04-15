import pyrosim.pyrosim as pyrosim
import numpy
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights_A = 2 * numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) -1
        self.weights_A = self.weights_A * c.numMotorNeurons - 1

        self.weights_B = 2 * numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) -1
        self.weights_B = self.weights_B * c.numMotorNeurons - 1
        self.fitness = 0


    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        nextAvailableID += 1

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Bodies()
        self.Create_Brains()

        os.system("start /B python simulate.py " + mode + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        for name in ["A", "B"]:
            fitnessFileName = "fitness_" + name + str(self.myID) + ".txt"
            while not os.path.exists(fitnessFileName):
                time.sleep(0.01)

            f = open(fitnessFileName, "r")
            self.fitness = float(f.read())

            f.close()
            os.system("del " + fitnessFileName)

    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons-1)
        column = random.randint(0,c.numMotorNeurons-1)

        self.weights_A[row,column] = 2* (random.random() * c.numMotorNeurons - 1) -1
        self.weights_B[row,column] = 2* (random.random() * c.numMotorNeurons - 1) -1


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()


    def Create_Bodies(self):
        pyrosim.Start_URDF("robot_A.urdf")
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)

        pyrosim.Send_Cube(name="Torso", pos=[x,y,1.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x+0.5,y,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x-0.5,y,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Hat" , parent= "Torso" , child = "Hat" , type = "revolute", position = [x,y,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Hat", pos=[0,0,0.125], size=[0.25,0.25,0.25])

        pyrosim.End()


        # this is putting the two robots in the same row so because they can't turn
        # making sure that they are far enough away before the spawn
        pyrosim.Start_URDF("robot_B.urdf")
        temp_x = random.randint(-10, 10)
        while abs(x-temp_x) < 6:
            temp_x = random.randint(-10, 10)

        x = temp_x

             


        #y = random.randint(-10, 10)
        pyrosim.Send_Cube(name="Torso", pos=[x,y,1.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x+0.5,y,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x-0.5,y,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Hat" , parent= "Torso" , child = "Hat" , type = "revolute", position = [x,y,2], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Hat", pos=[0,0,0.125], size=[0.25,0.25,0.25])
        pyrosim.End()


    def Create_Brains(self):
        pyrosim.Start_NeuralNetwork("brain_A" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Hat")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights_A[currentRow][currentColumn])
        
        pyrosim.End()

        pyrosim.Start_NeuralNetwork("brain_B" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Hat")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights_B[currentRow][currentColumn])

        pyrosim.End()
         









   