
import pygame
import os
import random
from modules.gameObjects.vector2D import Vector2
from modules.gameObjects.kirby import Kirby
from modules.gameObjects.flocker import Flocky
from modules.gameObjects.drawable import Drawable
from modules.UI.screenInfo import *


      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("FSM")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   
   kirby = Kirby(Vector2(0,0))
   flock = [Flocky(Vector2(random.randint(50, SCREEN_SIZE.x-50),random.randint(50, SCREEN_SIZE.y-50))) for x in range(20)]
   flocky = Flocky(SCREEN_SIZE // 2)
   
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
      flocky.draw(drawSurface)
      for f in flock:
          f.draw(drawSurface)
      
      pygame.transform.scale(drawSurface, list(UPSCALED), screen)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         
         kirby.handleEvent(event)
         flocky.handleEvent(event)
      
      # Update everything
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = gameClock.get_time() / 1000
      
      # let others update based on the amount of time elapsed
      kirby.update(seconds, SCREEN_SIZE)
      
      # for f in flock:
      #    f.update(seconds, flock, SCREEN_SIZE)
      flocky.update(seconds, flock, SCREEN_SIZE)
      
if __name__ == "__main__":
   main()