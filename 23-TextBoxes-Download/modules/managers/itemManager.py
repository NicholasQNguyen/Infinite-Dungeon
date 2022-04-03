from ..gameObjects.drawable import Drawable
from ..UI.displays import HoverClickMenu


class BasicItemManager(Drawable):
   """Basic ItemManager class for countable item display."""
   def __init__(self, background="", position=(0,0), parallax=0):
      super().__init__(background, position, parallax=parallax)
      self._items = {}
   
   def addItem(self, key, item):
      self._items[key] = item
   
   def updateItem(self, key, value):
      self._items[key].update(value)
   
   def increaseItem(self, key, value=1):
      self._items[key].increase(value)
   
   def decreaseItem(self, key, value=1):
      self._items[key].decrease(value)
      
   def getItemValue(self, key):
      return self._items[key].getValue()
   
   def draw(self, surface):
      for item in self._items.values():
         item.draw(surface)

