
import pygame
import os
import random
from vector2D import Vector2


SCREEN_SIZE = Vector2(200, 200)
SCALE = 3
UPSCALED = SCREEN_SIZE * 3

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Mouse & Upscale")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   drawSurface.fill((255, 255, 255))

   circles = []
   
   adjustedPos = [0, 0]   

   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      # Draw everything
      screen.fill((255,255,255))
      
      for circle in circles:
         pygame.draw.circle(drawSurface, *circle)
      
      pygame.transform.scale(drawSurface,list(UPSCALED), screen)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            
         elif event.type == pygame.MOUSEBUTTONDOWN:
            adjustedPos = list([int(x/SCALE) for x in event.pos])
            """circles.append((random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                            adjustedPos, 
                            random.randint(5, 20)))
            """
            circles.append(((random.randint(0,255),
                             random.randint(0,255),
                             random.randint(0,255)),
                             adjustedPos,
                             random.randint(5,20)))
   pygame.quit()
      
      
if __name__ == "__main__":
   main()
