"""
Author: Nicholas Nguyen
Final Project
File: golem.py

Monster that follows the player
"""
from alive import Alive
from FSM import GolemState
from frameManager import FrameManager

GOLEM_HP = 20
GOLEM_V_SPEED = 100


class Golem(Alive):

    def __init__(self, position):
        super().__init__("golem-walk.png", position, GOLEM_HP)

        self._vspeed = GOLEM_V_SPEED

        self._nFramesList = {
            "up": 5,
            "left": 5,
            "down": 5,
            "right": 5}

        self._rowList = {
             "up": 0,
            "left": 1,
            "down": 2,
            "right": 3}
        self._framesPerSecondList = {
            "up": 10,
            "left": 10,
            "down": 10,
            "right": 10}

        self._state = GolemState()

    def changeDirection(self, obj, archerPosition):
        self._state.manageState(obj, archerPosition)

    def transitionState(self, state):
        self._nFrames = self._nFramesList[state]
        self._frame = 0
        self._row = self._rowList[state]
        self._framesPerSecond = self._framesPerSecondList[state]
        self._animationTimer = 0
        self.setImage(FrameManager.getInstance().getFrame(self._imageName, (self._row, self._frame)))
