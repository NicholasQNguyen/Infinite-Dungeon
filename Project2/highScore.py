"""
Author: Nicholas Nguyen
Project 2
File: highScore.py
"""
import pygame


class HighScore():
    # variable for the font string name
    _font = None
    _fontSize = 0
    _message = None
    _score = 0
    # variable for the pygame font object
    _pygameFont = None

    def __init__(self, font="Arial", fontSize=20, message="Score: 0", score=0):

        """Set some default values for the message"""
        self._font = font
        self._fontSize = fontSize
        self._message = message
        self._score = score

        # set up the surface with the message
        self._pygameFont = pygame.font.SysFont(self._font, self._fontSize)
        renderedMessage = self._pygameFont.render(
                          self._message, False,  (255, 0, 255))
        # 100 is arbitrary
        self._image = pygame.Surface((100, self._fontSize))
        self._image.blit(renderedMessage, (0, 0))

    def getScore(self):
        """Returns the score as an int"""
        return self._score

    def setScore(self, number):
        """sets the score to a specific number"""
        self._score = number

    def iterateScore(self):
        """Iterate the score by 1"""
        self._score += 1

    def getMessage(self):
        """Returns the message as a string"""
        return self._message

    def updateMessage(self):
        # Remake the message string with the new score
        self._message = "Score: " + str(self.getScore())
        # Rerender the message with the font
        renderedMessage = self._pygameFont.render(
                          self._message, False,  (255, 0, 255))
        # Slap that image on the surface!
        self._image.blit(renderedMessage, (0, 0))

    def getFont(self):
        """Returns the font as a string"""
        return self._font

    def getFontSize(self):
        """Returns the font size as an int"""
        return self._fontSize

    def getImage(self):
        """Returns the surface the score is on."""
        return self._image
