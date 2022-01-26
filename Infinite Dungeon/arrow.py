"""
Author: Nicholas Nguyen
Final Project
File: arrow.py
"""

import pygame
import os
from vector2D import Vector2
from projectile import Projectile


class Arrow(Projectile):

    # 0 means horizontal, 1 means vertical
    _direction = 0
    _archer = None

    def __init__(self, position, archer):
        # All code to get the image and set it
        sprite = pygame.image.load(os.path.join("images", "arrow.png")).convert()
        grabberRectangle = pygame.Rect(12, 9, 8, 23)
        self._image = pygame.Surface((8, 23))
        self._image.blit(sprite, (0, 0), grabberRectangle)

        # The initial position is the location of the archer
        self._position = position
   
        # keep a copy of the archer to track it's position
        self._archer = archer
 
    def changeDirection(self, event):
        """Function to change if the arrow is vertical or 
           horizontal based on the arrow key inputted"""
        if event.key == pygame.K_DOWN:
            self._direction = 1
            print("DOWN")
    
        elif event.key == pygame.K_UP:
            self._direction = 1
            print("UP")
   
        if event.key == pygame.K_LEFT:
            self._direction = 0
            print("LEFT")   

        if event.key == pygame.K_RIGHT:
            self._direction = 0
            print("RIGHT")   

    def draw(self, surface, offset):
        surface.blit(self._image, list(self._position - self._archer.getWorldPosition()))

    def update(self):
        self._position[self._direction] += self._velocity
        
