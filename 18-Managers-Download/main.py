
import pygame
import os
from modules.managers.screenManager import ScreenManager
from modules.UI.screenInfo import SCREEN_SIZE, UPSCALED


def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Managers")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   drawSurf = pygame.Surface(list(SCREEN_SIZE))
   
   screenManager = ScreenManager()
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      
      screenManager.draw(drawSurf)
      
      pygame.transform.scale(drawSurf, list(UPSCALED), screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            break
         
         result = screenManager.handleEvent(event)
         
         if result == "exit":
            RUNNING = False
            break
            
      
      # Update everything     
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      
      # Get some time in seconds
      seconds = min(0.5, gameClock.get_time() / 1000)
      
      screenManager.update(seconds)
      
      
      
      
if __name__ == "__main__":
   main()
