
import pygame

from vector2D import Vector2

SCREEN_SIZE = Vector2(800, 400)

def main():
   
   # initialize the pygame module
   pygame.init()
   
   # load and set the logo
   pygame.display.set_caption("Basic Main")
   
   # obtain the screen
   screen = pygame.display.set_mode(list(SCREEN_SIZE))
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      # Draw everything
      screen.fill((255,255,255))
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
   
   pygame.quit()
   
   
if __name__ == "__main__":
   main()
