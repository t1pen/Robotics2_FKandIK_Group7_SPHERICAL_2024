import numpy as np

## Spherical Manipulator Inverse Kinematics

# link lengths in mm

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# Position Vector

x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))

## Formula List
theta1 = np.arctan(y0_3/x0_3)*180/np.pi # Formula 1
r1 = np.sqrt((x0_3**2) + (y0_3**2)) # Formula 2
r2 = z0_3 - a1 # Formula 3 
theta2 = np.arctan(r2/r1)*180/np.pi # Formula 4
d3 = np.sqrt((r1**2) + (r2**2)) - a2 - a3 # Formula 5

#Display the Joint Variables
print("theta1 = ", np.around(theta1,3))
print("theta2 = ", np.around(theta2, 3))
print("d3 = ", np.around(d3, 3))