
class BasicState(object):
    def __init__(self, facing="none"):
        self._facing = facing

    def getFacing(self):
        return self._facing

    def _setFacing(self, direction):
        self._facing = direction


class ArcherState(object):
    def __init__(self, state="standing"):
        self._state = state
        self._movement = {         
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False
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
            if self._movement[action] == False:
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
    def __init__(self, state="left"):
        self._state = state
        self._movement = {         
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False
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
        if self._state == "left":
            self._state = "right"
        else:
            self._state = "left"
