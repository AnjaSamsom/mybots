import sys
from simulation import SIMULATION

direct_or_GUI = sys.argv[1]
SolutionID = sys.argv[2]

simulation = SIMULATION(direct_or_GUI, SolutionID)
simulation.Run()
simulation.Get_Fitness()