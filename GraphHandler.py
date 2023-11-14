

class GraphHandler:
  graphValues: list[Events]

  def __init__(self, gr_vals: list[Events] = []) -> None:
    self.graphValues = gr_vals

  def getGraphInfo(self, graphID) -> string:
    pass

  def plotGraph(self) -> None:
    pass

