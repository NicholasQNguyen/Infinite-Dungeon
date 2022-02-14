
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
        if self.movement["left"]:
            self._lastFacing = "left"
        elif self.movement["right"]:
            self._lastFacing = "right"
        elif self.movement["up"]:
            self._lastFacing = "up"
        elif self.movement["down"]:
            self._lastFacing = "down"

        return self._lastFacing

    def getState(self):
        return self._state

    def manageState(self, action, obj):
        if action in self.movement.keys():
            if self.movement[action] == False:
                self.movement[action] = True
                if self._state == "standing":
                    self._state = "moving"
                    obj.transitionState(self._state)

        elif action.startswith("stop") and action[4:] in self.movement.keys():
            direction = action[4:]
            if self.movement[direction]:            
                self.movement[direction] = False
                allStop = True
                for move in self.movement.keys():
                    if self.movement[move]:
                        allStop = False
                        break

                if allStop:
                    self._state = "standing"
                    obj.transitionState(self._state)

        elif action == "stopall":
            if self._state != "standing":
                for direction in self.movement.keys():
                    self.movement[direction] = False

                self._state = "standing"
                obj.transitionState(self._state)

class SlimeState(object):
    def __init__(self, state="left"):
        self._state = state
        self.movement = {         
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False
         }

        self._lastFacing = "right"

    def getFacing(self):
        if self.movement["left"]:
            self._lastFacing = "left"
        elif self.movement["right"]:
            self._lastFacing = "right"

        return self._lastFacing

    def getState(self):
        return self._state

    def manageState(self, obj):
        if self._state == "left":
            self._state = "right"
        else:
            self._state = "left"
