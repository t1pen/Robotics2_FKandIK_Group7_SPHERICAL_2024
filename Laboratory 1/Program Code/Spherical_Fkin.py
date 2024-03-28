## Spherical Manipulator

# Import Libraries

import numpy as np

# link lengths in mm

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# joint variables: is mm if f, is degrees if theta\

T1 = float(input("T1 = ")) #0

T2 = float(input("T2 = ")) #90 deg

d3 = float(input("d3 = ")) #3 

# Convert Rotation angles (deg to rad)
T1 = (T1/180)*np.pi
T2 = (T2/180)*np.pi


# Parametric Table

PT = [[(0.0/180)*np.pi+T1, (90.0/180)*np.pi, 0, a1],
      [(90.0/180)*np.pi+T2, (90.0/180)*np.pi, 0, 0],
      [(0.0/180)*np.pi, (0.0/180)*np.pi, 0, a2+a3+d3]]

# Homegeneous Transformation Matrix Formula

i = 0
H0_1 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]       

i = 1
H1_2 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]] 

i = 2
H2_3 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]


#Multiply Matrices

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2, H2_3)


print ("Spherical Manipulator Forward Kinematics")
print("H0_3 = ")
H0_3 = np.array(np.around(H0_3,3))
print(H0_3)
