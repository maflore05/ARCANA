

class DatabaseManager:
  eventList: list[Event]

  def __init__(self, ls_events: list[Event]) -> None:
    self.eventList = ls_events

  def writeNewEvents(self, new_events: list[Event]) -> string:
    pass

  def updateEvent(self, event: Event) -> string:
    pass

  def removeEvent(self, event: Event) -> string:
    pass

