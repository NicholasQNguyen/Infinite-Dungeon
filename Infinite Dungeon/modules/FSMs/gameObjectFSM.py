"""
Author: Nicholas Nguyen
Infinite Dungeon
File: FSM.py

Classes for the finite state machines
"""
from .basicFSM import BasicState


class ArcherState(BasicState):

    def __init__(self, state="standing"):
        self._state = state
        self._movement = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
         }

        self._lastFacing = "right"

    def getFacing(self):
        if self._movement["left"]:
            self._lastFacing = "left"
        elif self._movement["right"]:
            self._lastFacing = "right"
        elif self._movement["up"]:
            self._lastFacing = "up"
        elif self._movement["down"]:
            self._lastFacing = "down"

        return self._lastFacing

    def getState(self):
        return self._state

    def manageState(self, action, obj):
        if action in self._movement.keys():
            if self._movement[action] is False:
                self._movement[action] = True
                if self._state == "standing":
                    self._state = "moving"
                    obj.transitionState(self._state)

        elif action.startswith("stop") and action[4:] in self._movement.keys():
            direction = action[4:]
            if self._movement[direction]:
                self._movement[direction] = False
                allStop = True
                for move in self._movement.keys():
                    if self._movement[move]:
                        allStop = False
                        break

                if allStop:
                    self._state = "standing"
                    obj.transitionState(self._state)

        elif action == "stopall":
            if self._state != "standing":
                for direction in self._movement.keys():
                    self._movement[direction] = False

                self._state = "standing"
                obj.transitionState(self._state)


class SlimeState(BasicState):

    def __init__(self, state="right"):
        self._state = state
        self._movement = {
            "up": False,
            "down": False,
            "left": False,
            "right": True
         }

        self._lastFacing = "right"

    def getFacing(self):
        if self._movement["left"]:
            self._lastFacing = "left"
        elif self._movement["right"]:
            self._lastFacing = "right"

        return self._lastFacing

    def getState(self):
        return self._state

    def manageState(self, obj):
        """Flip the direction of the movement"""
        self._movement["left"] = not self._movement["left"]
        self._movement["right"] = not self._movement["right"]


class GolemState(BasicState):

    def __init__(self, state="left"):
        self._state = state
        self._movement = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
         }

        self._lastFacing = "left"

    def getFacing(self):
        if self._movement["left"]:
            self._lastFacing = "left"
        elif self._movement["right"]:
            self._lastFacing = "right"
        elif self._movement["up"]:
            self._lastFacing = "up"
        elif self._movement["down"]:
            self._lastFacing = "down"

        return self._lastFacing

    def getState(self):
        return self._state

    def manageState(self, X, Y, obj, stopAll):
        if stopAll:
            if self._state != "standing":
                self._state = "standing"
                for direction in self._movement.keys():
                    self._movement[direction] = False

                obj.transitionState(self._state)

        else:
            if X in self._movement.keys():
                if X == "right":
                    self._movement["right"] = True
                    self._movement["left"] = False
                else:
                    self._movement["right"] = False
                    self._movement["left"] = True

            if Y in self._movement.keys():
                if self._state == "standing":
                    self._state = "down"
                    obj.transitionState(self._state)

                if Y == "up":
                    self._movement["up"] = True
                    self._movement["down"] = False
                else:
                    self._movement["up"] = False
                    self._movement["down"] = True


class TowerState(BasicState):

    def __init__(self, state="standing"):
        self._state = state
        self._lastFacing = "down"

    def getFacing(self):
        self._lastFacing = "down"


class DragonState(BasicState):

    def __init__(self, state="up"):
        self._state = state
        self._movement = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
         }

        self._lastFacing = "down"

    def getFacing(self):
        return "down"

    def getState(self):
        return self._state

    def manageState(self, X, Y, obj, stopAll):
        if stopAll:
            if self._state != "up":
                self._state = "up"
                for direction in self._movement.keys():
                    self._movement[direction] = False

                obj.transitionState(self._state)

        else:
            if X in self._movement.keys():
                if X == "right":
                    self._movement["right"] = True
                    self._movement["left"] = False
                else:
                    self._movement["right"] = False
                    self._movement["left"] = True

            if Y in self._movement.keys():
                if self._state == "standing":
                    self._state = "up"

                if Y == "up":
                    self._movement["up"] = True
                    self._movement["down"] = False
                else:
                    self._movement["up"] = False
                    self._movement["down"] = True
