import pygame
from ..UI.entries import AbstractUIEntry
from ..managers.frameManager import FrameManager
from .drawable import Drawable


class FollowItem(object):
    def __init__(self, followObject, followOffset):
        self._follow = followObject
        self._followOffset = followOffset
        self._parallax = 1

    def update(self, seconds=0):
        self._position = self._follow.getPosition() + self._followOffset


class AbstractItem(AbstractUIEntry):
    """Abstract class for countable UI items."""
    def __init__(self, position, initialValue, maxValue, minValue=0):
        super().__init__(position)
        self._value = initialValue
        self._maxValue = maxValue
        self._minValue = minValue

    def getValue(self):
        return self._value

    def change(self, value):
        self._value = max(self._minValue, min(self._maxValue, value))
        self._render()

    def increase(self, value=1):
        self.change(self._value + value)

    def decrease(self, value=1):
        self.change(self._value - value)

    def setMax(self, value):
        self._maxValue = value
        self._render()

    def setMin(self, value):
        self._minValue = value
        self._render()

    def update(self, seconds):
        pass


class TextItem(AbstractItem):
    """Class for countable items represented by text and numerical values."""
    def __init__(self, position, text, initialValue,
                 maxValue=99, minValue=0,
                 font="default", color=(255, 255, 255)):
        super().__init__(position, initialValue, maxValue, minValue)

        self._text = text
        self._color = color
        self._font = AbstractUIEntry.FONTS[font]

        self._renderedText = self._font.render(self._text, False, self._color)

        self._render()

    def _render(self):
        valueRender = self._font.render(str(self._value), False, self._color)
        width = valueRender.get_width() + self._renderedText.get_width()
        height = valueRender.get_height() + self._renderedText.get_height()
        self._image = pygame.Surface((width, height), pygame.SRCALPHA, 32)

        self._image.blit(self._renderedText, (0, 0))
        self._image.blit(valueRender, (self._renderedText.get_width(), 0))


class FollowTextItem(TextItem, FollowItem):
    def __init__(self, followObject, followOffset,
                 position, text, initialValue,
                 maxValue=99, minValue=0,
                 font="default", color=(255, 255, 255)):
        super().__init__(position, text, initialValue,
                         maxValue, minValue, font, color)
        FollowItem.__init__(self, followObject, followOffset)

    def update(self, seconds):
        FollowItem.update(self, seconds)


class RoundedItem(TextItem):
    def __init__(self, position, text, initialValue,
                 maxValue=100, minValue=0,
                 internalFunction=lambda x: int(x),
                 font="default", color=(255, 255, 255)):
        self._internalFunction = internalFunction
        super().__init__(position, text, initialValue,
                         maxValue, minValue, font, color)

    def getValue(self):
        return self._internalFunction(self._value)


class RepeatingItem(AbstractItem):
    """Class for countable items represented by images repeating."""
    def __init__(self,
                 position,
                 imageName,
                 initialValue,
                 maxValue=5,
                 minValue=0,
                 padding=1):
        super().__init__(position, initialValue, maxValue, minValue)

        self._repeater = FrameManager.getInstance().getFrame(imageName)
        self._padding = padding

        self._image = pygame.Surface((
                                     (self._repeater.get_width() +
                                      self._padding) * maxValue,
                                     self._repeater.get_height()),
                                     pygame.SRCALPHA, 32)

        self._render()

    def _render(self):
        self._image.fill((0, 0, 0, 0))

        for i in range(0, self._value):
            self._image.blit(self._repeater,
                             ((self._repeater.get_width() + self._padding) * i,
                              0))


class RectBarItem(AbstractItem):
    """Class for countable items represented by a percentage bar."""
    def __init__(self, areaRect, initialValue, maxValue=10,
                 color=(255, 0, 0), outline=(100, 100, 100),
                 outlineWidth=2, backgroundColor=None):
        super().__init__((0, 0), initialValue, maxValue)

        self._areaRect = areaRect
        self._color = color
        self._outline = outline
        self._outlineWidth = outlineWidth
        self._backgroundColor = backgroundColor

        self._render()

    def _render(self):
        self._valueRect = pygame.Rect(self._areaRect.left,
                                      self._areaRect.top,
                                      int(self._areaRect.width *
                                          (self._value / self._maxValue)),
                                      self._areaRect.height)

    def draw(self, surface):
        drawPosition = self._position - Drawable.WINDOW_OFFSET
        if self._backgroundColor:
            pygame.draw.rect(surface, self._backgroundColor,
                             drawPosition + self._areaRect)
        pygame.draw.rect(surface, self._color, drawPosition + self._valueRect)
        pygame.draw.rect(surface,
                         self._outline,
                         drawPosition + self._areaRect,
                         self._outlineWidth)


class FollowRectBarItem(RectBarItem, FollowItem):
    def __init__(self, followObject, followOffset, areaRect,
                 initialValue, maxValue=10,
                 color=(255, 0, 0), outline=(100, 100, 100),
                 outlineWidth=2, backgroundColor=None):
        super().__init__(areaRect, initialValue, maxValue,
                         color, outline, outlineWidth, backgroundColor)
        FollowItem.__init__(self, followObject, followOffset)

    def update(self, seconds):
        FollowItem.update(self, seconds)
        self._render()
        super().update(seconds)
