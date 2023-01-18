import pybullet as p
import time

# This creates an object, physicsClient, which handles the physics, 
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for i in range(1001):
    time.sleep(1/60)
    p.stepSimulation()
    print(i)
p.disconnect()