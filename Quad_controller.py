#P CONTROLLER 

#Regulates the altitude of the quadrotor

# As K_p increases, overshoot increase, frequency of oscillations
#As K_p increases, proportional droop decreases


############################################################################


class P_Controller:
	def__init__(self, kp = 0.0, start_time = 0):

		#Initialize P controller with specific kp value
		set.kp_ = float(kp)

		#create internal class variable for set_point and start_time_

		self.set_point_ = 0.0 
		self.start_time_ = start_time

		#store last timestamp
		self.last_timestamp_ = 0.0

		#Control effort history 
		self.u_p = [0]
	
	#set the altitude set point
	
	def setTarget(self, target):
		self.set_point_ = float(target)

	def setKP(self, kp):

		#set the internal kp_ value with the provided variable 
		self.kp_ = float(kp)

	def update(self, measured_value, timestamp): 
		#calculate delta_time
	
		delta_time = timestamp - self.last_timestamp_

		if delta_time == 0:
			return 0 

		#calculate the error 
		error = self.set_point_ - measured_value

		#set the last_timestamp to current_timestamp

		self.last_timestamp_ = timestamp

		#calculate the proportional error

		p = self.kp_ * error

		#set the control effort
		
		u = p 

		#store the control effort history for post control observations 
		self.u_p.append(p)
		
		return u 

############################################################
############################################################
#PI Controller

#Used to eliminate or reduce steady state error

#Increase the control input in relation to the total 
#accumulated error.

#As Ki increases : Rise time: decrease, Overshoot: increase,

#settling Time: increase, steady-state error: decrease, 

#stability: Degrade 



############################################################


class PI_controller:
	def __init__(self, kp = 0.0, ki = 0.0, start_time):
	
		#initalize kp and ki values
		self.kp_ = float(kp)
		self.ki_ = float(ki)

		#Define error sum
		self.error_sum_ = 0.0

		#Store relevant data 
	
		self.last_timestamp_ = 0.0 
		self.set_point_ = 0.0  
		self.start_time_ = start_time

		#control effort history

		self.u_p = [0] 
		self.u_i = [0] 

	def setTarget(self, target): 
		self.set_point_ = float(target)

	def setKP(self, kp):
		self.kp_ = float(kp)

	def setKI(self, ki):
		self.ki_ = ki 

	def update(self, measured_value, timestamp): 
		delta_time = timestamp - self.last_timestamp_ 
		if delta_time == 0:
			return 0
		error = self.set_point_ - measured_value 
		#set the last_timestamp_ 
		self.last_timestamp_ = timestamp

		#calculate the error_sum_

		self.error_sum_ += error * delta_time

		#calculate the proportional erro

		p = self.kp_ * error 

		i = self.ki_ * error 
		
		u = p + i 
		
		#store control history for post control observations 
		self.u_p.append(p) 
		self.u_i.append(i) 

		return u 

###################################################################################
###################################################################################

#PD Controller 




#################################################################################
		
class PD_Controller:
    
	def __init__(self, kp = 0.0, kd = 0.0, start_time = 0):
        
        
		# The PD controller can be initalized with a specific kp value
       
		# and kd value
        
		self.kp_ = float(kp)
        
		self.kd_ = float(kd)
        
        
		# Define last_error_ and set to 0.0
        
		########################################
        
		self.last_error_ = 0.0
        
		########################################

        

		# Store relevant data
        
		self.last_timestamp_ = 0.0
        
		self.set_point_ = 0.0
        
		self.start_time_ = start_time
        
		self.error_sum_ = 0.0

        

		# Control effort history
        
		self.u_p = [0]
        
		self.u_d = [0]

    
	def setTarget(self, target):
        
		self.set_point_ = float(target)

    
	def setKP(self, kp):
        
		self.kp_ = float(kp)
        
    
	def setKD(self, kd):
        
		# Set the internal kd_ value with the provided variable
        	
		########################################
        
		self.kd_ = kd
        
		########################################

    
	def update(self, measured_value, timestamp):
        
		delta_time = timestamp - self.last_timestamp_
        
		if delta_time == 0:
            
		# Delta time is zero
            
			return 0
        
        

		# Calculate the error 
        
		error = self.set_point_ - measured_value
        
        
		# Set the last_timestamp_ 
        
		self.last_timestamp_ = timestamp

        
		# Find error_sum_
        
		self.error_sum_ += error * delta_time
        
        
		# Calculate the delta_error
        
		########################################
    	    
		delta_error = error - self.last_error_
        
		########################################
        
        
		# Update the past error with the current error
        
		########################################
        
		self.last_error_ = error
        
		########################################

        
		# Proportional error
        
		p = self.kp_ * error
       
        
		# Calculate the derivative error here. Be sure to access the 
        
		# the internal Kd class variable
        
		########################################
        
		d = self.kd_ * (delta_error / delta_time)
        
		########################################
        
        
		# Set the control effort
       
		# u is the sum of all your errors. In this case it is just 
        
		# the proportional and derivative error.
        
		########################################
        
		u = p + d
        
		########################################
        
        
		# Here we are storing the control effort history for post control
        
		# observations. 
        
		self.u_p.append(p)
        
		self.u_d.append(d)

        

		return u


##########################################################################################
###########################################################################################

#PID Controller
