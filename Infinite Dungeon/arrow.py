"""
Author: Nicholas Nguyen
Final Project
File: arrow.py
"""

import pygame
import os
from vector2D import Vector2
from projectile import Projectile
from copy import deepcopy


class Arrow(Projectile):

    # 0 means horizontal, 1 means vertical
    _direction = 0
    _archer = None

    def __init__(self, archer):
        # All code to get the image and set it
        sprite = pygame.image.load(os.path.join("images", "arrow.png")).convert()
        grabberRectangle = pygame.Rect(12, 9, 8, 23)
        self._image = pygame.Surface((8, 23))
        self._image.blit(sprite, (0, 0), grabberRectangle)

        # keep a copy of the archer to track it's position
        self._archer = archer
 
        # The initial position is the location of the archer
        self._position = deepcopy(archer.getWorldPosition())
   
        # Variable used to track direction arrows fly
        self._posOrNeg = 1

    def changeDirection(self, event):
        """Function to change if the arrow is vertical or 
           horizontal based on the arrow key inputted"""
        if event.key == pygame.K_DOWN:
            self._direction = 1
            self._posOrNeg = 1
            print("DOWN")
    
        elif event.key == pygame.K_UP:
            self._direction = 1
            self._posOrNeg = -1
            print("UP")
   
        if event.key == pygame.K_LEFT:
            self._direction = 0
            self._posOrNeg = -1
            print("LEFT")   

        if event.key == pygame.K_RIGHT:
            self._direction = 0
            self._posOrNeg = 1
            print("RIGHT")   

    def draw(self, surface, offset):
        # Start it on the archer
        surface.blit(self._image, list(self._position))

    def update(self):
        self._position[self._direction] += self._velocity * self._posOrNeg
        
