
import pygame
import os
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.backgrounds import *
from modules.kirby import Kirby
from modules.systems import *



SCREEN_SIZE = Vector2(200, 200)
WORLD_SIZE = Vector2(5000, 200)

SCALE = 3
UPSCALED = SCREEN_SIZE * SCALE


      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo   
   pygame.display.set_caption("Parallax")
   
   screen = pygame.display.set_mode(list(UPSCALED))
   drawSurf = pygame.Surface(list(SCREEN_SIZE))
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   staticBG = EfficientBackground(SCREEN_SIZE, "bg3.png", parallax=0)
   bg2 = RepeatingSprite(WORLD_SIZE, "bg2.png", parallax = .25)
   bg1 = RepeatingSprite(WORLD_SIZE, "bg1.png", parallax= .5)

   fog = MovingBackground(SCREEN_SIZE, "fog.png", Vector2(-20, 0), parallax=2, )
   fog.setAlpha(100)
   
   backgrounds = [staticBG, bg2, bg1]
   foregrounds = [fog]
   
   floor = Floor(WORLD_SIZE[0])
   
   kirby = Kirby(Vector2(50,50))
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      
      drawSurf.fill((255,0,255))
      
      # Draw everything
      for background in backgrounds:
         background.draw(drawSurf)

         
      floor.draw(drawSurf)
      kirby.draw(drawSurf)
      
      for foreground in foregrounds:
         foreground.draw(drawSurf)
      
      pygame.transform.scale(drawSurf, list(UPSCALED), screen)
      
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
      
      clipRect = kirby.getCollisionRect().clip(floor.getCollisionRect())
         
      if clipRect.width > 0:
         kirby.collideGround(clipRect.height)
         
      
      # Get some time in seconds
      seconds = min(0.5, gameClock.get_time() / 1000)
      
      # let others update based on the amount of time elapsed
      
      kirby.update(seconds, WORLD_SIZE)
      
      fog.update(seconds)
      
      Drawable.updateWindowOffset(kirby, SCREEN_SIZE, WORLD_SIZE)
      
      
      
      
if __name__ == "__main__":
   main()
