from simulation import SIMULATION
from solution import SOLUTION

sol_id = 2

solution = SOLUTION(sol_id)
solution.Start_Simulation("GUI")
simulation = SIMULATION("GUI", sol_id)
simulation.Run()