
import pygame


SCREEN_SIZE = (1200, 700)

actionMap = {
   "attack" : 3,
   "jump"   : 1,
   "defend" : 2
   }

class TextPrint:
   def __init__(self):
      self._startX = 10
      self._startY = 10
      self._indent = 10
      self.reset()
      self._lineHeight = 40
      self._lineWidth = 300
      self._font = pygame.font.Font(None, 40)
      self._actions = []
      
   
   def showActions(self, screen):
      for text in self._actions:
         self.renderText(screen, text)

   def addAction(self, text):
      if text not in self._actions:
         self._actions.append(text)
         
   def removeAction(self, text):
      if text in self._actions:
         self._actions.remove(text)

   def renderText(self, screen, textString):
      # Render some text at the current location and move down a line
      textBitmap = self._font.render(textString, True, (0,0,0))
      screen.blit(textBitmap, [self._x, self._y])
      self._y += self._lineHeight
       
   def reset(self):
      # Go back to the top left
      self._x = self._startX
      self._y = self._startY
       
   def indent(self):
      # "tab" over
      self._x += self._indent
       
   def unindent(self):
      # undo tab
      self._x -= self._indent
      
      
      

def main():
   
   # initialize the pygame module
   pygame.init()
   # load and set the logo
   
   pygame.display.set_caption("Joystick Controls")
   
   screen = pygame.display.set_mode(SCREEN_SIZE)
   
   
   textPrint = TextPrint()
   
   joystick = pygame.joystick.Joystick(0)
   if not joystick.get_init():
      joystick.init()
   
   
   
   # define a variable to control the main loop
   running = True
   
   # main loop
   while running:
         
      
      # Draw everything
      screen.fill((255,255,255))
      textPrint.reset()
      
      # Get count of joysseconds
      joystick_count = pygame.joystick.get_count()
      
     
      textPrint.showActions(screen)
      
  
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            running = False
         
         elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == actionMap["attack"]:
               textPrint.addAction("attack")
            elif event.button == actionMap["jump"]:
               textPrint.addAction("jump")
            elif event.button == actionMap["defend"]:
               textPrint.addAction("defend")
               
         elif event.type == pygame.JOYBUTTONUP:
            if event.button == actionMap["attack"]:
               textPrint.removeAction("attack")
            elif event.button == actionMap["jump"]:
               textPrint.removeAction("jump")
            elif event.button == actionMap["defend"]:
               textPrint.removeAction("defend")
         
         
            
      
      # Update everything
      
if __name__ == "__main__":
   main()