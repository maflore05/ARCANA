from datetime import datetime

class CEADAnalyst:
    currentUser: str
    timeOfAccess: datetime

    def __init__(self, user: str):
        self.currentUser = user
        self.timeOfAccess = datetime.now()
