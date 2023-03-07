import copy
from solution import SOLUTION
import constants as c
import random

class HILLCLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()


    def Evolve(self):
        self.parent.Evaluate()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        print(self.parent.weights)
        print(self.child.weights)
        exit()


    
    def Select(self):
        pass