"""
Author: Nicholas Nguyen
Final Project
File: projectile.py
"""
from alive import Alive


class Projectile(Alive):

    def __init__(self, position, velocity, imageName):
        super().__init__(position, velocity, imageName)

    def fire(self, direction):
        None
