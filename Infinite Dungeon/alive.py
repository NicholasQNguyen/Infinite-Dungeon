"""
Author: Nicholas Nguyen
Project 2
File: alive.py

Class for things that can be dead.
"""
from mobile import Mobile


class Alive(Mobile):

    def __init__(self, position, velocity, imageName):
        super().__init__(position, velocity, imageName)
        self._isDead = False

    def kill(self):
        self._isDead = True

    def isDead(self):
        return self._isDead
