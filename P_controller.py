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
