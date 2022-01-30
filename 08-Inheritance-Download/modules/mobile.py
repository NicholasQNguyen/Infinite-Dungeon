import pygame
import os
from modules.vector2D import Vector2
from .drawable import Drawable

class Mobile(Drawable):
    def __init__(self, imageName, position):
        super().__init__(imageName, position)
        self.speed = 500
        self._velocity = Vector2(0,0)
 
    def update(self, ticks):
      
        newPosition = self.getPosition() + self._velocity * ticks
      
        self.setPosition(newPosition)
 
    
