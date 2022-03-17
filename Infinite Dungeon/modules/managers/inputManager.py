import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2


class InputManager(BasicManager):
    USER_TEXT = []

    def __init__(self, screenSize):
        self.inputText = Text(Vector2(504, 700),
                              "Please enter your name"
                              "dafault16")

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            pass

    def update(self):
        return submit

    def draw(self, drawSurf):
        drawSurf.fill((255, 255, 255))
        
