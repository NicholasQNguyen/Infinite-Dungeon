"""
Author: Nicholas Nguyen
Final Project
File: golem.py

Basic monster that moves back and forth.
"""
from alive import Alive

GOLEM_HP = 20
GOLEM_V_SPEED = 50


class Golem(Alive):

    def __init__(self, position):
        super().__init__("golem-walk.png", position, GOLEM_HP)

        self._vSpeed = GOLEM_V_SPEED

        self._nFramesList = {
            "moving": 5}

        self._rowList = {
            "moving": 0}

        self._framesPerSecondList = {
            "moving": 10}


    def move(self, seconds, archerPosition):
        # Move the golem left or right to chase the archer
        if archerPosition[0] > self._position[0]:
            self._position[0] += self._vSpeed * seconds
        elif archerPosition[0] < self._position[0]:
            self._position[0] -= self._vSpeed * seconds

        # Move the golem up or down to chase the archer
        if archerPosition[1] > self._position[1]:
            self._position[1] += self._vSpeed * seconds
        elif archerPosition[1] < self._position[1]:
            self._position[1] -= self._vSpeed * seconds
