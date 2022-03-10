"""
Author: Nicholas Nguyen
Final Project
File: rock.py

Class to handle randomly placed rocks.
"""

from .vector2D import Vector2
from .drawable import Drawable
from ..FSMs.gameObjectFSM import BasicState


class Rock(Drawable):

    def __init__(self, position):
        super().__init__("rock.png", position, None)
