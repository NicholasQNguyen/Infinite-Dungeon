
from .basicManager import BasicManager
from ..gameObjects.kirby import Kirby
from ..gameObjects.drawable import Drawable
from ..gameObjects.backgrounds import *
from ..gameObjects.vector2D import Vector2
from ..gameObjects.explosion import Explosion
from ..gameObjects.tree import Tree
from ..UI.screenInfo import adjustMousePos
from .soundManager import SoundManager
from ..particleSystem.systems import RainSystem

import random

class GameManager(BasicManager):
   
   WORLD_SIZE = Vector2(5000, 200)
   _DEBUG = True
   
   def __init__(self, screenSize):
      self._kirby = Kirby(Vector2(0,0))
      self._floor = Floor(GameManager.WORLD_SIZE.x)
      self._bg1 = EfficientBackground(screenSize, "bg1.png", parallax=0.5)
      self._bg2 = EfficientBackground(screenSize, "bg2.png", position=Vector2(50,0), parallax=0.25)
      self._staticBG = EfficientBackground(screenSize, "bg3.png", parallax=0)
      
      self._trees = [Tree(Vector2(random.randint(0, GameManager.WORLD_SIZE.x-200), GameManager.WORLD_SIZE.y - 225)) for x in range(20)]


   
   def draw(self, drawSurf):
      
      drawSurf.fill((255,0,255))
      
      # Draw everything
      self._staticBG.draw(drawSurf)
      self._bg2.draw(drawSurf)
      self._bg1.draw(drawSurf)
         
      self._floor.draw(drawSurf)
      self._kirby.draw(drawSurf)
      
      for tree in self._trees:
         tree.draw(drawSurf)
      
   
   def handleEvent(self, event):
      
               
      self._kirby.handleEvent(event)
   
   
   def update(self, seconds, screenSize):
      clipRect = self._kirby.getCollisionRect().clip(self._floor.getCollisionRect())
         
      if clipRect.width > 0:
         self._kirby.collideGround(clipRect.height)
         
      
      # let others update based on the amount of time elapsed
      
      status = self._kirby.update(seconds, GameManager.WORLD_SIZE)
      if status:
         return status
      self._bg2.update()
      self._bg1.update()
      
      
      
      Drawable.updateWindowOffset(self._kirby, screenSize, GameManager.WORLD_SIZE)
      
      
   def updateMovement(self):
      self._kirby.updateMovement()