disp("Spherical Manilpulator Forward Kinematics")

syms a1 a2 a3 a4 t1 t2 d3

%% Link Lengths

a1 = 50;
a2 = 20;
a3 = 15;

%% Joint Variables

t1 = pi/180*(0);
t2 = pi/180*(90);
d3 = 25;

%% D-H Parameters: [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0, offset = 0, after offset put the value of theta

H0_1 = Link([0,a1,0,pi/2,0,t1]); 
H0_1.qlim = pi/180*[-90 90];

H1_2 = Link([0,0,0,pi/2,0,t2]);
H1_2.qlim = pi/180*[-45 45];

H2_3 = Link([0,0,0,0,1,a2+a3]);
H2_3.qlim = [0 d3];

%% Build Mechanical Manipulator

Spherical = SerialLink([H0_1 H1_2 H2_3], 'name', 'Spherical')
Spherical.plot([0 0 0], 'workspace', [-80 80 -80 80 -10 130])
Spherical.teach

