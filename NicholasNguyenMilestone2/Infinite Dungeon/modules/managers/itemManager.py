from ..gameObjects.drawable import Drawable


class BasicItemManager(Drawable):
    """Basic ItemManager class for countable item display."""
    def __init__(self, background="", position=(0, 0)):
        super().__init__(background, position)
        self._items = {}

    def addItem(self, key, item):
        self._items[key] = item

    def changeItem(self, key, value):
        self._items[key].change(value)

    def increaseItem(self, key, value=1):
        self._items[key].increase(value)

    def decreaseItem(self, key, value=1):
        self._items[key].decrease(value)

    def getItemValue(self, key):
        return self._items[key].getValue()

    def draw(self, surface):
        if self._imageName != "":
            super().draw(surface)
        for item in self._items.values():
            item.draw(surface)

    def update(self, seconds):
        for item in self._items.values():
            item.update(seconds)
