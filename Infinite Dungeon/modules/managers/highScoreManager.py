import pygame
from .basicManager import BasicManager
from ..UI.items import Text
from modules.gameObjects.vector2D import Vector2
from .highScoreFunctions import writeToCSV


class HighScoreManager(BasicManager):

    def __init__(self, screenSize, highScores, newEntry=None):
        self.message = Text(Vector2(50, 100),
                            "High Scores!",
                            "default32")
        self.scoreStrings = []
        self.scoreTexts = []

        # Insert the new entry list into the high scores list
        for i in range(len(highScores)):
            if isinstance(highScores[i], int):
                highScores[i] = newEntry
                break

        # Prob not the bets place, but write to the CSV here
        writeToCSV(highScores)

        # Convert the high scores to strings and add them to a list
        for score in highScores:
            tempString = "".join(str(score))
            self.scoreStrings.append(tempString)
        # go through the top 10 scores and render them as texts
        for i in range(10):
            self.scoreTexts.append(Text(Vector2(50, (200 + i * 50)),
                                        self.scoreStrings[i],
                                        "default32"))
        self.scoreTexts.append(Text(Vector2(50, (200 + 11 * 50)),
                                    "Press Enter to Exit",
                                    "default32"))

    def draw(self, drawSurf):
        drawSurf.fill((255, 0, 0))
        self.message.draw(drawSurf)
        for text in self.scoreTexts:
            text.draw(drawSurf)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return "mainMenu"

    def update(self):
        pass
