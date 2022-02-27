"""
Author: Nicholas Nguyen
Project 2
File: target.py

Basic monster that moves back and forth.
"""
from .alive import Alive
from ..FSMs.gameObjectFSM import SlimeState

SLIME_HP = 6
SLIME_VSPEED = 150


class Slime(Alive):

    def __init__(self, position):
        super().__init__("slime_monster_spritesheet.png", position,
                         SLIME_HP, (0, 1))

        self._vspeed = SLIME_VSPEED

        self._nFramesList = {"moving": 3}
        self._rowList = {"moving": 2}
        self._framesPerSecondList = {"moving": 6}

        self._state = SlimeState()

    def changeDirection(self):
        """Flip from left to right or right to left"""
        self._state.manageState(self)

    def handleEvent(self):
        self._state.manageState(self)
