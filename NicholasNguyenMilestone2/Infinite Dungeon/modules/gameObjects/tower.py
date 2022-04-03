"""
Author: Nicholas Nguyen
Project 2
File: tower.py

Monster that moves fires based on where the archer is.
"""
from .alive import Alive
from ..FSMs.gameobjectFSM import TowerState

TOWER_HP = 6
TOWER_VSPEED = 0


class Tower(Alive):

    def __init__(self, position):
        super().__init__("range.png", position,
                         TOWER_HP)

        self._vspeed = TOWER_VSPEED

        self._state = TowerState()

        self._direction = "down"
