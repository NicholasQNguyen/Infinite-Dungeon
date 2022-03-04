"""
Author: Nicholas Nguyen
Project 2
File: alive.py

Class for things that can be dead.
"""
from .mobile import Mobile
from ..managers.frameManager import FrameManager


class Alive(Mobile):

    def __init__(self, imageName, position, hp, offset=(0, 0)):
        super().__init__(imageName, position, offset)
        self._isDead = False
        self.HP = hp
        self.level = 1

    def takeDamage(self, damage):
        self.HP -= damage

    def getDamage(self):
        return self._damage

    def kill(self):
        self._isDead = True

    def isDead(self):
        return self.HP <= 0 or self._isDead

    def transitionState(self, state):
        self._nFrames = self._nFramesList[state]
        self._frame = 0
        self._row = self._rowList[state]
        self._framesPerSeconds = self._framesPerSecondList[state]
        self._animationTimer = 0
        self.setImage(FrameManager.getInstance().getFrame(
                      self._imageName, (self._row, self._frame)))
