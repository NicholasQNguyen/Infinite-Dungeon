class BasicState(object):
    def __init__(self, facing="right"):
        self._facing = facing

    def getFacing(self):
        return self._facing

    def _setFacing(self, direction):
        self._facing = direction
