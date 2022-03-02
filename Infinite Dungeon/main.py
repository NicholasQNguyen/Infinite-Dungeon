"""
Author: Nicholas Nguyen
Infinite Dungeon
File: main.py
"""
import pygame
from modules.managers.screenManager import ScreenManager
from modules.UI.screenInfo import SCREEN_SIZE, UPSCALED


def main():
    # Initialize the module
    pygame.init()

    # Load and set the logo
    pygame.display.set_caption("Infinite Dungeon")

    # Get the screen
    screen = pygame.display.set_mode(list(UPSCALED))
    drawSurface = pygame.Surface(list(SCREEN_SIZE))

    screenManager = ScreenManager()

    # Make a game clock for nice, smooth animations
    gameClock = pygame.time.Clock()

    RUNNING = True

    while RUNNING:

        screenManager.draw(drawSurface)
        pygame.transform.scale(drawSurface, list(UPSCALED), screen)
        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False
                break
            result = screenManager.handleEvent(event)

            if result == "exit":
                RUNNING = False
                break

        gameClock.tick(60)
        seconds = min(.5, gameClock.get_time() / 1000)

        screenManager.update(seconds)

    pygame.quit()


if __name__ == '__main__':
    main()
