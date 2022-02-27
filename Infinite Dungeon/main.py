"""
Author: Nicholas Nguyen
Infinite Dungeon
File: main.py
"""

import pygame
from copy import deepcopy

from modules.gameObjects.vector2D import Vector2
from modules.gameObjects.drawable import Drawable
from modules.gameObjects.archer import Archer
from modules.gameObjects.arrow import Arrow
from modules.gameObjects.slime import Slime
from modules.gameObjects.atlas import Atlas
from modules.gameObjects.golem import Golem
from modules.gameObjects.upgrade import DamageUpgrade, SpeedUpgrade, ProjectileSpeedUpgrade
from modules.managers.frameManager import FrameManager
from modules.managers.screenManager import ScreenManager


WORLD_SIZE = Vector2(1008, 1008)
SCREEN_SIZE = Vector2(800, 800)
SCALE_FACTOR = 1
UPSCALED = SCREEN_SIZE * SCALE_FACTOR
BEGINNING = Vector2(-600, -600)
ARROW_KEYS = [pygame.K_DOWN, pygame.K_UP,
              pygame.K_LEFT, pygame.K_RIGHT]
WASD_KEYS = [ord("s"), ord("w"), ord("a"), ord("d")]

CENTER_OF_ROOM = Vector2(504, 504)
ARROW_VELOCITY = 5


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
    slimeTimer = 5

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
