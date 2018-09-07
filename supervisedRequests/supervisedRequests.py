import requests

from .waiter import Waiter

class SupervisedRequests:
    def __init__(self):
        self._waiter = Waiter()
        self._waiter.setVerbose(1)
        
        self._maxNumberOfAttempts = 10
        
        self._timeoutCodes = [408, 504, 524, 522]
        self._refusedCodes = [429, 423]
        
    def get(self, url):
        response = None
        
        currentAttemptNumber = 0
        while self._shouldContinue(currentAttemptNumber):
            try:
                response = requests.get(url)
                if response.status_code >= 400:
                    print("response.status_code == " + str(response.status_code))
                    if response.status_code in self._timeoutCodes or response.status_code in self._refusedCodes:
                        self._waiter.blocked()
                    else:
                        return None
                else:
                    self._waiter.passed()
                    return response
            except Exception as e:
                print(e)
                self._waiter.blocked()
            currentAttemptNumber += 1
            
    # Setters and getters:
    
    def setMaxNumberOfAttempts(self, maxNumberOfAttempts):
        self._maxNumberOfAttempts = maxNumberOfAttempts
    def getMaxNumberOfAttempts(self):
        return self_maxNumberOfAttempts
    
    def setWaiter(self, waiter):
        self._waiter = waiter
    def getWaiter(self):
        return self._waiter
    
    # Private functions:
    
    def _shouldContinue(self, attemptNumber):
        if self._maxNumberOfAttempts is None:
            return True
        if attemptNumber > self._maxNumberOfAttempts:
            return False
        return True
    
    # Fields:
    
    _waiter = None
    
    _maxNumberOfAttempts = None
    
    _timeoutCodes = None
    _refusedCodes = None