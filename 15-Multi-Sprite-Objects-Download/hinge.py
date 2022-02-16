
import pygame
import os
import math
from modules.vector2D import Vector2
from modules.rotated import Rotatable

SCREEN_SIZE =Vector2(800, 800)


def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Hinge Joint")
   
   screen = pygame.display.set_mode(list(SCREEN_SIZE))
   
   arm = Rotatable("bar-purple.png", SCREEN_SIZE // 2 - Vector2(64, 8))
   
   arm.setPivot(Vector2(16,16))
   
   forearm = Rotatable("bar-blue.png", Vector2(0,0))
   forearm.setPivot(Vector2(16,16))
   
   connection = Vector2(128-16,16)
   
   armChoice = 0
   
   arms = [arm, forearm]
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      forearm.setPivotPosition(arm.getHiddenPosition() + arm.getRotatedPivot(connection))
      
      # Draw everything
      screen.fill((255,255,255))      
      arm.draw(screen)
      forearm.draw(screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            Rotatable.DEBUG_DRAW = not Rotatable.DEBUG_DRAW
         
         elif event.type == pygame.MOUSEMOTION:
            mousePos = Vector2(*event.pos)
            arms[armChoice].pointToPosition(mousePos)
         
         elif event.type == pygame.MOUSEBUTTONDOWN:
            armChoice = 1
            
         elif event.type == pygame.MOUSEBUTTONUP:
            armChoice = 0
            
   
   
if __name__ == "__main__":
   main()
