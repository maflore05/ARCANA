

class Node:
    coordinates: tuple[int,int]

    def __init__(self, coord: tuple[int,int] = (0,0)) -> None:
        self.coordinates = coord

    def getCoordinates(self) -> tuple[int,int]:
        return self.coordinates
