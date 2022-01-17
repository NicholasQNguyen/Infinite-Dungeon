
from curses import KEY_UP
import pygame
import os
from vector2D import Vector2


SCREEN_SIZE = Vector2(800, 800)

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Arrows")
   
   screen = pygame.display.set_mode(list(SCREEN_SIZE))
   
   # Keep track of the image of the last arrow pressed, default to first arrow
   arrows = pygame.image.load(os.path.join("images", "arrows.png")).convert()
   
   arrowSize = Vector2(32,32)
   
   image = pygame.Surface(list(arrowSize))
   imagePosition = Vector2(200,200)
   velocity = Vector2(0,0)
   VELOCITYVALUE = 5


   # Blit an arrow onto the image
   image.blit(arrows, (0,0), pygame.Rect(0,0,arrowSize.x,arrowSize.y))
   
   # Set the color key. Since all arrows have the same color key, only need to do this once.
   image.set_colorkey(image.get_at((0,0)))
   
   gameClock = pygame.time.Clock()
   
   # Sefine a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      screen.fill((255,255,255))
      screen.blit(image, list(imagePosition))
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      gameClock.tick(60)
      seconds = gameClock.get_time()/1000

      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
            
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            image.blit(arrows, (0,0), pygame.Rect(0,0,arrowSize.x,arrowSize.y))
            velocity = Vector2(0, -VELOCITYVALUE)

         elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            image.blit(arrows, (0,0), pygame.Rect(arrowSize.x,0,arrowSize.x,arrowSize.y))
            velocity = Vector2(VELOCITYVALUE, 0)

         elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            image.blit(arrows, (0,0), pygame.Rect(arrowSize.x*2, 0, arrowSize.x, arrowSize.y))
            velocity = Vector2(0, VELOCITYVALUE)

         elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            image.blit(arrows, (0,0), pygame.Rect(arrowSize.x*3, 0, arrowSize.x, arrowSize.y))
            velocity = Vector2(-VELOCITYVALUE, 0)

         elif event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN,
                                                           pygame.K_LEFT, pygame.K_RIGHT]:
            velocity = Vector2(0,0)
      
      imagePosition += velocity


   pygame.quit()  
            
            
   
   
if __name__ == "__main__":
   main()
