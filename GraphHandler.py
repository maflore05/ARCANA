from Event import Event

class GraphHandler:
    graphValues: list[Event]

    def __init__(self, gr_vals: list[Event] = []) -> None:
        self.graphValues = gr_vals

    def getGraphInfo(self, graphID) -> str:
        pass

    def plotGraph(self) -> None:
        pass

