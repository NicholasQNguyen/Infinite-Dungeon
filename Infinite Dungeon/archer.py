"""
Author: Nicholas Nguyen
Infinite Dungeon
File: archer.py

Class for the player character
"""
import pygame
from alive import Alive
from FSM import ArcherState
from frameManager import FrameManager

ARCHER_HP = 50
ARCHER_VELOCITY = 4
ARCHER_V_SPEED = 50


class Archer(Alive):

    def __init__(self, position):
        super().__init__("archer.png", position, ARCHER_HP)

        self._nFrames = 4

        self.speedLevel = 0

        self._vspeed = ARCHER_V_SPEED

        self._nFramesList = {
            "moving": 5,
            "standing": 1}

        self._rowList = {
            "moving": 0,
            "standing": 1}

        self._framesPerSecondList = {
            "moving": 10,
            "standing": 1}

        self._state = ArcherState()

    def handleEvent(self, event):
        """Given an event, change the appropriate value in
           self._movement, if necessary."""
        if event.type == pygame.KEYDOWN:
            if event.key == event.key == ord("s"):
                self._state.manageState("down", self)

            elif event.key == event.key == ord("w"):
                self._state.manageState("up", self)

            elif event.key == event.key == ord("a"):
                self._state.manageState("left", self)

            elif event.key == event.key == ord("d"):
                self._state.manageState("right", self)

        elif event.type == pygame.KEYUP:
            if event.key == ord("s"):
                self._state.manageState("stopdown", self)

            elif event.key == ord("w"):
                self._state.manageState("stopup", self)

            elif event.key == ord("a"):
                self._state.manageState("stopleft", self)

            elif event.key == ord("d"):
                self._state.manageState("stopright", self)

    def getNewDoor(self):
        return self._newDoor

    def setNewDoor(self, door):
        self._newDoor = door

    def iterateSpeedLevel(self):
        self.speedLevel += 1

    def updateVSpeed(self):
        self._vSpeed = self._vSpeed + self.speedLevel

    def transitionState(self, state):
        self._nFrames = self._nFramesList[state]
        self._frame = 0
        self._row = self._rowList[state]
        self._framesPerSeconds = self._framesPerSecondList[state]
        self._animationTimer = 0
        self.setImage(FrameManager.getInstance().getFrame(
                      self._imageName, (self._row, self._frame)))
