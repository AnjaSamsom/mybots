from parallel_hillclimber import PARALLEL_HILLCLIMBER
import location as loc
import constants as c

# change this to change which type of robot you are using
legs = 4

# getting random numbers
Ax = loc.Ax
Bx = loc.Bx
y = loc.y


if legs==2:
    # two legs
    print("two legs")
    c.numSensorNeurons = 3
    c.numMotorNeurons = 2

    phc_A = PARALLEL_HILLCLIMBER(Ax, Bx, y, 2)
    phc_A.Evolve()
    phc_A.Show_Best()


elif legs == 4:
    # four legs
    print("four legs")
    c.numSensorNeurons = 5
    c.numMotorNeurons = 8

    phc_B = PARALLEL_HILLCLIMBER(Ax, Bx, y, 4)
    phc_B.Evolve()
    phc_B.Show_Best()

