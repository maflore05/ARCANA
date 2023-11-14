from datetime import datetime

class CEADAnalyst:
  currentUser: string = ""
  timeOfAccess: time = datetime()

  def __init__(self, user: string):
    self.currentUser = user


