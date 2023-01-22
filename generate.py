import pyrosim.pyrosim as pyrosim



# to tell pyrosim the name of the file where information about the 
# world you're about to create should be stored. 
# This world will currently be called box, because it will only 
# contain a box (links can be spheres, cylinders, or boxes).
pyrosim.Start_SDF("box.sdf")

length = 1
height = 1
width = 1

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length, height, width])

pyrosim.End()

