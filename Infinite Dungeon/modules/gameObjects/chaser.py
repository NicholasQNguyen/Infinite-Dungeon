
from .alive import Alive

class Chaser(Alive):

    def __init__(self,image, position, hp):
        super().__init__(image, position, hp)

    def whereIsTheArcherX(self, archerPosition):
        if archerPosition[0] > self._position[0]:
            return "right"
        elif archerPosition[0] < self._position[0]:
            return "left"

    def whereIsTheArcherY(self, archerPosition):
        if archerPosition[1] > self._position[1]:
            return "down"
        elif archerPosition[1] < self._position[1]:
            return "up"

    def changeDirection(self, archerPosition, stopAll=False):
        actionX = self.whereIsTheArcherX(archerPosition)
        actionY = self.whereIsTheArcherY(archerPosition)
        self._state.manageState(actionX, actionY, self, stopAll)
