#The following code creates an open loop controller

class Open_Controller:
    # the class initalization
    def __init__(self, start_time = 0):
        
        # Class variable to store the start time
        self.start_time_ = start_time
        
        # Class variable to store the control effort
        self.u = 0
        
        # Class variable to store the last timestamp
        self.last_timestamp_ = 0
        
        # Class variable to store our set point
        self.set_point_ = 0
        
        # Class variable to all applied control efforts!
        self.effort_applied = []

    # Set the controlled variables set point
    def setTarget(self, target):
        self.set_point_ = float(target)
     
    # Set the desired control effort   
    def setControlEffort(self, control_effort):
        self.u = float(control_effort)

    # Retrive the current control effort
    def getControlEffort(self,time):
        # Store the last time stamp!
        self.last_timestamp_ = time
        
        # Store control effort applied!
        self.effort_applied.append(self.u)
        
        return self.u
