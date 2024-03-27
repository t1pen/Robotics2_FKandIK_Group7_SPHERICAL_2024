import roboticstoolbox as rtb
import numpy as np 
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH

## Create Spherical Manipulator Model
# link lengths in cm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

#link conversion to meters
def cm_to_meter(a):
    m = 100 # 1 meter  = 100 cm
    return a/m

a1 = cm_to_meter(a1)
a2 = cm_to_meter(a2)
a3 = cm_to_meter(a3)

# limit of variable d1
d1 = float(input("d1 = "))
d1 = cm_to_meter(d1)

#Create links
#robot_variable = DHRobot([RevoluteDH(d,r,alpha,offset=theta,qlim)])
#robot_variable = DHRobot([PrismaticDH(d=0,r,alpha,offset=d,qlim)])
Spherical = DHRobot([
    RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    RevoluteDH(0,0,(90.0/180.0)*np.pi,(90.0/180.0)*np.pi,qlim=[0,np.pi/2]),
    PrismaticDH(0,0,(0.0/180)*np.pi,a2+a3,qlim=[0,d1])
], name="Spherical")

print(Spherical)

Spherical.teach(q=[0,0,0])