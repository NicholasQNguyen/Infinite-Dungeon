"""
Author: Nicholas Nguyen
Final Project
File: projectile.py

Class for all projectiles with a hitbox enemy or friendly
"""
from .alive import Alive

HEALTH = 1


class Projectile(Alive):

    def __init__(self, imageName, position, damage):
        super().__init__(imageName, position, HEALTH)
        self.damage = damage * self.level

    def fire(self, direction):
        None

    def getDamage(self):
        return self.damage
