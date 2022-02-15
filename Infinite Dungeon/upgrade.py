"""
Author: Nicholas Nguyen
Final Project
File: upgrade.py


A class to manage upgrades.
"""

from drawable import Drawable
from vector2D import Vector2
import pygame

CENTER_OF_ROOM = Vector2(504, 504)


class Upgrade(Drawable):

    def __init__(self):
        super().__init__("Potions.png", CENTER_OF_ROOM)


class DamageUpgrade(Upgrade):

    def __init__(self):
        super().__init__()
        # Grab the red bottle for damage up
        grabberRectangle = pygame.Rect(8, 1, 17, 31)
        tempSurface = pygame.Surface((17, 31))
        tempSurface.blit(self._image, (0, 0), grabberRectangle)
        self._image = tempSurface

    def upgrade(self, arrow):
        arrow.iterateDamageLevel()


class SpeedUpgrade(Upgrade):

    def __init__(self):
        super().__init__()
        # Grab the green bottle for speed up
        grabberRectangle = pygame.Rect(40, 1, 17, 31)
        tempSurface = pygame.Surface((17, 31))
        tempSurface.blit(self._image, (0, 0), grabberRectangle)
        self._image = tempSurface

    def upgrade(self, archer):
        archer.iterateSpeedLevel()
        archer.updateVSpeed()


class ProjectileSpeedUpgrade(Upgrade):

    def __init__(self):
        super().__init__()
        # Grab the blue bottle for speed up
        grabberRectangle = pygame.Rect(72, 1, 17, 31)
        tempSurface = pygame.Surface((17, 31))
        tempSurface.blit(self._image, (0, 0), grabberRectangle)
        self._image = tempSurface

    def upgrade(self, arrow):
        """Upgrade the projectile speed level"""
        arrow.iterateSpeedLevel()
