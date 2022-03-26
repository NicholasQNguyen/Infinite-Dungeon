"""
Author: Nicholas Nguyen
Project 2
File: tower.py

Monster that fires based on where the archer is.
"""
from .alive import Alive
from ..FSMs.gameObjectFSM import TowerState
from .enemyProjectile import EnemyProjectile

TOWER_HP = 6
TOWER_VSPEED = 0
TOWER_CONTACT_DAMAGE = 5


class Tower(Alive):

    def __init__(self, position):
        super().__init__("range.png", position,
                         TOWER_HP)

        self._vspeed = TOWER_VSPEED

        self._state = TowerState()

        self._direction = "down"

        self._damage = TOWER_CONTACT_DAMAGE

    def fire(self, archerPosition, arrowList):
        directionVector = (archerPosition - self.getPosition()).normalize() * 5
        newArrow = EnemyProjectile(self.getPosition(), directionVector)
        arrowList.append(newArrow)
