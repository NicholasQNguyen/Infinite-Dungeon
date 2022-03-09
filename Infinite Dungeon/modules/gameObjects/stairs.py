"""
Author: Nicholas Nguyen
Final Project
File: stairs.py

Class to handle the stairs spawn
"""
from .vector2D import Vector2
from .drawable import Drawable
from ..FSMs.gameObjectFSM import BasicState


class Stairs(Drawable):

    def __init__(self):
        self._state = BasicState()
        super().__init__("stairs.png", Vector2(504, 504), None)
