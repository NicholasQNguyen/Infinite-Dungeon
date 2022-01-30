
import pygame
import os
from modules.vector2D import Vector2
from modules.grass import Grass
from modules.star import Star
from modules.drawable import Drawable

SCREEN_SIZE = Vector2(300, 300)
WORLD_SIZE = Vector2(600, 600)
SCALE = 3
UPSCALED = SCREEN_SIZE * SCALE

def updateWindowOffset(tracked, screenSize, worldSize):
   position = tracked.getPosition()
   size = tracked.getSize()
   width = size[0]
   height = size[1]
   return Vector2(min(max(0, position[0] + (width // 2) - (screenSize[0] // 2)),
                        worldSize[0] - screenSize[0]),
                    min(max(0, position[1] + (height // 2) - (screenSize[1] // 2)),
                        worldSize[1] - screenSize[1]))
      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Inheritance and OOP")
   
   screen = pygame.display.set_mode(list(UPSCALED))   
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   gameClock = pygame.time.Clock()
   
   
   star = Star(Vector2(0,0))
   grass = Grass(Vector2(100,100))
   background = Drawable("background.png", Vector2(0, 0))
 
#    background = pygame.image.load(os.path.join("images", "background.png")).convert()
   
   offset = Vector2(0,0)
   
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      background.draw(drawSurface)
      star.draw(drawSurface)
      grass.draw(drawSurface)      
      
      pygame.transform.scale(drawSurface, list(UPSCALED), screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         
         star.handleEvent(event)
         
      gameClock.tick()
      
      seconds = gameClock.get_time() / 1000
            
      
      # Update everything
      star.update(seconds)
      
      
      # Detect collision
      if star.getCollisionRect().colliderect(grass.getCollisionRect()):
         grass.changeToRose()
      else:
         grass.changeToGrass()
         
         
      offset = Drawable.updateWindowOffset(star, SCREEN_SIZE, WORLD_SIZE)
   
if __name__ == "__main__":
   main()
