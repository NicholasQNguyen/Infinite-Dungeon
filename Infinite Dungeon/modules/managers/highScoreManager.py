import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2


class HighScoreManager(BasicManager):

    def __init__(self, screenSize, highScores):
        self.message = Text(Vector2(50, 200),
                            "High Scores!",
                            "default32")
        self.scoreStrings = []
        self.scoreTexts = []

        # Convert the high scores to strings and add them to a list
        for score in highScores:
            tempString = "".join(str(score))
            self.scoreStrings.append(tempString)
        # go through the top 10 scores and render them as texts
        for i in range(9):
            self.scoreTexts.append(Text(Vector2(50, (300 + i * 50)),
                                        self.scoreStrings[i],
                                        "default32"))

    def draw(self, drawSurf):
        drawSurf.fill((255, 0, 0))
        self.message.draw(drawSurf)
        for text in self.scoreTexts:
            text.draw(drawSurf)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "exit"

    def update(self):
        pass
