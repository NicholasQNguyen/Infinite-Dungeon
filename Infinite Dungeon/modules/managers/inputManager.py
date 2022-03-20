import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2


class InputManager(BasicManager):

    def __init__(self, screenSize, newHighScore):
        self.newHighScore = newHighScore
        self.inputList = ""
        self.inputText = Text(Vector2(50, 200),
                              "Please enter your name",
                              "default32")
        self.userText = Text(Vector2(50, 300),
                             self.inputList,
                             "default32")

    def draw(self, drawSurf):
        drawSurf.fill((0, 0, 0))
        self.inputText.draw(drawSurf)
        self.userText.draw(drawSurf)

    def handleEvent(self, event):
        # https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if event.type == pygame.KEYDOWN:
            # Submit if hit enter
            if event.key == pygame.K_RETURN:
                # Make the new list of the [name, newHighScore]
                newList = [self.inputList, self.newHighScore]
                return ("submit", newList)
            # Backspace
            elif event.key == pygame.K_BACKSPACE:
                self.inputList = self.inputList[:-1]
            # Add it to the username but cap it at 16 char
            # so that the high score screen isn't bad looking
            elif len(self.inputList) < 17:
                self.inputList += event.unicode
            return (None, None)
        return (None, None)

    def update(self):
        self.userText = Text(Vector2(50, 300),
                             self.inputList,
                             "default32")
