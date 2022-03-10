"""
Author: Nicholas Nguyen
Project 2
File: mobile.py

Class for thing that can move and have a position and velocity
"""
from .animated import Animated
from .vector2D import Vector2


class Mobile(Animated):

    def __init__(self, imageName, position, offset=(0, 0)):
        super().__init__(imageName, position, offset)

    def getPosition(self):
        """Returns the Vector2 of the position"""
        return self._position

    def setPosition(self, newPosition):
        """Sets the new position"""
        self._position = newPosition

    def getX(self):
        """Returns the X position which is an int"""
        return self._position[0]

    def getY(self):
        """Returns the X position which is an int"""
        return self._position[1]

    def update(self, seconds):
        super().update(seconds)
        oldPosition = self.getPosition()
        self._velocity = Vector2(0, 0)
        if self._state.getState() != "standing":
            # currentFacing = self._state.getFacing()

            if self._state._movement["down"]:
                self._velocity[1] = self._vspeed
            elif self._state._movement["up"]:
                self._velocity[1] = -self._vspeed
            if self._state._movement["left"]:
                self._velocity[0] = -self._vspeed
            elif self._state._movement["right"]:
                self._velocity[0] = self._vspeed

            newPosition = oldPosition + self._velocity * seconds
            self.setPosition(newPosition)
            changeInPosition = newPosition - oldPosition
            # print("CHANGEINPOSITION", changeInPosition)
            return changeInPosition

        else:
            self._velocity = Vector2(0, 0)
            return Vector2(0, 0)

    # https://www.youtube.com/watch?v=Okm3-OKzWa8
    def collideBlocks(self, direction, xChange, yChange, listOfObjects):
        hits = pygame.sprite.spritecollide(self, listOfObjects, False)
        if direction == "x":
            # Moving left
            if xChange > 0:
                self.rect.x = hits[0].rect.left - self.rect.width
            # Moving right
            if xChange < 0:
                self.rect.x = hits[0].rect.right
        if direction == "y":
            # Moving up
            if yChange > 0:
                self.rect.y = hits[0].rect.top - self.rect.height
            # Moving down
            if yChange < 0:
                self.rect.y = hits[0].rect.down
