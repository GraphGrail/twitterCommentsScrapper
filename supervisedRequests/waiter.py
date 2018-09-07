import time

class Waiter:
    def __init__(self):
        self._operation = 0 # 0 - multiplication, 1 - addition
        self._delta = 2
        self._minimumWaitingTimeInSeconds = 10
        self._maximumWaitingTimeInSeconds = 3600
        
        self._currentWaitingTime = self._minimumWaitingTimeInSeconds
        
        self._verbose = 0
        
    def blocked(self):
        if self._verbose != 0:
            print("Blocking requests for " + str(self._currentWaitingTime) + " seconds.")
        time.sleep(self._currentWaitingTime)
        
        if self._operation == 0:
            self._currentWaitingTime *= self._delta
        else:
            self._currentWaitingTime += self._delta
        if self._currentWaitingTime > self._maximumWaitingTimeInSeconds:
            self._currentWaitingTime = self._maximumWaitingTimeInSeconds
            
    def passed(self):
        if self._operation == 0:
            self._currentWaitingTime =  int(self._currentWaitingTime / self._delta)
        else:
            self._currentWaitingTime =  self._currentWaitingTime - self._delta
            
        if self._currentWaitingTime < self._minimumWaitingTimeInSeconds:
            self._currentWaitingTime = self._minimumWaitingTimeInSeconds
            
    # Setters and getters:
    
    def setOperation(self, operation):
        self._operation = operation
    def getOperation(self):
        return self._operation
        
    def setDelta(self, delta):
        self._delta = delta
    def getDelta(self):
        return self._delta
    
    def setMinimumWaitingTimeInSeconds(self, minimumWaitingTimeInSeconds):
        self._minimumWaitingTimeInSeconds = minimumWaitingTimeInSeconds
    def getMinimumWaitingTimeInSeconds(self):
        return self._minimumWaitingTimeInSeconds
    
    def setMaximumWaitingTimeInSeconds(self, maximumWaitingTimeInSeconds):
        self._maximumWaitingTimeInSeconds = maximumWaitingTimeInSeconds
    def getMaximumWaitingTimeInSeconds(self):
        return self._maximumWaitingTimeInSeconds
    
    def setVerbose(self, verbose):
        self._verbose = verbose
    
    # Fields:
    
    _operation = None
    _delta = None
    
    _currentWaitingTime = None
    _minimumWaitingTimeInSeconds = None
    _maximumWaitingTimeInSeconds = None
    
    _verbose = None
    