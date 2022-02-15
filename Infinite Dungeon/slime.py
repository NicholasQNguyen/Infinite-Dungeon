"""
Author: Nicholas Nguyen
Project 2
File: target.py

Basic monster that moves back and forth.
"""
from alive import Alive
from FSM import SlimeState

SLIME_HP = 6


class Slime(Alive):

    def __init__(self, position):
        super().__init__("slime_monster_spritesheet.png", position, SLIME_HP)

        self._direction = 1

        self._nFrames = 2
        self._framesPerSecond = 2
        self._nFramesList = {"walking": 3}
        self._rowList = {
            "up": 0,
            "right": 1,
            "down": 2
            }

        self._framesPerSecondList = {"walking": 6}

        self._state = SlimeState()

        self._vSpeed = 50

    def changeDirection(self):
        self._direction *= -1

    def move(self, seconds):
        """Move right for 5 seconds then left for 5 seconds"""
        self._position[0] += self._vSpeed * seconds

    def handleEvent(self):
        self._state.manageState(self)
