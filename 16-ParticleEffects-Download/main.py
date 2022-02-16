import pygame,random
from pygame.locals import *
from modules.vector2D import Vector2
import math
from modules.systems import *

WORLD_SIZE = Vector2(1000,600)

# Turn these on or off to see the various particle systems
SHOW = {
   "snow" : False,
   "rain" : False,
   "smoke": False,
   "shower" : False,
   "fountain" : True,
   "cotton" : True
}
         

def main():
   # Pygame setup
   pygame.init()
   screen = pygame.display.set_mode(list(WORLD_SIZE))

   clock=pygame.time.Clock()
   
   # Arbitrary line to simulate a floor
   floor = pygame.Rect(0,505,WORLD_SIZE.x,WORLD_SIZE.y)
   
   # Create and simulate the smoke system   
   smoke = SmokeSystem(Vector2(215, 500))
   smoke.simulate()
   
   # Create and simulate the rain system
   rain = RainSystem(Vector2(0,0))
   rain.setWidth(WORLD_SIZE.x * 2)
   rain.simulate()
   
   # Create and simulate the snow system
   snow = SnowSystem(Vector2(0,0))   
   snow.setWidth(WORLD_SIZE.x)
   snow.simulate()
   
   # Create and simulate the shower system
   shower = ShowerSystem(Vector2(615, 20))
   shower.simulate()
   
   fountain = FountainSystem(Vector2(615, 505))
   fountain.simulate()
   
   cotton = CottonwoodSystem(Vector2(0,500))
   cotton.setWidth(WORLD_SIZE.x)
   cotton.simulate()

   RUNNING = True
   while RUNNING:
      for event in pygame.event.get():
         if event.type == QUIT:
            RUNNING = False
         elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
               RUNNING = False
            elif event.key == K_1:
               SHOW["snow"] = not SHOW["snow"]
            elif event.key == K_2:
               SHOW["rain"] = not SHOW["rain"]
            elif event.key == K_3:
               SHOW["smoke"] = not SHOW["smoke"]
            elif event.key == K_4:
               SHOW["shower"] = not SHOW["shower"]
            elif event.key == K_5:
               SHOW["fountain"] = not SHOW["fountain"]
            elif event.key == K_6:
               SHOW["cotton"] = not SHOW["cotton"]
            
            elif event.key == K_SPACE:
               rain.toggleActiveAreaDraw()
               smoke.toggleActiveAreaDraw()
               snow.toggleActiveAreaDraw()
               shower.toggleActiveAreaDraw()
               fountain.toggleActiveAreaDraw()
               cotton.toggleActiveAreaDraw()
               

      # Tick tock
      seconds = min(0.04, clock.get_time() / 1000)
      
      # Fill the screen and draw the floor
      screen.fill((10, 10, 50))
      pygame.draw.rect(screen, (100,100,100), floor)
      
      # Show the systems
      if SHOW["rain"]:
         rain.update(seconds)
         rain.draw(screen)
      
      if SHOW["smoke"]:
         smoke.update(seconds)
         smoke.draw(screen)
      
      if SHOW["snow"]:
         snow.update(seconds)
         snow.draw(screen)
      
      if SHOW["shower"]:
         shower.update(seconds)
         shower.draw(screen)
         
         
      if SHOW["fountain"]:
         fountain.update(seconds)
         fountain.draw(screen)
         
      if SHOW["cotton"]:
         cotton.update(seconds)
         cotton.draw(screen)
         

      pygame.display.flip()
      clock.tick(60)
      
   pygame.quit()

if __name__ == "__main__":
    main()
