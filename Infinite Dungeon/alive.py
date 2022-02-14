"""
Author: Nicholas Nguyen
Project 2
File: alive.py

Class for things that can be dead.
"""
from mobile import Mobile


class Alive(Mobile):

    def __init__(self, imageName, position, hp):
        super().__init__(imageName, position)
        self._isDead = False
        self.HP = hp
        self.level = 1

    def takeDamage(self, damage):
        self.HP -= damage

    def kill(self):
        self._isDead = True

    def isDead(self):
        return self.HP <= 0 or self._isDead
