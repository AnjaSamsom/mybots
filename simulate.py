from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()


"""



targetAnglesF = c.amplitudeF*numpy.sin(c.frequencyF * numsArray + c.phaseOffsetF)
targetAnglesB = c.amplitudeB*numpy.sin(c.frequencyB * numsArray + c.phaseOffsetB)


with open('data/frontLegSensorValues.npy', 'wb') as f:
    numpy.save(f, frontLegSensorValues)

with open('data/backLegSensorValues.npy', 'wb') as f:
    numpy.save(f, backLegSensorValues)

with open('data/arrayDataF.npy', 'wb') as f:
    numpy.save(f, targetAnglesF)

with open('data/arrayDataB.npy', 'wb') as f:
    numpy.save(f, targetAnglesB) """