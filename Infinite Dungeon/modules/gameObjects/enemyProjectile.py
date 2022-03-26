"""
Author: Nicholas Nguyen
Infinite Dungeon
File: enemyProjectile.py

Class for the enemy's projectiles
"""

from .projectile import Projectile

BASE_DAMAGE = 5
BASE_VSPEED = 250


class EnemyProjectile(Projectile):
    def __init__(self, initialPosition, directionVector):
        super().__init__("arrow.png", initialPosition, BASE_DAMAGE)
        self._vspeed = directionVector

    def update(self, seconds):
        # Update the position based on the velocity and direction
        self._position += self._vspeed
