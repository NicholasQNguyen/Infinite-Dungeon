import pygame
import os
from vector2D import Vector2
from  archer import Archer
from arrow import Arrow


SCREEN_SIZE = Vector2(294, 600)
SCALE_FACTOR = 1.5
UPSCALED = SCREEN_SIZE * SCALE_FACTOR
BEGINNING = Vector2(-125, -550)
ARROW_KEYS = [pygame.K_DOWN, pygame.K_UP,
              pygame.K_LEFT, pygame.K_RIGHT]
WASD_KEYS = [ord("s"), ord("w"), ord("a"), ord("d")]

def main():
    # Initialize the module
    pygame.init()

    # Get the screen
    screen = pygame.display.set_mode(list(UPSCALED))

    # Let's make a background so we can see if we're moving
    background2 = pygame.image.load(os.path.join("images", "basicDungeonCropped.png")).convert_alpha()
    drawSurface = pygame.Surface(list(SCREEN_SIZE))

    # Stuff for the hero character
    archer = Archer()
    # List of arrows to keep track of them
    arrows = []

    gameClock = pygame.time.Clock()

    RUNNING = True

    while RUNNING:
        
        drawSurface.blit(background2, (0, 0))
        archer.draw(drawSurface, BEGINNING)
        pygame.transform.scale(drawSurface, list(UPSCALED), screen)

#         screen.blit(background2, (0, 0))

        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                # If the key in an arrow, apply it to projectile
                if event.key in ARROW_KEYS:
                    # Append a new arrow object to the list
                    arrows.append(Arrow(archer.getPosition()))
                    arrow.shoot(event, archer.getPosition(), drawSurface)
                elif event.key in WASD_KEYS:
                    archer.handleEvent(event)

            elif event.type == pygame.KEYUP:
                if event.key in ARROW_KEYS:
                    arrows.append(Arrow(archer.getPosition()))
                    arrow.shoot(event, archer.getPosition(), drawSurface)
                elif event.key in WASD_KEYS:
                    archer.handleEvent(event)

        gameClock.tick(60)
        seconds = gameClock.get_time() / 1000

        archer.update()

    pygame.quit()


if __name__ == '__main__':
    main()
