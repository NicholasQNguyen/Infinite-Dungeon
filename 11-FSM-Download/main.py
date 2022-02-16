
import pygame
import os
from modules.vector2D import Vector2
from modules.kirby import Kirby
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
   
   

   kirby = Kirby(Vector2(0,0))
   
   background = Drawable("background.png", Vector2(0,0))
   water = Drawable("water.png", Vector2(0,120))
   
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      background.draw(drawSurface)
      water.draw(drawSurface)
      kirby.draw(drawSurface)
      
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
            
      
      # Update everything
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = gameClock.get_time() / 1000
      
      if kirby.getCollisionRect().colliderect(water.getCollisionRect()):
         kirby.collide(water)
      else:
         kirby.collide(None)

      # let others update based on the amount of time elapsed
      kirby.update(seconds)
      
if __name__ == "__main__":
   main()
