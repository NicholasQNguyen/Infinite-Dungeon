"""
Author: Nicholas Nguyen
Project 2
File: orb.py
"""

from drawable import Drawable
import pygame
import os
from vector2D import Vector2
from random import randint

SCREEN_SIZE = Vector2(800, 800)
WORLD_SIZE = Vector2(1200, 1200)


class Orb(Drawable):
    _dead = False

    def __init__(self):
        self._imageName = "orbs.png"
        spriteSheet = pygame.image.load(os.path.join(self._imageName))
        # use a grabberRectangle with a randint to grab a random color
        grabberRectangle = pygame.Rect(((32 * randint(0, 9)), 0, 32, 32))
        self._image = pygame.Surface((32, 32))
        self._image.blit(spriteSheet, (0, 0), grabberRectangle)

        # Set position to center of the world view
        self._position = Vector2(WORLD_SIZE[0]/2, WORLD_SIZE[1]/2)
        # Set velocity to some random Vector2 to start with
        self._velocity = Vector2(randint(1, 10), randint(1, 10))

    def update(self, worldInfo, seconds):
        """Either just updates the posiiton of the orb based on
           the velocity or switches the velocity and adds some
           randomness to the the trajectory if it hits the edge"""
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
        self.setPosition(newPosition)

    def kill(self):
        """sets _dead variable to True to indicate it's dead"""
        self._dead = True

    def isDead(self):
        """Returns a boolean of if it's dead"""
        return self._dead
