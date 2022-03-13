"""
Author: Nicholas Nguyen
Infinite Dungeon
File: archer.py

Class for the player character
"""
import pygame

from .alive import Alive
from .items import FollowRectBarItem
from .vector2D import Vector2

from ..FSMs.gameObjectFSM import ArcherState
from ..managers.frameManager import FrameManager
from ..managers.itemManager import BasicItemManager


ARCHER_HP = 50
# ARCHER_V_SPEED = 150
ARCHER_V_SPEED = 550


# TODO Make a singleton
class Archer(Alive):

    def __init__(self, position):
        super().__init__("archer.png", position, ARCHER_HP)

        self._stats = BasicItemManager()
        self._stats.addItem("HP", FollowRectBarItem(self,
                                                    Vector2(0, -50),
                                                    pygame.Rect(0, 50, 55, 10),
                                                    outlineWidth=1,
                                                    initialValue=self.HP * 100,
                                                    maxValue=self.HP * 100,
                                                    backgroundColor=(0, 0, 0)))

        self.speedLevel = 0
        self._vspeed = ARCHER_V_SPEED

        self._nFrames = 4
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

    def update(self, damage, seconds):
        change = super().update(seconds)
        self._stats.decreaseItem("HP", damage * 100)
        self._stats.update(seconds)
        return(change)

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
        self.speedLevel += 15

    def updateVSpeed(self):
        self._vspeed = self._vspeed + self.speedLevel

    def transitionState(self, state):
        self._nFrames = self._nFramesList[state]
        self._frame = 0
        self._row = self._rowList[state]
        self._framesPerSeconds = self._framesPerSecondList[state]
        self._animationTimer = 0
        self.setImage(FrameManager.getInstance().getFrame(
                      self._imageName, (self._row, self._frame)))

    def updateMovement(self):
        # For unpausing the game
        pressed = pygame.key.get_pressed()

        if not pressed[pygame.K_UP]:
            self._state.manageState("stopup", self)
        if not pressed[pygame.K_DOWN]:
            self._state.manageState("stopdown", self)
        if not pressed[pygame.K_LEFT]:
            self._state.manageState("stopleft", self)
        if not pressed[pygame.K_RIGHT]:
            self._state.manageState("stopright", self)

    def drawStats(self, drawSurf):
        self._stats.draw(drawSurf)

    def getStats(self):
        return self._stats
