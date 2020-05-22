class TotalContext(object):
    def __init__(self, user, total):
        self._total = total
        self._user = user
    
    def getTotal(self):
        return self._total
    
    def getUser(self):
        return self._user