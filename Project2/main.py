"""
Author: Nicholas Nguyen
Project 1
File: Main.py
"""
import pygame
import os
from vector2D import Vector2
from random import randint
from orb import Orb
from star import Star

# Two different sizes now! Screen size is the amount we show the player,
#  and world size is the size of the interactable world
SCREEN_SIZE = Vector2(800, 800)
WORLD_SIZE = Vector2(1200, 1200)


def main():
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    pygame.display.set_caption("Nicholas Nguyen Project 2")

    screen = pygame.display.set_mode(list(SCREEN_SIZE))

    # Let's make a background so we can see if we're moving
    background = pygame.image.load(os.path.join("background.png")).convert()

    # Star images
    star = Star()
    star._image.convert()
    star._image.set_colorkey(star._image.get_at((0, 0)))

    # The offset of the window into the world
    offset = Vector2(0, 0)

    gameClock = pygame.time.Clock()

    # define a variable to control the main loop
    RUNNING = True

    # main loop
    while RUNNING:

        # Draw everything, adjust by offset
        screen.blit(background, (-offset.x, -offset.y))
        star.draw(screen, offset)

        # Flip the display to the monitor
        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type
            # QUIT or ESCAPE is pressed
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False

            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_DOWN:
                     velocity.y = speed  
               
                 elif event.key == pygame.K_UP:
                     velocity.y = -speed      
               
                 elif event.key == pygame.K_LEFT:
                     velocity.x = -speed        
               
                 elif event.key == pygame.K_RIGHT:
                     velocity.x = speed       
         
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    velocity.y = 0
               
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    velocity.x = 0

        gameClock.tick(60)

        ticks = gameClock.get_time() / 1000

        # Update everything
        star.update(WORLD_SIZE, ticks)

        # Recalculate the offest based on the new position
        offset = Vector2(max(0,
                             min(star.getX() + (star.getWidth() // 2) -
                                 (SCREEN_SIZE[0] // 2),
                                 WORLD_SIZE[0] - SCREEN_SIZE[0])),
                         max(0,
                             min(star.getY() + (star.getHeight() // 2) -
                                 (SCREEN_SIZE[1] // 2),
                                 WORLD_SIZE[1] - SCREEN_SIZE[1])))

    pygame.quit()


if __name__ == "__main__":
    main()
