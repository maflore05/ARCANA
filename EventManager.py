from Event import Event

class EventManager:
    events: list[Event] = []

    def __init__(self, init_events: list[Event] = []):
        self.events = init_events

    def editEvent(self, edit: str) -> None:
        pass

    def searchEvent(self, key: str) -> Event:
        pass

    def deleteEvent(self, event: Event) -> None:
        pass
