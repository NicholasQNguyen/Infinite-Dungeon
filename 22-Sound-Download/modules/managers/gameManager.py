
from .basicManager import BasicManager
from ..gameObjects.kirby import Kirby
from ..gameObjects.drawable import Drawable
from ..gameObjects.backgrounds import *
from ..gameObjects.vector2D import Vector2
from ..gameObjects.explosion import Explosion
from ..UI.screenInfo import adjustMousePos
from .soundManager import SoundManager

from ..particleSystem.systems import RainSystem

class GameManager(BasicManager):
   
   WORLD_SIZE = Vector2(5000, 200)
   _DEBUG = True
   
   def __init__(self, screenSize):
      self._kirby = Kirby(Vector2(0,0))
      self._floor = Floor(GameManager.WORLD_SIZE.x)
      self._bg1 = EfficientBackground(screenSize, "bg1.png", parallax=0.5)
      self._bg2 = EfficientBackground(screenSize, "bg2.png", position=Vector2(50,0), parallax=0.25)
      self._staticBG = EfficientBackground(screenSize, "bg3.png", parallax=0)
      
      self._waterfallActive = False
      
      self._waterfall = RainSystem(Vector2(500,0))
      self._waterfall.setWidth(50)
      self._waterfallPosition = Vector2(475, 0)
      
      
      self._waterfallNoise = SoundManager.getInstance().playSound("rain.wav")
      SoundManager.getInstance().pauseChannel(self._waterfallNoise)
      
      self._explosions = []
      


   
   def draw(self, drawSurf):
      
      drawSurf.fill((255,0,255))
      
      # Draw everything
      self._staticBG.draw(drawSurf)
      self._bg2.draw(drawSurf)
      self._bg1.draw(drawSurf)
         
      self._floor.draw(drawSurf)
      self._kirby.draw(drawSurf)
      
      for exp in self._explosions:
         exp.draw(drawSurf)
      
      if self._waterfallActive:
         self._waterfall.draw(drawSurf)
   
   def handleEvent(self, event):
      
      if event.type == pygame.MOUSEBUTTONDOWN:
         self._explosions.append(Explosion(adjustMousePos(event.pos), self._kirby))
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
         if self._waterfallActive:
            SoundManager.getInstance().pauseChannel(self._waterfallNoise)
         else:
            SoundManager.getInstance().updateVolumePositional(self._waterfallNoise, self._kirby.getPosition(), self._waterfallPosition)
            SoundManager.getInstance().unpauseChannel(self._waterfallNoise)
         self._waterfallActive = not self._waterfallActive
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
         SoundManager.getInstance().togglePlayMusic("realizer.mp3")
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
         SoundManager.getInstance().togglePauseMusic()
               
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
      
      
      for exp in self._explosions:
         exp.update(seconds, self._kirby)
         if exp.isDead():
            self._explosions.remove(exp)
      
      if self._waterfallActive:
         
         SoundManager.getInstance().updateVolumePositional(self._waterfallNoise, self._kirby.getPosition(), self._waterfallPosition)
         self._waterfall.update(seconds) 
      
      
      Drawable.updateWindowOffset(self._kirby, screenSize, GameManager.WORLD_SIZE)
      
      
   def updateMovement(self):
      self._kirby.updateMovement()
