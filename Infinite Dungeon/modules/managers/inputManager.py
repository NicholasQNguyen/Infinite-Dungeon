import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2


class InputManager(BasicManager):

    def __init__(self, screenSize):
        self.inputList = ""
        self.inputText = Text(Vector2(50, 200),
                              "Please enter your name",
                              "default32")
        self.userText = Text(Vector2(50, 300),
                             self.inputList,
                             "default32")

    def draw(self, drawSurf):
        drawSurf.fill((0, 0 , 0))
        self.inputText.draw(drawSurf)
        self.userText.draw(drawSurf)

    def handleEvent(self, event):
        # https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
        if event.type == pygame.KEYDOWN:
            # Submit if hit enter
            if event.key == pygame.K_RETURN:
                return "submit"
            # Backspace
            elif event.key == pygame.K_BACKSPACE:
                self.inputList = self.inputList[:-1]
            # Add it to the username
            else:
                self.inputList += event.unicode

    def update(self):
        self.userText = Text(Vector2(50, 300),
                             self.inputList,
                             "default32")
        print(self.inputList)        
