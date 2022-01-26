"""
Author: Nicholas Nguyen
Infinite Dungeon
File: archer.py
"""

import pygame
import os
from vector2D import Vector2
from drawable import Drawable
from alive import Alive

class Archer(Alive):
    _movement = {pygame.K_DOWN: False, pygame.K_UP: False,
                 pygame.K_LEFT: False, pygame.K_RIGHT: False}
    _position = Vector2(0, 0)
    _velocity = 4
    _image = pygame.Surface((25, 30))

    def __init__(self, position, velocity, imageName):
        super().__init__(position, velocity, imageName)
        tempSurface = pygame.Surface((25, 30))
        spriteSheet = pygame.image.load(os.path.join(
                                                "images",
                                                "archer.png")).convert_alpha()
        # Rectangle specifically for the germanic archer png
        grabberRectangle = pygame.Rect(24, 20, 50, 50)
        tempSurface.blit(spriteSheet, (0, 0), grabberRectangle)
        self._image = tempSurface

    def handleEvent(self, event):
        """Given an event, change the appropriate value in
           self._movement, if necessary."""
        if event.type == pygame.KEYDOWN:
            if event.key == event.key == ord("s"):
                self._movement[pygame.K_DOWN] = True

            elif event.key == event.key == ord("w"):
                self._movement[pygame.K_UP] = True

            elif event.key == event.key == ord("a"):
                self._movement[pygame.K_LEFT] = True

            elif event.key == event.key == ord("d"):
                self._movement[pygame.K_RIGHT] = True

        elif event.type == pygame.KEYUP:
            if event.key == ord("s"):
                self._movement[pygame.K_DOWN] = False

            elif event.key == ord("w"):
                self._movement[pygame.K_UP] = False

            elif event.key == ord("a"):
                self._movement[pygame.K_LEFT] = False

            elif event.key == ord("d"):
                self._movement[pygame.K_RIGHT] = False

    def update(self):
        # Change the position
        # based on what keys are True in _movement
        for key in self._movement:
            if self._movement[key]:
                if key == pygame.K_DOWN:
                    self._position[1] += self._velocity

                elif key == pygame.K_UP:
                    self._position[1] -= self._velocity

                elif key == pygame.K_LEFT:
                    self._position[0] -= self._velocity

                elif key == pygame.K_RIGHT:
                    self._position[0] += self._velocity
