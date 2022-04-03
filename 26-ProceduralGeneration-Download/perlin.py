
import pygame
import os
from modules.gameObjects.vector2D import Vector2
from modules.managers.perlinNoise import PerlinNoise



SCREEN_SIZE = Vector2(64 * 4, 64 * 4)
SCALE = 2

UPSCALED = Vector2(*[x * SCALE for x in SCREEN_SIZE])


      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Perlin Noise")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   drawSurf = pygame.Surface(list(SCREEN_SIZE))
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
   manager = PerlinNoise(SCREEN_SIZE)
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Let our game clock tick at 60 fps, ALWAYS
      gameClock.tick(60)
      
      # Draw everything
      drawSurf.fill((30,30,30))
      
      manager.draw(drawSurf)
      
      pygame.transform.scale(drawSurf, list(UPSCALED), screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         else:
            manager.handleEvent(event)
      
      # Get some time in seconds
      seconds = min(0.5, gameClock.get_time() / 1000)
      
      
      # update
      manager.update(seconds)
      
      
      
      
      
if __name__ == "__main__":
   main()
