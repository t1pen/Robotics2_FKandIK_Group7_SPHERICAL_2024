<h1 align="center">Robotics 2: Forward and Inverse Kinematics of a Spherical Manipulator</h1>
<br>

## Table of Contents
  - [I. Abstract](#i-abstract)
  - [II. Introduction](#ii-introduction)
  - [III. Degrees of Freedom](#iii-degrees-of-freedom)
  - [IV. Kinematic Diagram and D-H Frame](#iv-kinematic-diagram-and-d-h-frame)
  - [V. D-H Parametric Table](#v-d-h-parametric-table)
  - [VI. Homogeneous Transformation Matrix](#vi-homogeneous-transformation-matrix)
  - [VII. Inverse Kinematics](#vii-inverse-kinematics)
  - [VIII. Forward and Inverse Kinematics Calculator (Application)](#viii-forward-and-inverse-kinematics-calculator-application)
  - [IX. References](#ix-references)
  - [X. Group Members](#x-group-members)
<hr> 
<br>


## I. Abstract
<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The field of robotics is brimming with innovation, and our project delves into the fascinating world of spherical manipulators. This project explores the fascinating world of spherical manipulators, robots with three rotational degrees of freedom. We begin by explaining degrees of freedom in an engaging video, laying the groundwork for understanding the manipulator's abilities.
<br>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A clear kinematic diagram depicts the manipulator's structure, which aids in movement analysis. To systematically define the relationship between each joint and link, the Denavit-Hartenberg (D-H) convention is used.  A D-H parameter table is then created, which contains a concise representation of the manipulator's key geometric parameters. The project delves deeper into the concept of homogeneous transformation matrices, a powerful mathematical tool for representing the position and orientation of the end-effector relative to the base frame.  A key focus is on solving the inverse kinematics problem, which determines the joint angles required to achieve the desired end-effector position. To bridge the gap between theory and practice, we present the creation of a user-friendly Graphical User Interface (GUI) calculator. This interactive tool allows users to perform forward and inverse kinematics calculations. The calculator calculates the end-effector pose simply by inputting joint angles (forward kinematics).  Inverse kinematics allows users to specify an end-effector pose and obtain the corresponding joint angles. 
<br>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project provides a thorough examination of spherical manipulator kinematics, combining an educational video explanation with a practical and user-friendly GUI calculator. It aims to improve understanding and control of these versatile robots. So prepare to embark on a journey of discovery! Our project promises to reveal the inner workings of spherical manipulators, paving the way for more precise control and innovative uses.
</p>
<br>



## II. Introduction

  <p align="center">
  <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Pictures/Matlab%20Pic.png style="height: 300px; float: left;">
  <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/MatLab%20Sim/Spherical_Demo.gif style="height: 300px; float: right;">
  </p>
</div>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Spherical Manipulator</i></b> is a stationary manipulator featuring two revolute joints and one prismatic joint, with an arm attached to a robotic base, and a twisting joint. The spherical manipulator was also known as the <b><i>Polar Manipulator</i></b>. It has three mutually perpendicular axes and is well known in the history of robotics, because the first industrial robot, <b><i>Unimate</i></b>, was a spherical robot developed in the 1950s. It is also a type of robotic manipulator that operates with a spherical working envelope. Unlike traditional robotic arms that typically move in a planar or linear fashion, spherical manipulators can move in any direction within a three-dimensional space. These robots often consist of multiple joints arranged in a spherical configuration, allowing for movement along multiple axes simultaneously. This configuration enables them to reach points in 3D space with greater flexibility compared to traditional robotic arms.</p>

<p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Knowing that spherical manipulators have an arm which forms a spherical coordinate system. In mathematics, a spherical coordinate system is a three-dimensional coordinate system in which the position of a point is specified by three numbers: the radial distance from a fixed origin, the polar angle measured from a fixed zenith direction, and the azimuth angle of its orthogonal projection on a reference plane that passes through the origin and is orthogonal to the zenith, measured from a fixed reference direction. The radial distance is also known as the radius or radial coordinate. The polar angle is also known as the zenith angle, normal angle, colatitude, or inclination angle.</p>

  <p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;Spherical Manipulators perform three distinct movements: <i>rotation, elevation,</i> and <i>extension</i> from a stationary base–giving them a spherical/polar working envelope. This configuration allows the robot to move freely and with great flexibility, making it ideal for a variety of jobs. Here is a breakdown of the movements:</p>

- **Rotation**: The robot can rotate around a vertical axis, which forms the base of the robot. This allows the robot to cover a wide horizontal range around its base.
- **Elevation**: The robot's arm can move up and down in a vertical plane, enabling it to reach different heights.
- **Extension**: The robot's arm can extend or retract, moving closer to or farther from the base.

<br>



## III. Degrees of Freedom

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In robotics, <b><i>Degrees of Freedom</i></b> (DOF) refer to the number of independent parameters that define the configuration or motion of a robot. Essentially, it indicates how many different ways a robot can move within its environment.The more the degree of freedom, the more flexible and adaptable the robot. A robot with high DOF can make more complex movements and perform a variety of tasks.</p>
  
<p class="blank-line">&nbsp;</p>

#### The Ideal Degrees of Freedom:
  - A <b>point</b> in 2D: 2-DOF; in 3D space: 3-DOF
  - A <b>rigid body</b> in 3D: 6-DOF
  - <b>Planar Manipulator</b>: 3-DOF
  - <b>Spatial manipulator</b>: 6-DOF
<br>

#### Types of Manipulator based on the number of Degrees of Freedom:
  - <b>Under-Actuated Manipulator</b>
      - _Spatial Manipulator_ with less than 6-DOF
      - _Planar Manipulator_ with less than 3-DOF
  - <b>Ideal manipulator</b>
      - _Spatial Manipulator_ with exactly 6-DOF
      - _Planar Manipulator_ with exactly 3-DOF
  - <b>Redundant manipulator</b>
      - _Spatial Manipulator_ with more than 6-DOF
      - _Planar Manipulator_ with more than 3-DOF
<br>


#### Grubler's Criterion for Mobility
<div align="center">
  
|  Formula for the Mobility of _Spatial Manipulator_  | Formula for the Mobility of _Planar Manipulator_ |
|         :---: |     :-----:      |
| $$M = 6n - \sum_{i=1}^m (6-Ci)$$ |  $$M = 3n - \sum_{i=1}^m (3-Ci)$$ |

</div>

<br>

#### Mechanical Manipulator Anatomy

<div align="center">
  
|  Joint type  | DOF *f* | Constraints *c* between two planar rigid bodies | Constraints *c* between two spatial rigid bodies |
|         ---: |     :-----:      |     :---:     |     :---:    |
|  Revolute (R)  |  1  |  2  |  5  |
|  Prismatic (P)  |  1  |  2  |  5  |
|  Helical (H)  |  1  |  N/A  |  5  |
|  Cylindrical (C)  |  2  |  N/A  |  4  |
|  Universal (U)  |  2  |  N/A  |  4  |
|  Spherical (S)  |  3  |  N/A  |  3  |

</div>
<br>


### Spherical Manipulator Degrees of Freedom (DOF) Computation:
___

<div align="center">
  
|  RRP Spherical Manipulator  | Solution |
|         :---: |     :-----:      |
| <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/47e17d1beba12200080123f1b98170126aadcb39/First%20Page/DOF%20Fig.png alt=DOF-Fig style="height: 200px; float: left;"> |  $$M = 6n - \sum_{i=1}^m (6-Ci)$$  $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$  $$M = 18 - (5 + 5 + 5)$$  $$M = 18 - 15$$  $$M = 3$$  <p>&#8756; This is an Under-Actuated Spatial Manipulator with 3-DOF.</p> |

</div>
<br>


  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The illustration above is a simplified diagram of an RRP Spherical Manipulator. It is also shown above the written computation to get the Degrees of Freedom of Spherical Manipulator. Furthermore, a Spherical Manipulator is a robot or manipulator with two rotational joints and one prismatic joint and it is commonly used on industries that involves material handling and welding. Meanwhile, Degrees of Freedom, as discussed in our classes, is the minimum number of independent parameters or variables or coordinates required to fully describe a system. To get the degrees of freedom for spherical manipulator, the Grubler’s Criterion for Mobility or DOF of Spatial Manipulator is used as the spherical manipulator is a type of spatial manipulator. Based on the computations above, it can be concluded that this spherical manipulator is an Under-Actuated Spatial Manipulator with three degrees of freedom. 
</p>
<br>

#### Degrees of Freedom of a Spherical Manipulator Tutorial Video

[![Degrees of Freedom Vid](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157614915/39e21a83-98fe-494d-a3cf-e3a6db176c38)](https://youtu.be/mnKm1PiER7k?si=11NSObyTCmY0OiG2)

<br>



## IV. Kinematic Diagram and D-H Frame
  <p align="center">
  <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/6b1f57110fecfee109d07f42817c1e87ddae8e89/First%20Page/Kinematic%20Diagram.png alt=Spherical-Manipulator-Kinematic-Diagram style="height: 300px;">
  </div>
<br>

  <p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A <b><i>Kinematic Diagram</i></b> is a simplified representation of a mechanism that illustrates the motion of all the components without showing the forces or the physical dimensions that cause the motion. It is an important tool used in mechanical engineering to examine the motion of mechanisms. Typically, the diagram shows the mechanism's joints and links in schematic form. It is also a diagram that shows how the links and joints are connected together when all of the joint variables have a value of 0.
</p>
<br>

<div align="center">
  
<table border="1">
  <tr>
    <th colspan="2">Joint Variables</th>
  </tr>
  <tr>
    <td> <p align="center">Twisting or Revolute Joint</p> </td>
    <td> <p align="center">Prismatic Linear or Orthogonal Joints</p> </td>
  </tr>
  <tr>
    <td><img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/af546ee69ca1e190b12295380745505086c36d6b/First%20Page/Twisting%20or%20Revolute%20Joint.png alt=Twisting-or-Revolute-Joint style="height: 230px; float: left;"></td>
    <td><img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/af546ee69ca1e190b12295380745505086c36d6b/First%20Page/Prismatic%20Linear%20or%20Orthoganal%20Joint.png alt=Prismatic-Linear-or-Orthogonal-Joints style="height: 200px; float: left;"></td></td>
  </tr>
</table>
</div>
<br>

  <p align="justify"> 
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>Links</i></b> are the rigid parts of the mechanical manipulator. A link is defined as a single part that can be a resistant body or a composite of resistant bodies with inflexible connections and relative motion in relation to other machine components. Also, joints are considered links and the values are constant:</p>
    
  - If it is revolute or twisting, links are drawn from the center of the rotation.
  - If it is prismatic, either linear or orthogonal, links are drawn from the center of translation.
  - If it is from base, links are drawn from the center of gravity.
    
<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <b><i>Joint Variables</i></b>, are the values that change when the joint moves. It is a connection between two or more links that allows for some motion, or potential motion, between them.  Joints are sometimes known as <b><i>kinematic pairs</i></b>. A joint variable has a two indicator which is the rotation of a counterclockwise arrow &#8634; and the arrow with the flat line at the tail &#8614;. We use this symbol &#8634; for the twisting and revolute joint and we label it as <b><i>theta</i></b> ($&theta;$) , theta is the rotation angle of the circle. While in a prismatic joint we use this symbol &#8614; and label it as $d$, $d$ is the translation length. Remember that in joint variables, the numbering of joints will be based on their consecutive order.
</p>
<br>



### D-H Frame Assignment
___

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>D-H Notation</i></b> was introduced by <b>Jacques Denavit</b> and <b>Richard Hartenberg</b> in <b>1955</b> in order to standardize the coordinate frames for spatial linkages. D-H notation is used to solve the forward kinematics of a mechanical manipulator. The <b><i>Frames</i></b> in a Mechanical Manipulator are used to determine where they are and where they need to go. It also shows the movement of our mechanical manipulator. The frames are positioned at each part of the mechanical manipulator, including the base, joints, and end effector.</p>

#### Three Types of Frames used in Mechanical Manipulator:
  - Base (World) Frame
  - User Frame
  - Tool Frame
<br>

<b><i>D-H Frame Assignment</i></b> follow this rules in assigning frames in a kinematic diagram:
  - **Rule 1**: The z axis must be the axis of rotation for a revolute/twisting joint, or the direction of translation for a prismatic joint.
  - **Rule 2**: The x axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it.
  - **Rule 3**: Each axis must intersect the z axis of the frame before it. The rules for complying rule 3:
      - Rotate the axis until it hits the other.
      - Translate the axis until it hits the other.
  - **Rule 4**: All frames must follow the right hand rule. 
<br>


### Applying D-H Frame Rules to the Kinematic Diagram of a Spherical Manipulator
___

<p align="center">
  <img src="https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/d1ef20c165eca1aaeace5ca92892b76bb5c5f78a/First%20Page/Kinematic%20Diagram%20with%20D-H%20Frame.png" style="height: 300px;"></p>
</div>
<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Following the rules for assigning D-H Frames, we obtained the kinematic diagram with D-H frame assignments shown at the illustration above. First is that the z-axis must be the axis of rotation for a revolute/twisting joint or the direction of translation for a prismatic joint. As observed in the illustration above, all of the blue arrows, which are the z-axis, point in the direction of the axis of rotation for the two revolute joints and the direction of translation for the single prismatic joint. The next rule is the x axis must be perpendicular both to its own z-axis, and the z-axis of the frame before it hence it is seen in the illustration that all the red arrows, an indicator for the x-axis, are all perpendicular to its own z-axis as well as to the z-axis of theframe prior to it. The next rule states that the x axis must be perpendicular to both its own z-axis and the z-axis of the frame preceding it. As can be seen in the illustration, all of the red arrows, which indicate the x-axis, are perpendicular to both its own z-axis and the z-axis of the frame prior to it. The third rule states that each axis must intersect the z-axis of the frame that preceded it. And the rules for complying with this rule are to rotate or translate the axis until it hits the other. Hence, the frame for the prismatic joint were translated into the joint before it so that it will comply with the third rule. The last rule of the D-H frame assignment is that all the frames must follow the right-hand rule. Thus, all the green arrows which indicate the y-axis are drawn with the right-hand rule in mind.
</p>
<br>


#### Kinematic Diagram and D-H Frame of a Spherical Manipulator Tutorial Video

[![Kinematic Diagram Vid](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157614915/663645cb-1c74-4885-adbb-916cdb70ea0a)](https://youtu.be/zZ7G4kbAt04?si=Fj-rtLJrEH_eJqRP)

<br>



## V. D-H Parametric Table

#### Steps in Denavit-Hartenberg Notation
  1.  Assign the frames according to the 4 D-H Frame Rules.
  2.  Construct and fill out the D-H Parametric Table.
  3.  Plug the table into the Homogeneous Transformation Matrix form.
  4.  Multiply the matrices together.
<br>


<p align="center"> <b>Example of D-H Parametric Table</b> </p>

<div align="center">
  
| $n$   | $\theta$ | $\alpha$ |    $r$    |    $d$    |
| :---: |  :---:  |  :---:  |  :---:  |  :---:  |   
|   1   |         |         |         |         |
|   2   |         |         |         |         |
|   3   |         |         |         |         |
|   4   |         |         |         |         |

</div>
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The <b><i>Four Parameters</i></b> in the D-H Parametric are  $&theta;$, $&alpha;$ $r$ and $d$. The $&theta;$ and the $&alpha;$ are the rotation or orientation parameters and their units are in degrees or radian. While $d$ and $r$ are the position or translation parameters and their units are in units of length.
  </p>
<br>


<div align="center">
  
| $\theta$ | $\alpha$ | $d$ | $r$ |
|     :---:     |     :---:     |     :---:    |     :---:     
|  " $\theta$ " is the rotation around $z_{n-1}$ that is required to get $x_{n-1}$ to match $x_{n}$, with the joint variable theta if the joint is a revolute or twisting joint.  |   " $\alpha$ " is the rotation around $x_{n}$ that is required to match $z_{n-1}$ to $z_{n}$.  |  " $d$ " is the distance from the origin of $n-1$ and $n$ frames along the $z_{n-1}$ direction with the joint variable if the joint is prismatic.  |  " $r$ " is the distance from the origin of $n-1$ and $n$ frames along the $x_{n}$ direction.  |

</div>
<br>


### D-H Parametric Table for a Spherical Manipulator
___

<p align="center">
  <img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Pictures/Kinematic%20Diagram%20with%20DH%20Frame%20Assignments%20and%20DH%20Parameters.png?raw=true"
" style="height: 300px;"></p>
</div>
<br>

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The figure above is the D-H Parametric table for a Spherical Manipulator. Moreover, a D-H (Denavit-Hartenberg) Parametric Table is a method for organizing the four parameters generated by using the D-H frame assignment rules.  These parameters are useful in determining the kinematic equations of a robotic manipulator. The four parameters are: $theta (\theta$), $alpha (\alpha$), $r$, and $d$. <b><i>Theta</i></b> ($\theta$) represents the angle of the joint between the current and next link. For revolute joints, this is the angle of rotation around the frame's z-axis. It is the rotation around $z_{n-1}$ that is required to get $x_{n-1}$ to match $x_{n}$, with the joint variable theta if the joint is a revolute or twisting joint. The <b><i>alpha</i></b> ($\alpha$) represents the offset angle between the z-axis of frame (n-1) and the z-axis of frame (n). For easier calculations, it is commonly set to 0 or 90 degrees. The <b><i>r</i></b> represents the distance from the origin of n-1 and n frames along the $x_{n}$ direction. And lastly, The <b><i>d</i></b> refers to the distance from the origin of n-1 and n frames along the $z_{n-1}$ direction, with the joint variable if the joint is prismatic. By filling up this table for each link in the manipulator, we will obtain a concise representation of the manipulator's geometry based on these four parameters.  These parameters are then employed in formulas to compute the homogeneous transformation matrices, which ultimately represent the position and orientation of the manipulator's end-effector based on the joint variables.
  </p>
<br>


#### D-H Parametric Table for a Spherical Manipulator Tutorial Video

[![D-H Parametric Table Vid](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157614915/732a991e-9d57-45d1-a0df-d99e02ab7e3f)](https://youtu.be/Bhz1y153_98?si=WD-beuqAP2u4eSK3)

<br>



## VI. Homogeneous Transformation Matrix

<p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Homogeneous Transformation Matrix</i></b> includes both the rotation matrix and the displacement vector in the same matrix. Homogeneous transformation matrices are described as matrices that specify an object's position and orientation. Rotation matrices can be combined using multiplication while Position vectors cannot be added or multiplied. In order to combine position vectors, we shall use the homogeneous transformation matrix denoted as $H_{n}^{n-1}$ or $T_{n}^{n-1}$. The homogeneous transformation matrix contains a superscript and a subscript that indicate the reference frame and projected frame. It is obtained by concatenating 3x3 rotation matrix and 3x1 position vector, resulting in a 3x4 matrix. However, a square matrix is required thus adding an augmentation row is added at the bottom. 
</p>
<br>

<p align="center"> <b>Homogeneous Transformation Matrix Formula</b> </p>

$$
H_{n}^{n-1} =
\begin{bmatrix}
\ Rotation \ (3\times3) & Position \ (3\times1)\\\
0  \ \ \ \ \ \ \ \ \ \ 0 \ \ \ \ \ \ \ \ \ \ \ 0 & 1
\end{bmatrix}
$$
<br>
<br>
<br>

$$H_{n}^{n-1} = 
\begin{bmatrix} 
  cos\theta_{n} & -sin\theta_{n}cos\alpha_{n} & sin\theta_{n} sin\alpha_{n} & r_{n}cos\theta_{n} 
  \\
  sin\theta_{n} & cos\theta_{n}cos\alpha_{n} & -cos\theta_{n}sin\alpha_{n} & r_{n}sin\theta_{n} 
  \\
  0 & sin\alpha_{n} & cos\alpha_{n} & d_{n} 
  \\
  0 & 0 & 0 & 1 
\end{bmatrix}$$

<br>
<br>


### Homogeneous Transformation Matrix of a Spherical Manipulator
___


<p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are two ways to obtain the Homogeneous Transformation Matrix, by manual computation and using the D-H Parametric Table.
</p>
<br>

#### Obtaining the Homogeneous Transformation Matrix Formula Computed Method
  - To obtain $H_{1}^{0}$, concatenate the rotation matrix $r_{1}^{0}$ and the position vector $r_{1}^{0}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below.

$$
H_{1}^{0} =
\begin{bmatrix} 
  c\theta_{1} & 0 & s\theta_{1} & 0 
  \\
  s\theta_{1} & 0 & -c\theta_{1} & 0
  \\
  0 & 1 & 0 & a_{1}
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Same as the previous matrix, to get the $H_{2}^{1}$, concatenate the rotation matrix $r_{2}^{1}$ and position vector $p_{2}^{1}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below. 

$$
H_{2}^{1} =
\begin{bmatrix} 
  -s\theta_{2} & 0 & c\theta_{2} & 0 
  \\
  c\theta_{2} & 0 & s\theta_{2} & 0
  \\
  0 & 1 & 0 & 0
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Lastly, to obtain $H_{3}^{2}$, concatenate the rotation matrix $r_{3}^{2}$ and the position vector $p_{3}^{2}$, followed by the augmentation column 0 0 0 1 at the bottom that gives us this matrix presented below.

$$
H_{3}^{2} =
\begin{bmatrix} 
  1 & 0 & 0 & 0 
  \\
  0 & 1 & 0 & 0
  \\
  0 & 0 & 1 & a_{2}+a_{3}+d_{3}
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>

  - Finally, to determine the homogeneous transformation matrix from frame 0 (the base frame) to frame 3 (the end-effector), multiply all of the transformation matrices $H_{1}^{0}$, $H_{2}^{1}$, and $H_{3}^{2}$ together. Then we can obtain: 

$$
H_{3}^{0} =
H_{1}^{0} \ H_{2}^{1} \ H_{3}^{2}  
\begin{bmatrix} 
  -c\theta_{1}s\theta_{2} & s\theta_{1} & c\theta_{1}c\theta_{2} & c\theta_{1}c\theta_{2}(a_{2}+a_{3}+d_{3})
  \\
  -s\theta_{1}s\theta_{2} & -c\theta_{1} &  s\theta_{1}c\theta_{2} & s\theta_{1}c\theta_{2}(a_{2}+a_{3}+d_{3})
  \\
  -c\theta_{2} & 0 & s\theta_{2} & a_{1}+s\theta_{1}(a_{2}+a_{3}+d_{3})
  \\
  0 & 0 & 0 & 1
\end{bmatrix}
$$

<br>


#### Homogeneous Transformation Matrix of a Spherical Manipulator Tutorial Video

[![Homogeneous Transformation Matrix](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157614863/edb6d97f-dbc4-47c9-8d06-843654c1b489)](https://www.youtube.com/watch?v=5I9Ls5j5U-M)

<br>



## VII. Inverse Kinematics

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Kinematics</i></b> is the study of how bodies move in a robotic mechanism, regardless of the forces or torques that cause the motion. It also studies the relationship between a robot's joint coordinates and its spatial organization, which is a fundamental and classical topic in robotics.
  </p>
<br>

<div align="center">
  
|  Forward Kinematics  | Inverse Kinematics |
|   ---  |   ---  |
|  - The given inputs are the joint variables and the output is the position vector.  |  - The given is the position vector while the output is the joint variables.  |
|  - For identifying the limits of your joint.  |  - For mimicking the motion of the human arm.  |
|  - For obtaining the trajectory solution.  |  - For detailed positioning of the end-effector.  | 
|  - Easier to solve.  |  - Difficult to solve.  |

</div>
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Forward kinematics</i></b> is the geometric problem of finding the position vector and orientation of the end effector using joint variables. It is also a technique for calculating the frames of a robot's links using a configuration and the robot's kinematic structure as input. While <b><i>Inverse kinematics</i></b> is utilized to move the mechanical manipulator. Inverse Kinematics is essentially the opposite operation: it calculates configurations to reach the desired workspace coordinate. This process is required for many robotics activities, including moving a tool along a specified path, manipulating items, and viewing situations from the correct perspective.
  </p>
<br>


### Inverse Kinematics of a Spherical Manipulator using Graphical Method
___

<p align="center">
  <img src="https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/d1ef20c165eca1aaeace5ca92892b76bb5c5f78a/First%20Page/Kinematic%20Diagram%20with%20D-H%20Frame.png" style="height: 300px;"></p>
</div>
<p align="center"> Kinematic Diagram with D-H Frame of a Spherical Manipulator </p>
<br>


<p align="center"> <b>Inverse Kinematics using Graphical Method</b>b> </p> 

<div align="center">
  
|  Top View  | Process |
|   ---  |   ---  |
|  <p align="center"> <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/09f5a206f0c4c7439b1ef3df475fadf370f38396/First%20Page/inverse%20top%201.png alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 250px; width: 1000px"></p>  |  To solve for $\theta_{1}$, use SOHCAHTOA;<br>  &nbsp;&nbsp;&nbsp;&nbsp; $tan \theta_{1}= \frac{opposite}{adjacent}$<br>  &nbsp;&nbsp;&nbsp;&nbsp; $opposite = Y_{3}^{0}$ <br>  &nbsp;&nbsp;&nbsp;&nbsp; $adjacent = X_{3}^{0}$ <br><br>  &nbsp;&nbsp;&nbsp;&nbsp; $\theta_{1}=tan^{-1}(\frac{Y_{3}^{0}}{X_{3}^{0}})$  eq. 1 |
|  <p align="center"> <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/09f5a206f0c4c7439b1ef3df475fadf370f38396/First%20Page/inverse%20top%202.png alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 250px; width: 1000px"></p>  |  &nbsp;&nbsp;&nbsp;&nbsp;However, the hypotenuse is changing its length due to $d_{3}$ since it is a prismatic joint as well as because of the joint 2 being a revolute joint and so, it can change its orientation hence, we will give a new name for our hypotenuse, in this case, $r_{1}$. So from the equation 1, we can now derive the formula for $r_{1}$.<br><br>  $r_{1}=\sqrt{(X_{3}^{0})^{2} + (Y_{3}^{0})^{2}}$  eq. 2  |

</div>
<br>


<div align="center">
  
|  Front View  | Process |
|   ---  |   ---  |
|  <p align="center"> <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/09f5a206f0c4c7439b1ef3df475fadf370f38396/First%20Page/inverse%20front%201.png alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 300px; width: 1250px"></p> <br> <p align="center"> <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/09f5a206f0c4c7439b1ef3df475fadf370f38396/First%20Page/inverse%20front%202.png alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 300px; width: 1250px"></p>  |  &nbsp;&nbsp;&nbsp;&nbsp;And now in terms of the front view of the spherical manipulator, the $r_{1}$ will now be the adjacent length or side of $\theta_{2}$. After placing the $r_{1}$, it can be noticed that we now have a right triangle with the $a_{2}+a_{3}+d_{3}$ being the hypotenuse. However we can’t use the $Z$ as the opposite side of our triangle thus, we will make a another line that would represent the opposite length of  $\theta_{2}$ and we will call it as $r_{2}$. <br><br> Based on the illustration above, we can derive that,<br> &nbsp;&nbsp;&nbsp;&nbsp; $Z = a_{1}+r_{2}$ therefore,<br> &nbsp;&nbsp;&nbsp;&nbsp; $r_{2} =  Z - a_{1}$  eq. 3 <br><br> And so, we can now derive for the formula of  $\theta_{2}$ using again the sohcahtoa;<br> &nbsp;&nbsp;&nbsp;&nbsp; $tan\theta_{2}=\frac{opposite}{adjacent}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $opposite = r_{2}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $adjacent = r_{1}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $\theta_{2}=tan^{-1}(\frac{r_{2}}{r_{1}})$  eq. 4 <br> <br> Finally, to find the joint variable $d_{3}$, the Pythagorean theorem is used;<br> &nbsp;&nbsp;&nbsp;&nbsp; $c_{2} = a_{2} + b_{2}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $( a_{2}+a_{3}+d_{3})^{2} ) = r_{1}^{2} + r_{2}^{2}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $a_{2}+a_{3}+d_{3})^{2} = \sqrt{(r_{1})^{2} + (r_{2})^{2}}$ <br> &nbsp;&nbsp;&nbsp;&nbsp; $d_{3} = \sqrt{(r_{1})^{2}+ (r_{2})^{2}} - a^{2} - a^{3}$  eq. 5  |

</div>
<br>


#### Summary of the Step-by-Step Process on How to Find the Inverse Kinematics of a Spherical Manipulator
  - On the <b><i>Top View</b></i>:
    - To solve for $\theta$<sub>1</sub>, we use the inverse tangent because $Y_{3}^{0}$ and $X_{3}^{0}$ is given.
    - We can’t use $a_{2} + a_{3} + d_{3}$ as hypotenuse that’s why we name our hypotenuse as $r_{1}$.
  - On the <b><i>Front View</b></i>:
      - $r_{1}$ is the length of the link of the prismatic joint and the end-effector that change if $\theta_{2}$ changes its orientation.
      - Then for the new side, which is the $r_{2}$ to get the value of $Z_{3}^{0}$, so the $r_{2}$ is equal to $Z_{3}^{0} - a_{1}$.
      - To solve for $\theta_{2}$, we can use again the inverse tangent formula.
      - Then to solve for $d_{3}$, we will use the Pythagorean Theorem.
<br>


#### Inverse Kinematics of a Spherical Manipulator Tutorial Video

[![Inverse Kinematics Vid](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157614915/11b73c50-734a-40a6-a7f9-aff4a56bae58)]

<br>



## VIII. Forward and Inverse Kinematics Calculator (Application)

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
After the manual calculation of the requirements to build the spherical manipulator, the students applies it in a software based manner for better visualization and interpretation of the theories used in building the spherical manipulator. This was done using <a href='https://www.python.org/'>Python</a> and other libraries that are essential to build the application. 
</p>

### Libraries Used:
___

These are the following libraries used for the application:

- [`roboticstoolbox-python`](https://github.com/petercorke/robotics-toolbox-python) This library was used to visually display the spherical manipulator model after forward and Inverse Kinematics Calculation was done.

- [`numpy`](https://github.com/numpy/numpy) This library was used for mathematical expressions required in modelling the manipulator and express it in Python format.

- [`tkinter`]() This is a library included when you install python. This serves as the library for building the _Graphical User Interface_ (GUI) of the application

- [`openpyxl`](https://openpyxl.readthedocs.io/en/stable/) This library was used in order to save data in an excel file. This helps the user to track down results or serves as the history of results of the application.

- [`pyinstaller`](https://pyinstaller.org/en/stable/) This is used to convert the Python files to an Executable file that allows the application to run to other devices without the necessity to installation of libraries and Python.

- [`auto-py-to-exe`](https://pypi.org/project/auto-py-to-exe/) This library is a .py to .exe converter that uses a simple graphical interface and PyInstaller instead of converting the python file in a terminal.
<br>


### Tkinter Designer
___

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Tkinter is known for its old school way of creating GUI in terms of its aesthetics. <a href="https://github.com/ParthJadhav/Tkinter-Designer">Tkinter Designer</a> is a gui creator developed by <a href="https://github.com/ParthJadhav">ParthJadhav</a> to create modern GUI using a design sofware <a href="https://www.figma.com/files/recents-and-sharing/recently-viewed?fuid=1350011666009633546">Figma</a>. Tkinter Designer uses the Figma API in reading the design file and generates the codes and resource files (assets) needed for the designed GUI. This still uses codes that is built in with tkinter. 
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/42001064/119863796-92af4a80-bf37-11eb-9f6c-61b1ab99b039.png" width= 700>
</p>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Even though Tkinter Designer generates the code itself, code is still needed to be modify because some resources such as fonts and element alignment are not interpreted in the code properly. Troubleshooting and debugging is necessary.  
</p>
<br>

### Graphical User Interface Design
___

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The design of the Graphical User Interface focuses on a modern approach. The GUI uses the following colors for the design of the GUI. 
</p>

#### Color Pallete

- ![#262626](https://via.placeholder.com/15/262626/000000?text=+) `#262626` - Background of the GUI.
- ![#51FF00](https://via.placeholder.com/15/51FF00/000000?text=+) `#51FF00` - Accent Color of the GUI.
- ![#D9D9D9](https://via.placeholder.com/15/D9D9D9/000000?text=+) `#D9D9D9` - Entry Boxes of the GUI.
- ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) `#FFFFFF` - Font Color of the GUI.
- ![#888888](https://via.placeholder.com/15/888888/000000?text=+) `#888888` - Buttons of the GUI.

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Pictures/GUI%20Design/Figma%20Design.png?raw=true" width= 700>
</p>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
However through out the design process and coding the application, we opted to add additional features such as saving the data to an excel file. Moreover, we also added a checkbutton that decides whether the Data will be recorded or not. Below is the final design of the application's GUI run in python.
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Pictures/GUI%20Design/Final%20GUI%20Design.png?raw=true" width= 700>
</p>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Some circumstances such as the font used on the title are modified with what is available with tkinter. Otherwise, the design of the GUI was accomplished based on the user's specification.
</p>
<br>

### Functionality
___

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Tkinter designer only generates the design of the GUI of application but does not directly bind the functionality of the application. With these, we defined functions and bind it with the buttons present in the GUI.
</p>

#### Reset Button

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The reset deletes all the entries present in the all entry boxes. By clicking the reset button, it is expected to do the its function. Here is the demo of the function. 
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Reset_Button.gif?raw=true" width= 700>
</p>
<br>

#### Forward Button

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
The forward button performs the forward kinematics of function of the calculator. The function of these button is to get entry values from entry boxes of the link lengths and the joint variable and do the computations of forward kinematics to obtain the position vector. It also saves the datas in an excel file when the <a href='#recording-data'>Record Data Checkbox</a>  is checked. Additionally, it launches the <code>roboticstoolbox</code> that visually shows the orientation of the manipulator based on the data entered and computation.
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Forward_Button.gif?raw=true" width= 700>
</p>
<br>

#### Inverse Button

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Just like the forward button, this button is binded to run a function for inverse kinematics calculation. Instead, this get entry values from the link lengths and position vector in order to obtain the values of the joint variables. This also record the data when the <a href='#recording-data'>Record Data Checkbox</a> is checked. Then it launches <code>roboticstoolbox</code> to show the orientation of the manipulator.
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Inverse_Button.gif?raw=true" width= 700>
</p>
<br>

#### Recording Data

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
When obtaining the data, it is nice to runback through the obtained results of from the calculator. Glad to help you with that because this calculator records your data instantaneously in an excel file. You also have an option to turn off this feature by unchecking the checkbox. You can also know if the data is recorded or not through an info message box that pop-up the screen. The video below shows the demonstration of turning off/on the record data checkbox.
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Record_Data.gif" width= 700>
</p>
<br>

#### View Excel File

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
As the data from previous session can be recorded, we created a button that is linked to access the excel file where all data are stored. Sheets for forward kinematics data is separated to the inverse kinematics formula. Additionally we add timestamp to better track the desired results.
</p>

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/View_Excel.gif" width= 700>
</p>
<br>

#### Error Message Boxes

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
When entering data, it is inevitable to encounter mistakes. We designed the application to be responsive to these mistake through an error message box showing the error that has occured. Errors are listed below.
</p>

- __Please fill all required fields__ - this error will be encountered if the required entry boxes for either forward or inverse are not filled. 

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Required_Fields.gif" width= 700>
</p>

- __Invalid Input__ - this error will be encountered when a non float value is detected in on the entry boxes. It will be prompt 

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Invalid_Input.gif" width= 700>
</p>

- __Undefined__ - this error occurs when ``ZeroDivisionError`` occured on the inverse kinematics computation. These is due to the [Formula #1]() of the inverse kinematics computation. 

<p align="center">
<img src="https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/GIFs/GUI/Undefined.gif" width= 700>
</p>
<br>

### Installation
___

Installation of the application can be done in two ways: <b>Installer</b>, or <b>Portable Software</b>.

#### Installer (Installation Guide)

1. Download and run the [SphericalCalcApp_setup.exe](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Spherical%20GUI%20Installer/SphericalCalcApp.zip) file.
2. During install it in a directory such as Desktop or Document.
3. Run __Spherical_GUI.exe__ and enjoy the app.

<sub>Installation Video <a href="">Here</a></sub>

#### Portable Software

1. Download the zip file [SphericalCalcApp.zip](https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/main/Midterm%20Project/Spherical%20GUI%20Installer/SphericalCalcApp.zip).
2. Extract the file.
3. Run __Spherical_GUI.exe__ and enjoy the app.

<sub>Installation Video <a href="">Here</a></sub>
<br>
<br>



## IX. References
- Polar/Spherical Robots. (2022, May 13). Midwest Engineered Systems. https://www.mwes.com/types-of-industrial-robots/polar-spherical-robots/
- Agnihotri, N. (2023, June 29). Understanding the degree of freedom in robots. Engineers Garage. https://www.engineersgarage.com/understanding-the-degree-of-freedom-in-robots/
- What is a kinematic diagram, and how does it help in understanding the motion of mechanisms? (n.d.). https://www.proprep.com/questions/what-is-a-kinematic-diagram-and-how-does-it-help-in-understanding-the-motion-of-mechanisms
- Lab, D. (2021, September 30). Kinematics in Robotics. https://www.linkedin.com/pulse/kinematics-robotics-decibelslab
- Automaticaddison, A. (2020, August 26). Find Homogeneous Transformation Matrices for a Robotic Arm – Automatic Addison. https://automaticaddison.com/find-homogeneous-transformation-matrices-for-a-robotic-arm/#:~:text=Homogeneous%20transformation%20matrices%20combine%20both,frame%200%20to%20frame%202
<hr> 
<br>



## X. Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.
