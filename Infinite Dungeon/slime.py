"""
Author: Nicholas Nguyen
Project 2
File: target.py

Basic monster that moves back and forth.
"""
from alive import Alive
from FSM import SlimeState
from vector2D import Vector2

SLIME_HP = 6
SLIME_VSPEED = 150


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

        self._vSpeed = SLIME_VSPEED

    def changeDirection(self):
        """Flip from left to right or right to left"""
        self._state.manageState()

#     def move(self, seconds):
#         """Move right for 5 seconds then left for 5 seconds"""
#         self._position[0] += self._vSpeed * seconds * self._direction

    def handleEvent(self):
        self._state.manageState()

    def update(self, seconds):
        self._velocity = Vector2(0, 0)
        currentFacing = self._state.getFacing()

        if self._state._movement["left"]:
            self._velocity[0] = -self._vSpeed
        elif self._state._movement["right"]:
            self._velocity[0] = self._vSpeed

        newPosition = self.getPosition() + self._velocity * seconds
        self.setPosition(newPosition)
