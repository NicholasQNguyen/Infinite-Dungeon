
import pygame
import os
from vector2D import Vector2


SCREEN_SIZE = Vector2(800, 800)


class Star(object):
   def __init__(self):
      
      self.image = pygame.image.load(os.path.join("images", "star.png")).convert()
      
      self.image.set_colorkey(self.image.get_at((0,0)))
      self.position = Vector2(0,0)
      self.velocity = Vector2(0,0)
      self.speed = 500
   
   def update(self, seconds):
      self.position += self.velocity * seconds
      

class Grass(object):
   def __init__(self):
      
      flowers = pygame.image.load(os.path.join("images", "flowers-color-key.png")).convert()
      
      self.image = pygame.Surface((114,116))
      self.image.blit(flowers, (0,0), pygame.Rect(456,116,114,116))
      
      self.collidedImage = pygame.Surface((114,116))
      self.collidedImage.blit(flowers, (0,0), pygame.Rect(342,232,114,116))
      
      
      self.image.set_colorkey(self.image.get_at((0,0)))
      self.collidedImage.set_colorkey(self.image.get_at((0,0)))
      self.position = Vector2(400,400)
   
   
def getCollisionBox(obj):
   rect = obj.position + pygame.Rect(obj.image.get_rect())
   return rect
      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Collision")
   
   screen = pygame.display.set_mode(list(SCREEN_SIZE))
   
   
   background = pygame.image.load(os.path.join("images", "background.png")).convert()
   
   
   star = Star()
   grass = Grass()
   
   # Create a clock
   gameClock = pygame.time.Clock()
   
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      screen.blit(background, (0,0))
      screen.blit(star.image, list(star.position))
      screen.blit(grass.image, list(grass.position))
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               star.velocity.y = star.speed
            elif event.key == pygame.K_UP:
               star.velocity.y = -star.speed
            elif event.key == pygame.K_LEFT:
               star.velocity.x = -star.speed
            elif event.key == pygame.K_RIGHT:
               star.velocity.x = star.speed
         
         elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
               star.velocity.y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               star.velocity.x = 0
         
 
      gameClock.tick(60)
      
      seconds = gameClock.get_time() / 1000
            
            
      
      # Update everything
      star.update(seconds)
      
      if getCollisionBox(star).colliderect(getCollisionBox(grass)):
           grass.image = grass.collidedImage
         
         
   
if __name__ == "__main__":
   main()
