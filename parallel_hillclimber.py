import copy
from solution import SOLUTION
import constants as c
import os

class PARALLEL_HILLCLIMBER:
    def __init__(self):

        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}

        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID  += 1

    def Evolve_For_One_Generation(self):
        
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #self.Print()
        self.Select()
        
        
    def Print(self):
        print()
        for key in self.parents.keys():
            print(str(self.parents[key].fitness) + " " + str(self.children[key].fitness))
        print()

    def Show_Best(self):
        minimum = self.parents[0]
        for key in self.parents.keys():
            unit = self.parents[key]
            if unit.fitness < minimum.fitness:
                minimum = unit

        minimum.Start_Simulation("GUI")
        print("the best fitness value is: " + str(minimum.fitness))


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

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
        for unit in self.parents:
            if self.children[unit].fitness < self.parents[unit].fitness:
                self.parents[unit] = self.children[unit]

    def Evaluate(self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")

        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()