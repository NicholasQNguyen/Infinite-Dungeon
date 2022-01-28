"""
Author: Nicholas Nguyen
Project 2
File: target.py

Test target for collision testing.
"""

import pygame
from alive import Alive


class Target(Alive):

    def __init__(self, position):
        super().__init__(position, 0, "rangeSmaller.png")
        tempSurface = pygame.Surface((16, 16))
        tempSurface.blit(self._image, (0, 0))
        self._image = tempSurface

        self._position = position
