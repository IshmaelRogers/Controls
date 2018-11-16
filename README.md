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
[image7]: ./images/typesofoscillations.png
[image8]: ./images/PV&SP.png
[image9]: ./images/contvsdisc.png
[image10]: ./images/rectangles.png

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
1. As K_p decreases:
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

When there are strict design requirments on the amount of steady-state error (SSE) that is tolerable, the P controller in not enough. In general the PI controller is necessary to eliminate or reduce the SSE. Addin the integral gain can smooth certain types of noise. Similiar to the proportional gain, it is not possible to make the integral gain randomly large with consequences. 

Note: If <a href="https://www.codecogs.com/eqnedit.php?latex=k_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k_{i}" title="k_{i}" /></a> is too large, the overcompensation of the error can cause the oscillations to increase in magnitude i.e increased instability. 

We increase the control input in relation to the total accumulated error. Simply put, the integral controller takes into consideration all the past system error values. Thus, even small errors will eventually be amplified and cause the controller to increase its input to the plant. 

![alt text][image8]:

 PV = Process Variable (measured output)
 SP = Set Point (reference signal) 
 
Implementing the continuous time controller equation on a computer
-- 
The graphs below compares how a computer interperts a mobile robot's varying speed as it accelerates to its desired destination. The image at the top is an example of how humans perceive the graph (continuously). The image at the bottom is an example of how computer perceive the graphs, (discretely). 
NOTE: The computer only "see" the samples at periodic intervals usually defined by a sampling rate. Therefore, discrete-time approximations are needed for both integral and derivatives.

![alt text][image9]: 

The Integral
---
In calculus the integral represents the area under a curve. In discrete-time sceniaros, this can be approximated as simply summing rectangles. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{0}^{t}e(\tau)d\tau&space;\approx&space;\sum_{k=1}^{n}e_{k}\Delta&space;t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{0}^{t}e(\tau)d\tau&space;\approx&space;\sum_{k=1}^{n}e_{k}\Delta&space;t" title="\int_{0}^{t}e(\tau)d\tau \approx \sum_{k=1}^{n}e_{k}\Delta t" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=e_{k}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_{k}" title="e_{k}" /></a> - the error at each point (i.e the height of the rectangle)

<a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;t" title="\Delta t" /></a> - the time interval (i.e the width of the rectangle) 

![alt text][image10]

NOTE: At each new time-step, the computer program should compute the new error and add it to the accumulated sum.
<a href="https://www.codecogs.com/eqnedit.php?latex=E_{k}=&space;E_{k-1}&space;&plus;&space;e_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{k}=&space;E_{k-1}&space;&plus;&space;e_k" title="E_{k}= E_{k-1} + e_k" /></a>

Effects of ki
---
As Ki increases: 
* Rise time: Decrease
* Overshoot: Increase
* Settling Time: Increase
* Steady-state error: ecrease 
* Stability: Degrade 

Adding the integral gain allowed us to minimize the SSE but increase the settling time and percent overshoot. 

# PD- Control

The derivative term attempts to predict what the error will be by linearly extrapolating the change in error value. When the system takes into an account the rate of change in error, it can approach the setpoint much more elegantly and rapidly. 

NOTE: All this means that it looks to future values. 
NOTE: The finite difference approximation of the derivative is the slope of the tangent line

Single-step backwards difference formula
---
The derivative of a function is the slope of the tangent line evaluated at a particular point. We can approximate the slow with the following formula

<a href="https://www.codecogs.com/eqnedit.php?latex={f}'(x_{k})\approx&space;\frac{f(x_{k})-f(x_{k-1})}{\Delta&space;t}\Rightarrow&space;\frac{e_{k}-e_{k-1}}{\Delta&space;t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{f}'(x_{k})\approx&space;\frac{f(x_{k})-f(x_{k-1})}{\Delta&space;t}\Rightarrow&space;\frac{e_{k}-e_{k-1}}{\Delta&space;t}" title="{f}'(x_{k})\approx \frac{f(x_{k})-f(x_{k-1})}{\Delta t}\Rightarrow \frac{e_{k}-e_{k-1}}{\Delta t}" /></a>

Effects on kd
---
As kd increases:
Overshoot: Decreases


# PID - Control 

# Limitations

# Real life case - Integrator Windup

# Real life case - Noise

# Control Design Objective and Criteria 

# Tuning Strategies 

# Combine Concepts

# Project: Quadrotor Control using PID 


