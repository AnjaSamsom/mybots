from simulation import SIMULATION
from solution import SOLUTION

sol_id = 0

solution = SOLUTION(sol_id)
solution.Start_Simulation("DIRECT")

simulation = SIMULATION("DIRECT", sol_id)

simulation.Get_Fitness()