
import pygame
import os
from modules.vector2D import Vector2
from modules.plants import *
from modules.star import Star
from modules.kirby import Kirby
# from modules.timer import TimerFunction
import random


SCREEN_SIZE = Vector2(300, 300)
SCALE = 3
UPSCALED = SCREEN_SIZE * SCALE


def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Animation")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   star = Star(Vector2(0,0))
   lilly = WaterLilly(Vector2(150,200))
   kirbys = []
#    kirby = Kirby(SCREEN_SIZE / 2)
   background = Drawable("background.png", Vector2(0,0))
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   timer = 5   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      background.draw(drawSurface)
      star.draw(drawSurface)
      lilly.draw(drawSurface)
      for kirby in kirbys:
         kirby.draw(drawSurface)

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
            
      
      # Update everything
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = min(.5, gameClock.get_time() / 1000)
      
      timer -= seconds

      if timer <= 0:
         kirbys.append(Kirby((random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]))))
         timer = 5
      # let others update based on the amount of time elapsed
      star.update(seconds)
      lilly.update(seconds)
      for kirby in kirbys:
         kirby.update(seconds)
      
      
      
      # Detect collision
      if star.getCollisionRect().colliderect(lilly.getCollisionRect()):
         lilly.startAnimation()
      else:
         lilly.stopAnimation()
      
if __name__ == "__main__":
   main()
