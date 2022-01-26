"""
Author: Nicholas Nguyen
Final Project
File: arrow.py
"""

import pygame
import os
from projectile import Projectile


class Arrow(Projectile):

    # 0 means horizontal, 1 means vertical
    _direction = 0

    def __init__(self, initialPosition):
        # All code to get the image and set it
        sprite = pygame.image.load(os.path.join
                                   ("images", "arrow.png")).convert()
        grabberRectangle = pygame.Rect(12, 9, 8, 23)
        self._image = pygame.Surface((8, 23))
        self._image.blit(sprite, (0, 0), grabberRectangle)

        # The initial position is the location of the archer
        self._position = initialPosition

        # Variable used to track direction arrows fly
        self._posOrNeg = 1

    def changeDirection(self, event):
        """Function to change if the arrow is vertical or
           horizontal based on the arrow key inputted"""
        if event.key == pygame.K_DOWN:
            self._direction = 1
            self._posOrNeg = 1

        elif event.key == pygame.K_UP:
            self._direction = 1
            self._posOrNeg = -1

        if event.key == pygame.K_LEFT:
            self._direction = 0
            self._posOrNeg = -1

        if event.key == pygame.K_RIGHT:
            self._direction = 0
            self._posOrNeg = 1

    def draw(self, surface):
        # Shooting down
        if self._direction == 1 and self._posOrNeg == 1:
            # Start it on the archer
            surface.blit(self._image, list(self._position))

        # Shooting up
        elif self._direction == 1 and self._posOrNeg == -1:
            surface.blit(pygame.transform.rotate(self._image, 180),
                                                 list(self._position))
        # Shooting left
        elif self._direction == 0 and self._posOrNeg == -1:
            surface.blit(pygame.transform.rotate(self._image, 270),
                                                 list(self._position))

        # Shooting right
        elif self._direction == 0 and self._posOrNeg == 1:
            surface.blit(pygame.transform.rotate(self._image, 90),
                                                 list(self._position))

    def update(self):
        # Update the position based on the velocity and direction
        self._position[self._direction] += self._velocity * self._posOrNeg
