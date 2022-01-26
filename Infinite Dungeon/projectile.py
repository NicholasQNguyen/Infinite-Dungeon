"""
Author: Nicholas Nguyen
Final Project
File: projectile.py
"""

from vector2D import Vector2
from drawable import Drawable


class Projectile(Drawable):

    _isDead = False
    _position = Vector2(0, 0)
    _velocity = 5

    def __init__(self):
        None

    def fire(self, direction):
        None

    def kill(self):
        self._isDead = True

    def isDead(self):
        return self._isDead
