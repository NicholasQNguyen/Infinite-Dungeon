"""
Author: Nicholas Nguyen
Final Project
File: golem.py

Basic monster that moves back and forth.
"""
import pygame
from alive import Alive

GOLEM_HP = 20


class Golem(Alive):

    def __init__(self, position, velocity):
        super().__init__("golem-walk.png", position, velocity, GOLEM_HP)
        grabberRectangle = pygame.Rect(11, 0, 44, 60)
        tempSurface = pygame.Surface((44, 60))
        tempSurface.blit(self._image, (0, 0), grabberRectangle)
        self._image = tempSurface

    def move(self, archerPosition):
        # Move the golem left or right to chase the archer
        if archerPosition[0] > self._position[0]:
            self._position[0] += self._velocity
        elif archerPosition[0] < self._position[0]:
            self._position[0] -= self._velocity

        # Move the golem up or down to chase the archer
        if archerPosition[1] > self._position[1]:
            self._position[1] += self._velocity
        elif archerPosition[1] < self._position[1]:
            self._position[1] -= self._velocity
