disp("Spherical Manilpulator Forward Kinematics")

syms a1 a2 a3 a4 t1 t2 d3

%% Link Lengths

a1 = 5;
a2 = 5;
a3 = 5;

%% Joint Variables

t1 = 0;
t2 = 0;
d3 = 5;

%% D-H Parameters: [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0, offset = 0, after offset put the value of theta

H0_1 = Link() 

H1_2 =

H2_3 =

H3_4 = 
%% Build Mechanical Manipulator
