
import pygame
import os
import random
from modules.gameObjects.vector2D import Vector2
from modules.gameObjects.kirby import Kirby
from modules.gameObjects.flocking import Flocky
from modules.gameObjects.drawable import Drawable
from modules.UI.screenInfo import *


      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Flocking")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   
   kirby = Kirby(Vector2(0,0))
   flock = [Flocky(Vector2(random.randint(50, SCREEN_SIZE.x-50),random.randint(50, SCREEN_SIZE.y-50))) for x in range(20)]
   
   background = Drawable("background.png", Vector2(0,0))
      
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
 
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      background.draw(drawSurface)
      kirby.draw(drawSurface)
      # flocky.draw(drawSurface)
      for f in flock:
          f.draw(drawSurface)
      
      Flocky.drawAll(drawSurface)
      
      pygame.transform.scale(drawSurface, list(UPSCALED), screen)
      
   
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            
         # Click to show the debug rings, velocity, and target position of the closest unit of the flock
         elif event.type == pygame.MOUSEBUTTONDOWN:
            nearest = flock[0]
            mousePos = adjustMousePos(event.pos)
            for f in flock[1:]:
               if (mousePos - f.getPosition()).magnitude() < (mousePos - nearest.getPosition()).magnitude():
                  nearest = f
            
            nearest.toggleDebugDraw()
            
         # Event handling for changing the distance properties of the flock
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            for f in flock:
               f.increasePersonalDistance()
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            for f in flock:
               f.decreasePersonalDistance()           
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            for f in flock:
               f.increaseSightDistance()
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            for f in flock:
               f.decreaseSightDistance()
            
         # Kirby and weight events
         else:         
            kirby.handleEvent(event)
            Flocky.handleEventWeights(event)
      
      # Update everything
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = min(0.1, gameClock.get_time() / 1000)
      
      # Update world based on the time elapsed
      kirby.update(seconds, SCREEN_SIZE)
      
      for f in flock:
          f.update(seconds, flock, kirby, SCREEN_SIZE)
      
if __name__ == "__main__":
   main()
