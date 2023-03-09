from parallel_hillclimber import PARALLEL_HILLCLIMBER
import os

os.system("del brain*.nndf")

phc = PARALLEL_HILLCLIMBER()
phc.Evolve()