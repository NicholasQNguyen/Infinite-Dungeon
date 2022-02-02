"""
Author: Nicholas Nguyen
Infinite Dungeon
File: main.py
"""

import pygame
from vector2D import Vector2
from archer import Archer
from arrow import Arrow
from copy import deepcopy
from target import Target
from random import randint
from slime import Slime
from atlas import Atlas
from golem import Golem


WORLD_SIZE = Vector2(1008, 1008)
SCREEN_SIZE = Vector2(800, 800)
SCALE_FACTOR = 1
UPSCALED = SCREEN_SIZE * SCALE_FACTOR
BEGINNING = Vector2(-600, -600)
ARROW_KEYS = [pygame.K_DOWN, pygame.K_UP,
              pygame.K_LEFT, pygame.K_RIGHT]
WASD_KEYS = [ord("s"), ord("w"), ord("a"), ord("d")]

CENTER_OF_ROOM = Vector2(504, 504)
ARCHER_VELOCITY = 4


def main():
    # Initialize the module
    pygame.init()

    # Get the screen
    screen = pygame.display.set_mode(list(UPSCALED))

    # Let's make a background so we can see if we're moving
    drawSurface = pygame.Surface(list(SCREEN_SIZE))

    # Basic Room Drawing
    atlas = Atlas()

    print(atlas)

    rooms = atlas.getRooms()

    currentRoom = 0

    # Stuff for the hero character
    archer = Archer((Vector2(500, 500)), ARCHER_VELOCITY, "archer.png")

    arrows = []

    offset = Vector2(0, 0)

    gameClock = pygame.time.Clock()
    seconds = 0

    arrowCollisionRects = []

    timer = 5

    RUNNING = True

    while RUNNING:

        # Blit the background
        drawSurface.fill((255, 255, 255))

        # start by drawing the starting room
        rooms[currentRoom].draw(drawSurface, offset)

        for door in rooms[currentRoom].doors:
            door.draw(drawSurface, offset)

        archer.draw(drawSurface, offset)

        for arrow in arrows:
            arrow.draw(drawSurface, offset)

        for enemy in rooms[currentRoom].enemies:
            enemy.draw(drawSurface, offset)

        pygame.transform.scale(drawSurface, list(UPSCALED), screen)

        pygame.display.flip()

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # change the value to False, to exit the main loop
                RUNNING = False

            elif event.type == pygame.KEYDOWN:
                # If the key in an arrow, apply it to the player's arrows
                if event.key in ARROW_KEYS:
                    arrow = Arrow(deepcopy(archer.getPosition()),
                                  5, "arrow.png")
                    # Set the direction based on what arrow was hit
                    arrow.changeDirection(event)
                    arrows.append(arrow)

                elif event.key in WASD_KEYS:
                    archer.handleEvent(event)

            elif event.type == pygame.KEYUP:

                if event.key in WASD_KEYS:
                    archer.handleEvent(event)

        gameClock.tick(60)
        seconds = gameClock.get_time() / 1000

        timer -= seconds

        # Stuff for object movement
        for arrow in arrows:
            arrow.update()
            arrowCollisionRects.append(arrow.getCollideRect())

        for enemy in rooms[currentRoom].enemies:
            if isinstance(enemy, Slime):
                enemy.move()
            elif isinstance(enemy, Golem):
                enemy.move(deepcopy(archer.getPosition()))

        # Change the slime's movement direction every 5 seconds
        if timer <= 0:
            for enemy in rooms[currentRoom].enemies:
                if isinstance(enemy, Slime):
                    enemy.changeDirection()
            timer = 5

        # Check if the slimes are going beyond the borders and bounce them back if so
        for enemy in rooms[currentRoom].enemies:
            if isinstance(enemy, Slime):
                if enemy.getX() + enemy.getWidth() > WORLD_SIZE[0] or enemy.getX() < 0 or \
                   enemy.getY() > WORLD_SIZE[1] or enemy.getY() < 0:
                    enemy.changeDirection()
 
        archer.update()

        # Check if arrows are beyond the border and delete them if they are
        for arrow in arrows:
            if arrow.getX() > WORLD_SIZE[0] or arrow.getX() < 0 or \
               arrow.getY() > WORLD_SIZE[1] or arrow.getY() < 0:
                arrow.isDead()

        archerCollisionRect = archer.getCollideRect()

        # Check for enemy arrow collisions
        for enemy in rooms[currentRoom].enemies:
            enemyCollisionRect = enemy.getCollideRect()
            if arrows != []:
                for collisionBox in arrowCollisionRects:
                    if enemyCollisionRect.colliderect(collisionBox):
                        # TODO: Replace this with damage instead of just killing
                        enemy.kill()
                        arrow.kill()

        for door in rooms[currentRoom].doors:
            doorCollisionRect = door.getCollideRect()
            if doorCollisionRect.colliderect(archerCollisionRect):
                print("Moving")
                # Change the index to change what room is drawn
                currentRoom = door.getDestination()
                # Move the archer to the center of the room when moving rooms
                print(currentRoom)
                archer.setPosition(deepcopy(CENTER_OF_ROOM))

                if currentRoom == 99:
                    currentRoom = -1

                # Redraw the room so that we get rid of the enemies from the last room
                drawSurface.fill((255, 255, 255))
                pygame.display.flip()
                rooms[currentRoom].draw(drawSurface, offset)
                pygame.display.flip()

        for enemy in rooms[currentRoom].enemies:
            if enemy.isDead():
                rooms[currentRoom].enemies.remove(enemy)

        for arrow in arrows:
            if arrow.isDead():
                arrows.remove(arrow)

        offset = Vector2(max(0,
                             min(archer.getX() + (archer.getWidth() // 2) -
                                 (SCREEN_SIZE[0] // 2),
                                 WORLD_SIZE[0] - SCREEN_SIZE[0])),
                         max(0,
                             min(archer.getY() + (archer.getHeight() // 2) -
                                 (SCREEN_SIZE[1] // 2),
                                 WORLD_SIZE[1] - SCREEN_SIZE[1])))

    pygame.quit()


if __name__ == '__main__':
    main()
