"""
Author: Nicholas Nguyen
Final Project
File: upgrade.py


A class to manage upgrades.
"""

from .drawable import Drawable
from .vector2D import Vector2
from ..FSMs.gameObjectFSM import BasicState

CENTER_OF_ROOM = Vector2(504, 504)


class Upgrade(Drawable):

    def __init__(self, offset):
        super().__init__("Potions.png", CENTER_OF_ROOM, offset)
        self._state = BasicState()


class DamageUpgrade(Upgrade):

    def __init__(self):
        super().__init__((0, 0))
        # Grab the red bottle for damage up

    def upgrade(self, arrow):
        arrow.iterateDamageLevel()


class SpeedUpgrade(Upgrade):

    def __init__(self):
        super().__init__((1, 0))
        # Grab the green bottle for speed up

    def upgrade(self, archer):
        archer.iterateSpeedLevel()
        archer.updateVSpeed()


class ProjectileSpeedUpgrade(Upgrade):

    def __init__(self):
        super().__init__((2, 0))
        # Grab the blue bottle for speed up

    def upgrade(self, arrow):
        """Upgrade the projectile speed level"""
        arrow.iterateSpeedLevel()
