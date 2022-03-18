import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2


class InputManager(BasicManager):
    USER_TEXT = []

    def __init__(self, screenSize):
        self.inputText = Text(Vector2(50, 200),
                              "Please enter your name",
                              "default32")

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "submit"

    def update(self):
        return "submit"

    def draw(self, drawSurf):
        drawSurf.fill((0, 0 , 0))
        self.inputText.draw(drawSurf)
        
