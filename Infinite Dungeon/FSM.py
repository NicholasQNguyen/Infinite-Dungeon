"""
Author: Nicholas Nguyen
Infinite Dungeon
File: FSM.py

Classes for the finite state machines
"""

class BasicState(object):
    def __init__(self, facing="left"):
        self._facing = facing

    def getFacing(self):
        return self._facing

    def _setFacing(self, direction):
        self._facing = direction


class ArcherState(object):
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


class SlimeState(object):
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

class GolemState(object):
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

    def manageState(self, obj, archerPosition):
        # Move the golem left or right to chase the archer
        if archerPosition[0] > obj._position[0]:
            self._movement["left"] = False
            self._movement["right"] = True
        elif archerPosition[0] < obj._position[0]:
            self._movement["right"] = False
            self._movement["left"] = True
        # Move the golem up or down to chase the archer
        if archerPosition[1] > obj._position[1]:
            if not self._movement["down"]:
                obj.transitionState("down")
            self._movement["up"] = False
            self._movement["down"] = True
        elif archerPosition[1] < obj._position[1]:
            if not self._movement["up"]:
                obj.transitionState("up")
            self._movement["down"] = False
            self._movement["up"] = True
