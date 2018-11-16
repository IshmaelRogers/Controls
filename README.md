# Ishmael Rogers
# Robotics Engineer, Infinitely Deep Robotics Group
# www.idrg.io
# 2018 

[image1]: ./images/blockdiagram.jpg
[image2]: ./images/closed_loop.PNG
[image3]: ./images/idealcontroller.PNG
[image4]: ./images/quad.jpg
[image5]: ./images/kp_characteristics.png
[image6]: ./images/stepResponse.png
[image7]: ./images/typesofoscillations

# Controls Systems engineering 
A multi-disciplinary topic with roots in engineering and applied mathematics

design systems that have a predicatable and desire response to an input. 

In robotics, movement commands, yaw, pitch roll, speed control 

# Open-loop control

Open loop control systems do not have sensors that measure the output of the system. Furthermore, the lack the capability to correct error in the system. The performance of a household toaster does not directly measure the how "well" the toast is cooked. The hungry operator of the toaster simply inputs desired heat and time settings and the toaster carries out those commands regardless of the state of the toast inside. In a simple system this behavior is tolerable but, for a more complex system with mission critical tasks, we must develop a way for the system to monitor its on performance and correct errors due to distrubances 

Please see the Open Control folder in this repo for code that can be used to get an idea of the performance of an open loop controller designed for a drone


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
The PID controller is known for being the most reliable scheme in industry. It is very relatively inexpensive and easy to use. In some applications they are ideal because they do not require a mathematical model for the plant.  
NOTE: The hardware used for PID control is also known as an operational amplifier 

The primary purpose of the PID is to keep track of its input's (<a href="https://www.codecogs.com/eqnedit.php?latex=e(t)&space;=&space;r(t)&space;-y(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(t)&space;=&space;r(t)&space;-y(t)" title="e(t) = r(t) -y(t)" /></a>) past and present values. Equipped with this knowledge, it is able to predict future values. 

If we isolate the controller portion of the block diagram and "look inside" we can understand how the control signal,  <a href="https://www.codecogs.com/eqnedit.php?latex=u(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(t)" title="u(t)" /></a> is produced. 

Three components
---
Proportional, integral, derivative components take the error, <a href="https://www.codecogs.com/eqnedit.php?latex=e(t)&space;=&space;r(t)&space;-y(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(t)&space;=&space;r(t)&space;-y(t)" title="e(t) = r(t) -y(t)" /></a> manipluates it. 

NOTE: The algrebraic sum of these components represent the control signal.

There are three parameters associated with each component that needs to be tuned by the designer in order to acheieve optimal performance and stability. 

![alt text][image3]

Controller gains
---
These are simply constants that scales to each component.

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{p}" title="k_{p}" /></a> 

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{i}" title="k_{i}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=k_{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{d}" title="k_{d}" /></a>

Setting individual gains to zero allow for the possiblitly to create combinations of controllers that can meet specific needs for a system.
For completeness, I present the explict equation for the control signal: 

<a href="https://www.codecogs.com/eqnedit.php?latex=u(t)=&space;k_{p}e(t)&plus;k_{i}\int_{0}^{T}e(\tau)d\tau&space;&plus;k_{d}\frac{\mathrm{d}&space;e(t)}{\mathrm{d}&space;x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(t)=&space;k_{p}e(t)&plus;k_{i}\int_{0}^{T}e(\tau)d\tau&space;&plus;k_{d}\frac{\mathrm{d}&space;e(t)}{\mathrm{d}&space;x}" title="u(t)= k_{p}e(t)+k_{i}\int_{0}^{T}e(\tau)d\tau +k_{d}\frac{\mathrm{d} e(t)}{\mathrm{d} x}" /></a>

To get an understanding of the types of controller combinations  available we will discuss some common ones below as they might be applied to quadcopter. 


![alt text][image4]

# P- Control

Consider an fictional quadrotor that has one of the following sensors for measuring it's altitude

* Baraometer 
* GPS 
* Ultrasonic transducer

When the drone is powered on, the pre-programmed flight path commands the motors to ascend to 10 meters, hover for 8 seconds and move north east maintaining the same altitude. 

At the very beginning of it's flight plan, the error in altitude is 
<a href="https://www.codecogs.com/eqnedit.php?latex=e(t)&space;=&space;r&space;-&space;y(t)&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(t)&space;=&space;r&space;-&space;y(t)&space;\\" title="e(t) = r - y(t) \\" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex==&space;10&space;m&space;-&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=&space;10&space;m&space;-&space;0" title="= 10 m - 0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex==&space;10&space;m" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=&space;10&space;m" title="= 10 m" /></a>

When the sensors on the drone detect the large error, it commands the motors to produce a vertical thrust that is directly proportional to the error. 

<a href="https://www.codecogs.com/eqnedit.php?latex=u(t)=k_{p}\times&space;e(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u(t)=k_{p}\times&space;e(t)" title="u(t)=k_{p}\times e(t)" /></a>

NOTE: As the quadrotor approaches the desired altitude, the error decreases and thus the controller input also decreases.

Effects on kp
---
0. As K_p increases: 
* overshoot increase
* frequency of oscillations
1. As K_p increases:
* proportional droop decreases

![alt text][image5]:

Many real-world systems are governed by second-order differential equations and exhibit a transient, oscillatory response to a step input before setting to some steady-state value. 

![alt text][image6]:

Performance parameters
---
<a href="https://www.codecogs.com/eqnedit.php?latex=T_{R}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{R}" title="T_{R}" /></a> - the rise time is the time required to move from a specified low value to a specified high value.
NOTE: Expressed as percentage of the final value i.e 0% to 100% of its final steady-state value. 

<a href="https://www.codecogs.com/eqnedit.php?latex=T_{p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{p}" title="T_{p}" /></a> - the time required to reach the first overshoot peak

<a href="https://www.codecogs.com/eqnedit.php?latex=M_{OS}=\frac{y(T_{p})-y(T_{ss})}{y(T_{ss})}&space;\times&space;100" target="_blank"><img src="https://latex.codecogs.com/gif.latex?M_{OS}=\frac{y(T_{p})-y(T_{ss})}{y(T_{ss})}&space;\times&space;100" title="M_{OS}=\frac{y(T_{p})-y(T_{ss})}{y(T_{ss})} \times 100" /></a> - the maximum percent overshoot

<a href="https://www.codecogs.com/eqnedit.php?latex=T_{s}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{s}" title="T_{s}" /></a> - the time required for the response to reach and stay within a range of the final steady-state value ( 2 to 5 % of <a href="https://www.codecogs.com/eqnedit.php?latex=y_{ss}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{ss}" title="y_{ss}" /></a>)

damping
---
A damper is any mechanism that dissipates energy usually assoicated with friction. 

* Under damped systems oscillate with greater magnitude and frequency than more heavily damped systems. 

* Critically damped system has no oscillations. 

* Over damped systems (i.e., even more damped than critically damped) also do not oscillate and their time to reach a steady-state value increases.

![alt text][image7]:

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


