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

    def __init__(self, position):
        # All code to get the image and set it
        sprite = pygame.image.load(os.path.join("images", "arrow.png")).convert()
        grabberRectangle = pygame.Rect(12, 9, 8, 23)
        self._image = pygame.Surface((8, 23))
        self._image.blit(sprite, (0, 0), grabberRectangle)

        # The initial position is the location of the archer
        self._position = position
    
    def shoot(self, event, heroPosition, surface):
        if event.key == pygame.K_DOWN:
            self._direction = 1
            print("DOWN")
    
        elif event.key == pygame.K_UP:
            print("UP")
   
        if event.key == pygame.K_LEFT:
            print("LEFT")   

        if event.key == pygame.K_RIGHT:
            print("RIGHT")   

    def draw(self, heroPosition, offset, surface):
        print(heroPosition)
        surface.blit(self._image, (150, 300))

    def update(self):
        self._position[0] += self._velocity
