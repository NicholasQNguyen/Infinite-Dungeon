"""
Author: Nicholas Nguyen
Final Project
File: projectile.py
"""

from vector2D import Vector2
from mobile import Mobile


class Projectile(Mobile):

    def __init__(self, position, velocity):
        super().__init__(position, velocity)

    def fire(self, direction):
        None

