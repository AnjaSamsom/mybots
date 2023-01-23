import pyrosim.pyrosim as pyrosim



# to tell pyrosim the name of the file where information about the 
# world you're about to create should be stored. 
# This world will currently be called box, because it will only 
# contain a box (links can be spheres, cylinders, or boxes).
pyrosim.Start_SDF("boxes.sdf")

length = 1
height = 1
width = 1

x = 0
y = 0.5
z = 0

for a in range(5):
    x = 0
    y = 0.5
    z = 0 + a

    length = 1
    height = 1
    width = 1
    for w in range (5):
        x = 0+w
        y = 0.5
        z = 0

        length = 1
        height = 1
        width = 1

        for i in range(10):
            
            length = length * 0.9
            height = height  * 0.9
            width = width  * 0.9

            if i == 0:
                length = height = width = 1

            pyrosim.Send_Cube(name="Box", pos=[x,z,y+i] , size=[length, width, height])



# x2 = 1
# y2 = 1.5
# z2 = 0

# pyrosim.Send_Cube(name="Box", pos=[x,z,y] , size=[length, width, height])
# pyrosim.Send_Cube(name="Box 2", pos=[x2,z2,y2] , size=[length, width, height])


pyrosim.End()

