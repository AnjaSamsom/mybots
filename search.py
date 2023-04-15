from parallel_hillclimber import PARALLEL_HILLCLIMBER
import random

Ax = random.randint(-10, 10)
temp_x = random.randint(-10, 10)
while abs(Ax-temp_x) < 6:
    temp_x = random.randint(-10, 10)

Bx = temp_x

y = random.randint(-10, 10)

phc = PARALLEL_HILLCLIMBER(Ax, Bx, y)

phc.Evolve()
phc.Show_Best()

