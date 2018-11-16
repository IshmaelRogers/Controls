# Ishmael Rogers
# Robotics Engineer, Infinitely Deep Robotics Group
# www.idrg.io
# 2018 

[image1]: ./images/blockdiagram.jpg
[image2]: ./images/closed_loop.PNG
[image3]: ./images/idealcontroller.PNG
# Controls engineering 
A multi-disciplinary topic with roots in engineering and applied mathematics

design systems that have a predicatable and desire response to an input. 

In robotics, movement commands, yaw, pitch roll, speed control 

# Open-loop control

Open loop control systems do not have sensors that measure the output of the system. Furthermore, the lack the capability to correct error in the system. The performance of a household toaster does not directly measure the how "well" the toast is cooked. The hungry operator of the toaster simply inputs desired heat and time settings and the toaster carries out those commands regardless of the state of the toast inside. In a simple system this behavior is tolerable but, for a more complex system with mission critical tasks, we must develop a way for the system to monitor its on performance and correct errors due to distrubances 


# Closed-loop control

![alt text][image1]


Closed loop control features a sensor that constantly monitors the output of the system. We relate the sensor readings to the input with the use of a summing node. Can function in a wide range of operating condition. A well designed and finely tuned feedback controller is essential in applications where predictability is limited. 

* <a href="https://www.codecogs.com/eqnedit.php?latex=r(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r(t)" title="r(t)" /></a> - Is the input signal or desired set point

* <a href="https://www.codecogs.com/eqnedit.php?latex=y(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y(t)" title="y(t)" /></a> - Is the output of the system

* <a href="https://www.codecogs.com/eqnedit.php?latex=\sum" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum" title="\sum" /></a> - Is the summing node that calculates the difference between the disred set point and the output measured by the sensor.

* <a href="https://www.codecogs.com/eqnedit.php?latex=e(t)&space;=&space;r(t)&space;-y(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(t)&space;=&space;r(t)&space;-y(t)" title="e(t) = r(t) -y(t)" /></a> -The error signal is feed into the systems controller. 
NOTE: The controller takes this error signal and adjusts the system's parameters that will drive the error to zero. 

* <a href="https://www.codecogs.com/eqnedit.php?latex=u(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(t)" title="u(t)" /></a> - The control signal represents the output of the controller and the input to the plant

Below is the block diagram of a simple cruise control system
--
![alt text][image2]

# PID
t
If we isolate the controller portion of the block diagram and "look inside" we can understand how the control signal,  <a href="https://www.codecogs.com/eqnedit.php?latex=u(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(t)" title="u(t)" /></a> is produced. 

Three components
---
Proportional, integral, derivative components take the error, <a href="https://www.codecogs.com/eqnedit.php?latex=e(t)&space;=&space;r(t)&space;-y(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(t)&space;=&space;r(t)&space;-y(t)" title="e(t) = r(t) -y(t)" /></a> manipluates it. 

NOTE: The algrebraic sum of these components represent the control signal.

There are three parameters associated with each component that needs to be tuned by the designer in order to acheieve optimal performance and stability. 

Controller gains
---
<a href="https://www.codecogs.com/eqnedit.php?latex=k_{p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{p}" title="k_{p}" /></a> 

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{i}" title="k_{i}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{d}" title="k_{d}" /></a>

 

NOTE: must be sa

So common because of the reliablity in various field

simple and inexpensive to produce

Do not require a mathematical model

Ideal controller 

![alt text][image3]

Parameterstake the error and manipulate it in some way.

# P- Control

# PI- Control

# PD- Control

# PID - Control 

# Limitations

# Real life case - Integrator Windup

# Real life case - Noise

# Control Design Objective and Criteria 

# Tuning Strategies 

# Combine Concepts

# Project: Quadrotor Control using PID 


