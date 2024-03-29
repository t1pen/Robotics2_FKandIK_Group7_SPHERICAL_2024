# Robotics2_FKandIK_Group7_SPHERICAL_2024
<br>

## Table of Contents
  - [I. Abstract](#i.-abstract-)
  - [II. Introduction](#-ii.-introduction-)
  - [III. Degrees of Freedom](#-iii.-degrees-of-freedom-)
  - [IV. Kinematic Diagram and D-H Frame](#-iv.-kinematic-diagram-and-d-h-frame-)
  - [V. D-H Parametric Table](#-v.-d-h-parametric-table-)
  - [VI. Homogeneous Transformation Matrix](#-vi.-homogeneous-transformation-matrix-)
  - [VII. Inverse Kinematics](#-vii.-inverse-kinematics-)
  - [VIII. Forward and Inverse Kinematics (GUI calculator)](#-viii.-forward-and-inverse-kinematics-(gui-calculator)-)
  - [IX. References](#-ix.-references-)
  - [X. Members](#-x.-members)
<hr> 
<br>


## I. Abstract
    (description)
<hr> 
<br>


## II. Introduction

  <p align="center">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/0b0c965065028159e971cf92570e9344e1e41f4b/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20-%20Modern%20Variant.png alt=Spherical-Manipulator-Modern-Variant style="height: 300px; float: left;">
  <img src=https://github.com/MEXECardenas/SPHERICAL_G7_Assignment_2024/blob/a9a0b089f3911adfcc915ab37b061117838ae024/Kinematic%20Diagrams%20with%20D-H%20Parametric%20Tables/Spherical%20Manipulator%20(Modern%20Variant).gif alt=Spherical-Manipulator-(Modern-Variant) style="height: 300px; float: right;">
  </p>
</div>
<br>

<p align="justify"> 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b><i>Spherical Manipulator</i></b> is a stationary manipulator featuring two revolute joints and one prismatic joint, with an arm attached to a robotic base, and a twisting joint. The spherical manipulator was also known as the <b><i>Polar Manipulator</i></b>. It has three mutually perpendicular axes and is well known in the history of robotics, because the first industrial robot, <b><i>Unimate</i></b>, was a spherical robot developed in the 1950s. It is also a type of robotic manipulator that operates with a spherical working envelope. Unlike traditional robotic arms that typically move in a planar or linear fashion, spherical manipulators can move in any direction within a three-dimensional space. These robots often consist of multiple joints arranged in a spherical configuration, allowing for movement along multiple axes simultaneously. This configuration enables them to reach points in 3D space with greater flexibility compared to traditional robotic arms.</p>

<p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Knowing that spherical manipulators have an arm which forms a spherical coordinate system. In mathematics, a spherical coordinate system is a three-dimensional coordinate system in which the position of a point is specified by three numbers: the radial distance from a fixed origin, the polar angle measured from a fixed zenith direction, and the azimuth angle of its orthogonal projection on a reference plane that passes through the origin and is orthogonal to the zenith, measured from a fixed reference direction. The radial distance is also known as the radius or radial coordinate. The polar angle is also known as the zenith angle, normal angle, colatitude, or inclination angle.</p>

  <p align="justify">
  &nbsp;&nbsp;&nbsp;&nbsp;Spherical Manipulators perform three distinct movements: rotation, elevation, and extension from a stationary base–giving them a spherical/polar working envelope. This configuration allows the robot to move freely and with great flexibility, making it ideal for a variety of jobs. Here is a breakdown of the movements:</p>

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


#### Degrees of Freedom (DOF) Computation:

<div align="center">
  
|  RRP Spherical Manipulator  | Solution |
|         :---: |     :-----:      |
| <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/47e17d1beba12200080123f1b98170126aadcb39/First%20Page/DOF%20Fig.png alt=DOF-Fig style="height: 200px; float: left;"> |  $$M = 6n - \sum_{i=1}^m (6-Ci)$$  $$M = 6(3) - [(6-1) + (6-1) + (6-1)]$$  $$M = 18 - (5 + 5 + 5)$$  $$M = 18 - 15$$  $$M = 3$$  <p>&#8756; This is an Under-Actuated Spatial Manipulator with 3-DOF.</p> |

</div>

<hr> 
<br>



## IV. Kinematic Diagram and D-H Frame
  <p align="center">
  <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/6b1f57110fecfee109d07f42817c1e87ddae8e89/First%20Page/Kinematic%20Diagram.png alt=Spherical-Manipulator-Kinematic-Diagram style="height: 300px;">
  <p align="center"> Figure 2. Kinematic Diagram of a Spherical Manipulator </p>
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
    
  - If it is revolute or twisting, links are drawn from the center of the rotation. </p>
  - If it is prismatic, either linear or orthogonal, links are drawn from the center of translation.
  - If it is from base, links are drawn from the center of gravity.
    
<br>

 <p align="justify"> 
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>Joint Variables,</i></b> are the values that change when the joint moves. It is a connection between two or more links that allows for some motion, or potential motion, between them.  Joints are sometimes known as <b><i>kinematic pairs</i></b>. A joint variable has a two indicator which is the rotation of a counterclockwise arrow &#8634; and the arrow with the flat line at the tail &#8614;. We use this symbol &#8634; for the twisting and revolute joint and we label it as <b><i>theta</i></b> (&Theta;), theta is the rotation angle of the circle. While in a prismatic joint we use this symbol &#8614; and label it as <b><i>d,</i></b> <b><i>d</i></b> is the translation length. Remember that in joint variables, the numbering of joints will be based on their consecutive order.</p>
<br>



### D-H Frame

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><i>D-H Notation</i></b> was introduced by <b>Jacques Denavit</b> and <b>Richard Hartenberg</b> in <b>1955</b> in order to standardize the coordinate frames for spatial linkages. D-H notation is used to solve the forward kinematics of a mechanical manipulator. </p>
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The <b><i>Frames</i></b> in a Mechanical Manipulator are used to determine where they are and where they need to go. It also shows the movement of our mechanical manipulator. The frames are positioned at each part of the mechanical manipulator, including the base, joints, and end effector.  </p>
<br>

#### Three Types of Frames used in Mechanical Manipulator:
  - Base (World) Frame
  - User Frame
  - Tool Frame
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>D-H Frame Rules</i></b> is the rules used in assigning frames in a kinematic diagram.  </p>
<br>

  - **Rule 1**: The z axis must be the axis of rotation for a revolute/twisting joint, or the direction of translation for a prismatic joint.
  - **Rule 2**: The x axis must be perpendicular both to its own Z axis, and the Z axis of the frame before it. \
  - **Rule 3**: Each axis must intersect the z axis of the frame before it. The rules for complying rule 3:
      - Rotate the axis until it hits the other.
      - Translate the axis until it hits the other.
  - **Rule 4**: All frames must follow the right hand rule. 
<br>


  <p align="center">
  <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/6b1f57110fecfee109d07f42817c1e87ddae8e89/First%20Page/Kinematic%20Diagram%20with%20D-H%20Frame.png alt=Spherical-Manipulator-Kinematic-Diagram-with-D-H-Frame style="height: 300px;"></p>
<p align="center"> Figure 3. Kinematic Diagram and D-H Frame of a Spherical Manipulator </p>
</div>
<br>


<p align="center"> <b>Kinematic Diagram and D-H Frame Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=Kinematic-Diagram-and-D-H-Frame-Tutorial-Video style="height: 300px; float: left;">
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
  
|  n  | &Theta; | &alpha; | r | d |
|     :---:     |     :---:     |     :---:     |     :---:    |     :---:     
|  1  |    |    |    |
|  2  |    |    |    |
|  3  |    |    |    |
|  4  |    |    |    |

</div>
<br>


 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  The <b><i>Four Parameters</i></b> in the D-H Parametric are  &Theta;, &alpha; r and d. The &Theta; and the &alpha are the rotation or orientation parameters and their units are in degrees or radian. While d and r are the position or translation parameters and their units are in units of length.
  </p>
<br>


<div align="center">
  
| &Theta; | &alpha; | r | d |
|     :---:     |     :---:     |     :---:    |     :---:     
|  <b>"&Theta;"</b> is the rotation around z <sub>n-1</sub> that is required to get x <sub>n-1</sub> to match x <sub>n</sub>, with the joint variable theta if the joint is a revolute or twisting joint.  |   <b>"&alpha;"</b> is the rotation around x <sub>n</sub> that is required to match z <sub>n-1</sub> to z <sub>n</sub>.  |  <b>"d"</b> is the distance from the origin of n-1 and n frames along the z <sub>n-1</sub> direction with the joint variable if the joint is prismatic.  |  <b>"r"</b> is the distance from the origin of n-1 and n frames along the x <sub>n</sub> direction.  |

</div>
<br>


<p align="center"> <b>D-H Parametric Table of Spherical Manipulator</b> </p>
  <p align="center">
  <img src=https://github.com/yannaaa23/Robotics2_Midterm_Try/blob/f7fb56960b0356ba05be5484fbbf70c3b3404437/First%20Page/D-H%20parametric%20Table.png alt=D-H-Parametric-table-of-Speherical-Manipulator style="height: 300px;"></p>
</div>
<br>


<p align="center"> <b>D-H Prametric Table Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=D-H-Parametic-Table-Tutorial-Video style="height: 300px; float: left;">
<br>



## VI. Homogeneous Transformation Matrix

 <p align="justify"> 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <b><i>Homogeneous transformation Matrix</i></b> includes both the rotation matrix and the displacement vector in the same matrix. Furthermore, homogeneous transformation matrices are described as matrices that specify an object's position and orientation. 3x3 rotation matrices can be combined using multiplication. Position vectors cannot be added or multiplied. And to combine position vectors, we shall use the homogeneous transformation matrix, denoted as H or T . The homogeneous transformation matrix contains a superscript and a subscript that indicate the reference and projected frames. It consists of a 3x3 rotation matrix paired with our 3x1 position vector, resulting in a 3x4 matrix. A square matrix is the equal sum of the rows and columns. To make this equal and to make it 4x4 matrix, an augmentation column (0 0 0 1) is added. 
  </p>
<br>

<p align="center"> <b>&#128512; HINDI KO NA ALAM ANG KASUNOD &#128512; </b> </p>


<p align="center"> <b>Homogeneous Transformation Matrix of a Spherical Manipulator</b> </p>
  <p align="center">
  <img src=link alt=Homogeneous-Transformation-Matrix-of-a-Spherical-Manipulator style="height: 300px;"></p>
</div>
<br>


<p align="center"> <b>Homogeneous Transformation Matrix of a Spherical Manipulator Tutorial Video</b> </p>
  <p align="center">
  <img src=link alt=Homogeneous-Transformation-Matrix-of-a-Spherical-Manipulator-Tutorial-Video style="height: 300px; float: left;">
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


<p align="center"> <b>Inverse Kinematics of a Spherical Manipulator</b> </p>

<div align="center">
  
|  Top View  | Front View |
|   ---  |   ---  |
|  <p align="center"> <img src=link alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 300px;"></p>  |  <p align="center"> <img src=link alt=Inverse-Kinematics-of-a-Spherical-Manipulator style="height: 300px;"></p>  |

</div>
<br>


#### Summary of the Step-by-Step Process on How to Find the Inverse Kinematics of a Spherical Manipulator
  - On the <b><i>Top View</b></i>:
    - To solve for &Theta;<sub>1</sub>, we use the inverse tangent because Y<sup>0</sup><sub>3</sub> and X<sup>0</sup><sub>3</sub> is given.
    - We can’t use a<sub>2</sub> + a<sub>3</sub> + d<sub>3</sub> as hypotenuse that’s why we name our hypotenuse as r<sub>1</sub>.
  - On the <b><i>Front View</b></i>:
      - r<sub>1</sub> is the length of the link of the prismatic joint and the end-effector that change if &Theta;<sub>2</sub> changes its orientation.
      - Then for the new side, which is the r<sub>2</sub> to get the value of Z<sup>0</sup><sub>3</sub>, so the r<sub>2</sub> is equal to Z<sup>0</sup><sub>3</sub> - a<sub>1</sub>.
      - To solve for &Theta;<sub>2</sub>, we can use again the inverse tangent formula.
      - Then to solve for d<sub>3</sub>, we will use the Pythagorean Theorem.
<br>





## VIII. Forward and Inverse Kinematics (GUI calculator)

<br>


## IX. References
-
-
-
-
-
<hr> 
<br>



## Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.


















<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
## Table of Contents
- [Kinematic Diagram and Parametric Table of Spherical Manipulator](#-kinematic-diagram-and-parametric-table-of-spherical-manipulator-)
- [Derivation of Inverse Kinematics using Graphical Method](#-derivation-of-inverse-kinematics-using-graphical-method-)
- [Comparison of Forward and Inverse Kinematics in MATLAB and Phyton](#-comparison-of-forward-and-inverse-kinematics-in-matlab-and-phyton-)
   - [Trial Table of Forward Kinematics in MATLAB and Python](#-trial-table-of-forward-kinematics-in-matlab-and-python-)
   - [Trial Table of Inverse Kinematics in MATLAB and Python](#-trial-table-of-inverse-kinematics-in-matlab-and-python-)
- [Group Members](#group-members)
<br>

<h1 align="center"> Kinematic Diagram and Parametric Table of Spherical Manipulator </h1> 
<p align="center">
  <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157677365/c0c481a4-3d7c-4005-83e1-21bc436ec15e alt=DH_Frame_and_Parametric_Table width="700"/>
<p align="center">
</p>
<br>
<br>

<h1 align="center"> Derivation of Inverse Kinematics using Graphical Method </h1> 
<p align="center">
   <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157677365/b659b633-7068-412a-b9b0-58626bb0287f alt=Inverse_Kinematics_Graphical_Method_1 width="700"/>
<p align="center">
   <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/assets/157677365/d8f43e6d-8a61-4257-808e-a8dff408b0ef alt=Inverse_Kinematics_Graphical_Method_2 width="700"/>
<br>
<br>

<h1 align="center"> Comparison of Forward and Inverse Kinematics in MATLAB and Phyton </h1>
<hr>

<h1 align="center"> Trial Table of Forward Kinematics in MATLAB and Python </h1> 
<p align="center">
  <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/0d4a1af26e3a6964fa47395ed9f41d56eaa53fae/Trial%20Table%20for%20Forward%20and%20Inverse%20Kinematics/Trial%20Table%20for%20Forward%20Kinematics.png alt=trial-table-of-forward-kinematics-in-matlab-and-python width="800"/>
</p>
<br>
<br>

<h1 align="center"> Trial Table of Inverse Kinematics in MATLAB and Python </h1> 
<p align="center">
  <img src=https://github.com/t1pen/Robotics2_FKandIK_Group7_SPHERICAL_2024/blob/440b5c7742bceab7f9bf815b060b93355776fd29/Trial%20Table%20for%20Forward%20and%20Inverse%20Kinematics/Trial%20Table%20for%20Inverse%20Kinamatics.png alt=trial-table-of-inverse-kinematics-in-matlab-and-python width="990"/>
</p>
<br>
<br>


### Group Members:
- Alojado, Stephen Gabriel S.
- Apostol, Jan Benedict D.
- Cardenas, Sofia Bianca J.
- Catapang, Jamil Darrius S.
- Umali, Ariane Mae D.
