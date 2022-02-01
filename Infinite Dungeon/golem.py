"""
Author: Nicholas Nguyen
Final Project
File: golem.py

Basic monster that moves back and forth.
"""
import pygame
from alive import Alive


class Golem(Alive):

    def __init__(self, position, velocity):
        super().__init__(position, velocity, "golem-walk.png")
        grabberRectangle = pygame.Rect(11, 0, 44, 60) 
        tempSurface = pygame.Surface((44, 60))
        tempSurface.blit(self._image, (0, 0), grabberRectangle)
        self._image = tempSurface

    def move(self, archerPosition):
        if self._position 
