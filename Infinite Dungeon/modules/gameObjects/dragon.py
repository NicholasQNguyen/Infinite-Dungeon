"""
author: nicholas nguyen
project 2
file: dragon.py

Boss that fires based on where the archer is.
"""
from .chaser import Chaser
from ..FSMs.gameObjectFSM import DragonState
from .enemyProjectile import EnemyProjectile

DRAGON_HP = 100
DRAGON_V_SPEED = 100
DRAGON_CONTACT_DAMAGE = 5


class Dragon(Chaser):

    def __init__(self, position):
        super().__init__("dragon.png", position,
                         DRAGON_HP)

        self._vspeed = DRAGON_V_SPEED

        self._nFramesList = {
            "down": 2}

        self._rowList = {
             "down": 0,
             }

        self._framesPerSecondList = {
            "down": 4}

        self._state = DragonState()

        self._direction = "down"

        self._damage = DRAGON_CONTACT_DAMAGE

    def fire(self, archerPosition, arrowList):
        directionVector = (archerPosition - self.getPosition()).normalize() * 5
        newArrow = EnemyProjectile(self.getPosition(), directionVector)
        arrowList.append(newArrow)
