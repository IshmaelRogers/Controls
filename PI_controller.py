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
