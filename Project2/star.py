"""
Author: Nicholas Nguyen
Project 2
File: star.py
"""

from drawable import Drawable
import pygame
import os
from vector2D import Vector2
from random import randint

SCREEN_SIZE = Vector2(800, 800)
WORLD_SIZE = Vector2(1200, 1200)


class Star(Drawable):

    _maxVelocity = 1.1
    _acceleration = 0.1
    _movement = {pygame.K_DOWN: False, pygame.K_UP: False,
                 pygame.K_LEFT: False, pygame.K_RIGHT: False}

    def __init__(self):
        self._imageName = "star.png"
        self._image = pygame.image.load(os.path.join(self._imageName))
        # Set position to center of the world view
        self._position = Vector2(WORLD_SIZE[0]/2, WORLD_SIZE[1]/2)
        # Set velocity to (0,0) to start with
        self._velocity = Vector2(0, 0)

    def handleEvent(self, event):
        """Given an event, change the appropriate value in
           self._movement, if necessary."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self._movement[pygame.K_DOWN] = True

            elif event.key == pygame.K_UP:
                self._movement[pygame.K_UP] = True

            elif event.key == pygame.K_LEFT:
                self._movement[pygame.K_LEFT] = True

            elif event.key == pygame.K_RIGHT:
                self._movement[pygame.K_RIGHT] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self._movement[pygame.K_DOWN] = False

            elif event.key == pygame.K_UP:
                self._movement[pygame.K_UP] = False

            elif event.key == pygame.K_LEFT:
                self._movement[pygame.K_LEFT] = False

            elif event.key == pygame.K_RIGHT:
                self._movement[pygame.K_RIGHT] = False

    def update(self, worldInfo, seconds):
        # Change the _velocity variable
        # based on what keys are True in _movement
        for key in self._movement:
            if self._movement[key]:
                if key == pygame.K_DOWN:
                    self._velocity[1] += self._acceleration

                elif key == pygame.K_UP:
                    self._velocity[1] -= self._acceleration

                elif key == pygame.K_LEFT:
                    self._velocity[0] -= self._acceleration

                elif key == pygame.K_RIGHT:
                    self._velocity[0] += self._acceleration

        # Check if we've gone beyone the max permissable speed
        if self._velocity[0] > self._maxVelocity:
            self._velocity[0] = self._maxVelocity

        elif self._velocity[0] < -self._maxVelocity:
            self._velocity[0] = -self._maxVelocity

        if self._velocity[1] > self._maxVelocity:
            self._velocity[1] = self._maxVelocity

        elif self._velocity[1] < -self._maxVelocity:
            self._velocity[1] = -self._maxVelocity

        newPosition = self._position + self._velocity
        # We've gone beyond the borders
        if newPosition[0] < 0 or \
           (newPosition[0] + self.getWidth()) > worldInfo[0] or \
           newPosition[1] < 0 or \
           (newPosition[1] + self.getHeight()) > worldInfo[0]:

            # Add some random noise to change the angle at which it bounces
            # and a bound from (-10,10) so that the orb doesn't
            # go flying really fast all over the place
            newXVelocity = max(min(self._velocity[0] * -1 +
                                   randint(-5, 5), 10), -10)
            newYVelocity = max(min(self._velocity[1] * -1 +
                                   randint(-5, 5), 10), -10)

            self._velocity[0] = newXVelocity
            self._velocity[1] = newYVelocity

            newPosition = self._position + self._velocity

        # Whatever the case may be, set the position
        # to the new calculated position
        self._position = newPosition
