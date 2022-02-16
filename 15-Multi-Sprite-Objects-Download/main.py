
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.kirby import Kirby
from modules.waddle import WaddleDee
from modules.drawable import Drawable


SCREEN_SIZE = Vector2(320, 240)
SCALE = 3
UPSCALED_SCREEN_SIZE = SCREEN_SIZE * SCALE

      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("FSM")
   
   screen = pygame.display.set_mode(list(UPSCALED_SCREEN_SIZE))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   
   
   
   kirby = Kirby(Vector2(50,50))
   waddles = [WaddleDee(Vector2(random.randint(50, SCREEN_SIZE.x-50),random.randint(50, SCREEN_SIZE.y-50))) for x in range(20)]
   
   
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
      for waddle in waddles:
         waddle.draw(drawSurface)
      
      pygame.transform.scale(drawSurface, list(UPSCALED_SCREEN_SIZE), screen)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
                       

         kirby.handleEvent(event)
      
      for waddle in waddles:
         waddle.think(kirby)
            
      
      # Update everything
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = gameClock.get_time() / 1000
      
      # let others update based on the amount of time elapsed
      kirby.update(seconds, SCREEN_SIZE)
      for waddle in waddles:
         waddle.update(seconds, SCREEN_SIZE)
      
if __name__ == "__main__":
   main()
