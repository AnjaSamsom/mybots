from parallel_hillclimber import PARALLEL_HILLCLIMBER
import location as l
import constants as c
import os
import time

trial = 1
while trial<=10:
    trial = str(trial)

    os.system("python location.py")
    l.trial = trial

    # change this to change which type of robot you are using

    # getting random numbers
    Ax = l.Ax
    Bx = l.Bx
    y = l.y


    legs = 2
    # two legs
    print("two legs")
    c.numSensorNeurons = 3
    c.numMotorNeurons = 2

    phc_A = PARALLEL_HILLCLIMBER(Ax, Bx, y, 2)
    phc_A.Evolve()
    phc_A.Show_Best()

    time.sleep(10)


    legs = 4
    # four legs
    print("four legs")
    c.numSensorNeurons = 5
    c.numMotorNeurons = 8

    phc_B = PARALLEL_HILLCLIMBER(Ax, Bx, y, 4)
    phc_B.Evolve()
    phc_B.Show_Best()

    time.sleep(10)

    trial = int(trial)
    trial += 1

os.system("python combinedGraph.py")
