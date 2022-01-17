
import pygame

SCREEN_SIZE = (800, 600)

def main():
   
   # initialize the pygame module
   pygame.init()

   # initialize the font stuff
   pygame.font.init()

   # set up the arial font and message
   arial = pygame.font.SysFont("Arial", 20)
   message = arial.render("This text is centered on the screen!", False, (0,0,0))

   # Set up the surface that we'll use to blit the sprite from the sheet
   archerSurface = pygame.Surface((20,20))
   grabberRectangle = pygame.Rect(0,20,20,20)
   # Load the sprite sheet
   spriteSheet = pygame.image.load("images/spriteSheet.png")
   archerSurface.blit(spriteSheet, (0,0), grabberRectangle)
   archerSurface.set_colorkey(archerSurface.get_at((0,0)))

   # load and set the logo
   pygame.display.set_caption("Basic Main")
   
   # obtain the screen
   screen = pygame.display.set_mode(SCREEN_SIZE)
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      # Draw everything
      screen.fill((190,190,190))

      # Add the message to the cneter of the screen
      screen.blit(message, (screen.get_width()/2 - message.get_width()/2, screen.get_height()/2- message.get_height()/2))

      # Add sprite to bottom center of screen
      screen.blit(archerSurface, ((screen.get_width() / 2) - 20, screen.get_height()-20))
      
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
