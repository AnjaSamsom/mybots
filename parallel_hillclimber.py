import copy
from solution import SOLUTION
import constants as c
import random

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        self.parents = {}

        self.nextAvailableID = 0

        for i in range(c.populationSize):
            print(self.nextAvailableID)

            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID  += 1



        

    def Evolve_For_One_Generation(self):
        
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        exit()

        # self.child.Start_Simulation("DIRECT")
        # print()
        # self.Print()
        # print()

        # self.Select()
        
        

    def Print(self):
        print(str(self.parent.fitness) + " " + str(self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate("GUI")



    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        #self.Show_Best()


    def Spawn(self):
        self.children = {}

        for key in self.parents.keys():
            unit = copy.deepcopy(self.parents[key])
            self.nextAvailableID += 1
            self.children[key] = unit


    def Mutate(self):
        for key in self.children.keys():

            self.children[key].Mutate()


    def Select(self):
        # if the child does better, set the new parent to the child
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Evaluate(self, solutions):
        for value in solutions.items():
            value[1].Start_Simulation("GUI")

        for value in solutions.items():
            value[1].Wait_For_Simulation_To_End()