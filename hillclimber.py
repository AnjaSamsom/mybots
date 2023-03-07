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
        self.child.Evaluate("DIRECT")
        print()
        self.Print()
        print()

        self.Select()

    def Print(self):
        print(str(self.parent.fitness) + " " + str(self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate("GUI")



    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        self.Show_Best()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        self.Show_Best()


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        # if the child does better, set the new parent to the child
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child