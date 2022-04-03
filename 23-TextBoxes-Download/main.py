
import pygame
import os
# from modules.utils.vector2D import Vector2
from modules.gameObjects.backgrounds import *
from modules.UI.textBox import *
# from modules.utils.drawable import Drawable
from modules.UI.screenInfo import SCREEN_SIZE, UPSCALED


def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Textboxes")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   drawSurf = pygame.Surface(list(SCREEN_SIZE))
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   staticBG = RepeatingSprite(SCREEN_SIZE, "background.png", (0,0), None, 0)
   
   TEXTS = TextManager.getInstance()
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      
      # Draw everything
      drawSurf.fill((30,30,30))
      staticBG.draw(drawSurf)
      
      TEXTS.draw(drawSurf)
      
      pygame.transform.scale(drawSurf, list(UPSCALED), screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         elif event.type == pygame.KEYDOWN and event.key in [pygame.K_0, pygame.K_1, pygame.K_3]:
            TEXTS.showBox(pygame.key.name(event.key))
         else:            
            TEXTS.handleEvent(event)
            
      
      # Get some time in seconds
      seconds = min(0.5, gameClock.get_time() / 1000)
      
   pygame.quit()
      
      
      
if __name__ == "__main__":
   main()
