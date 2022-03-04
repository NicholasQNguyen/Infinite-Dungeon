"""
Author: Nicholas Nguyen
Project 2
File: tower.py

Monster that moves fires based on where the archer is.
"""
from .alive import Alive

TOWER_HP = 6
TOWER_VSPEED = 0

class Tower(Alive):

    def __init__(self, position):
        super().__init__("range.png", position,
                         TOWER_HP)

        self._vspeed = TOWER_VSPEED

        self._state = TowerState()

        self._direction = "down"

    def fire(self):
        # Shooting down
        if self._direction == "down":
            # Start it on the archer
            surface.blit(self._image, list(self._position - offset))

        # Shooting up
        elif self._direction == "up":
            surface.blit(pygame.transform.rotate(self._image, 180),
                         list(self._position - offset))
        # Shooting left
        elif self._direction == "left":
            surface.blit(pygame.transform.rotate(self._image, 270),
                         list(self._position - offset))

        # Shooting right
        elif self._direction == "right":
            surface.blit(pygame.transform.rotate(self._image, 90),
                         list(self._position - offset))
