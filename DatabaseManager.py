from Event import Event

class DatabaseManager:
    eventList: list[Event]

    def __init__(self, ls_events: list[Event]) -> None:
        self.eventList = ls_events

    def writeNewEvents(self, new_events: list[Event]) -> str:
        pass

    def updateEvent(self, event: Event) -> str:
        pass

    def removeEvent(self, event: Event) -> str:
        pass

