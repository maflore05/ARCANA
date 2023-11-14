
class EventManager:
  events: list[Events] = []

  def __init__(self, init_events: list[Events] = []):
    self.events = init_events

  def editEvent(self, edit: string) -> None:
    pass

  def searchEvent(self, key: string) -> Event:
    pass

  def deleteEvent(self, event: Event) -> None:
    pass

