
import pygame
import os
import math
from modules.vector2D import Vector2


SCREEN_SIZE = Vector2(300, 300)

INTERP = "linear"

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Orb Arms")
   
   screen = pygame.display.set_mode(list(SCREEN_SIZE))

   
   mousePos = Vector2(0,0)
   
   shoulder = Vector2(50,50)
   
   nOrbs = 5
   
   shoulderSize = 20
   mouseSize = 15
   
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      screen.fill((255,255,255))
      
      pygame.draw.circle(screen, pygame.Color('purple'), list(shoulder), shoulderSize)
      
      shoulderToMouse =  mousePos - shoulder
      sizeDiff = mouseSize - shoulderSize
      eachOrbDist = (mousePos - shoulder) / (nOrbs + 1)
      
      for i in range(1, nOrbs+1):
         if INTERP == "linear":
            percentage = i / (nOrbs + 1)
            pygame.draw.circle(screen, pygame.Color('darkgreen'),
                               list(map(int, shoulder + shoulderToMouse * percentage)),
                               int(shoulderSize + sizeDiff * percentage))
            
         else:
            percentage = i / (nOrbs)
            orbSize = int(20 - (5 * percentage))
            
            xCoord = int(eachOrbDist.x * i)
            
            yCoord = int(math.sin(percentage * math.pi) * shoulderToMouse.y + (shoulderToMouse.y / (nOrbs - 1)) * i)
            
            
            color = pygame.Color(int(128 + (0 - 128) * percentage),0,int(128 + (255 - 128) * percentage))
            
            pygame.draw.circle(screen, color, (xCoord + shoulder.x, yCoord + shoulder.y), orbSize)
         
         
      pygame.draw.circle(screen, pygame.Color('blue'), list(mousePos), 15)
      
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            
         # Detect WASD for movement
         elif event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(*event.pos)
            
         
         
         
            
            
   
   
if __name__ == "__main__":
   main()
