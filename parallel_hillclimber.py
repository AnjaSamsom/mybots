import copy
from solution import SOLUTION
import constants as c
import os
import numpy as np
import location as l

class PARALLEL_HILLCLIMBER:
    def __init__(self, Ax, Bx, y, legs):

        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}

        self.nextAvailableID = 0

        self.legs = legs

        self.fitness_matrix = np.zeros(shape=(c.populationSize,c.numberOfGenerations))


        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, Ax, Bx, y)
            self.nextAvailableID  += 1

    def Evolve_For_One_Generation(self, currentGeneration):
        
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Store_Fitness(currentGeneration)


    def Store_Fitness(self, currentGeneration):
        population = 0
        for key in self.parents:
            sol = self.parents[key]
            self.fitness_matrix[population][currentGeneration] = sol.fitness
            population += 1



         
    def Print(self):
        print()
        for key in self.parents.keys():
            print(str(self.parents[key].fitness) + " " + str(self.children[key].fitness))
        print()

    def Show_Best(self):

        minimum = self.parents[0]
        for key in self.parents.keys():
            unit = self.parents[key]
            #print(unit.fitness)
            if unit.fitness < minimum.fitness:
                minimum = unit


        minimum.Start_Simulation("DIRECT", self.legs)
        print("the best fitness value is: " + str(minimum.fitness))

        f = open("results.txt", "a")

        f.write(str(minimum.fitness))
        
        f.close()

        if(self.legs == 2):
            test_name = "A" + l.trial
        elif(self.legs == 4):
            test_name = "B" + l.trial
        np.savetxt("matrix" + test_name + ".csv", self.fitness_matrix, delimiter =', ')
        np.save("matrix" + test_name + ".npy", self.fitness_matrix)

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)


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
            solutions[key].Start_Simulation("DIRECT", self.legs)


        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()