
from .basicManager import BasicManager
from ..gameObjects.kirby import Kirby
from ..gameObjects.drawable import Drawable
from ..gameObjects.backgrounds import *
from ..gameObjects.vector2D import Vector2
from .itemManager import BasicItemManager
from ..gameObjects.items import *
from ..gameObjects.goal import Goal
import json
import time, threading


class GameManager(BasicManager):

   def __init__(self, screenSize, loadFile):
      
      self._loadFile = loadFile
      self._screenSize = screenSize
      
   def load(self):
      filePtr = open(os.path.join("resources", "levels", self._loadFile))      
      info = json.load(filePtr)
      filePtr.close()
      
      self._worldSize = Vector2(*info["worldSize"])
      self._kirby = Kirby(Vector2(*info["start"]))
      self._floor = Floor(self._worldSize.x)
      self._bg1 = EfficientBackground(self._screenSize, "bg1.png", parallax=0.5)
      self._bg2 = EfficientBackground(self._screenSize, "bg2.png", position=Vector2(50,0), parallax=0.25)
      self._staticBG = EfficientBackground(self._screenSize, "bg3.png", parallax=0)
      
      self._goal = Goal(Vector2(*info["goal"]))
      
      
      self._HUD = BasicItemManager()
            
      self._HUD.addItem("time", RoundedItem((130,10), "Time: ", info["time"], font="default8"))

      
   
   def draw(self, drawSurf):
      
      drawSurf.fill((255,0,255))
      
      # Draw everything
      self._staticBG.draw(drawSurf)
      self._bg2.draw(drawSurf)
      self._bg1.draw(drawSurf)
         
      self._floor.draw(drawSurf)
      self._kirby.draw(drawSurf)
      self._goal.draw(drawSurf)
      
   
      self._HUD.draw(drawSurf)
   
   def handleEvent(self, event):
      
      
               
      self._kirby.handleEvent(event)
   
   
   def update(self, seconds, screenSize):
      clipRect = self._kirby.getCollisionRect().clip(self._floor.getCollisionRect())
         
      if clipRect.width > 0:
         self._kirby.collideGround(clipRect.height)
         
      
      # let others update based on the amount of time elapsed
      
      status = self._kirby.update(seconds, self._worldSize)
      if status:
         return status
   
      if self._kirby.getCollisionRect().colliderect(self._goal.getCollisionRect()):
         return "nextLevel"
      self._bg2.update()
      self._bg1.update()
      
      self._HUD.decreaseItem("time", seconds)
      if self._HUD.getItemValue("time") <= 0:
         return "dead"
      
      Drawable.updateWindowOffset(self._kirby, screenSize, self._worldSize)
      
      
   def updateMovement(self):
      self._kirby.updateMovement()



class GameManagerThreaded(GameManager):
   
   def __init__(self, screenSize, loadFile):
      super().__init__(screenSize, loadFile)
      
      self._loaded = False
      
   
   def load(self):
      self._loaded = False
      self._loadingThread = threading.Thread(target=self._loadAssets)
      self._loadingThread.start()
      
      
   def _loadAssets(self):
      super().load()
      time.sleep(2) # Artificially inflate loading time, remove this for your actual game!
      self._loaded = True
   
   def isLoaded(self):
      return self._loaded

   def updateMovement(self):
      if self.isLoaded():
         super().updateMovement()
      
