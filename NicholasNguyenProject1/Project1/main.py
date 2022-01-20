"""
Author: Nicholas Nguyen
Project 1
File: Main.py
"""
import pygame
import os
from vector2D import Vector2
from random import randint

# Two different sizes now! Screen size is the amount we show the player,
#  and world size is the size of the interactable world
SCREEN_SIZE = Vector2(800, 800)
WORLD_SIZE = Vector2(1200, 1200)


class Orb:
    _image = pygame.image.load(os.path.join("orb.png"))
    _position = Vector2(0, 0)
    _velocity = Vector2(0, 0)

    def __init__(self):
        # Set position to center of the world view
        self._position = Vector2(WORLD_SIZE[0]/2, WORLD_SIZE[1]/2)
        # Set velocity to some random Vector2 to start with
        self._velocity = Vector2(randint(1, 10), randint(1, 10))

    def draw(self, surface, offset):
        """Blits the orb onto a specifed surface with an offset"""
        surface.blit(self._image, list(self._position - offset))

    def getPosition(self):
        """Returns the Vector2 of the position"""
        return self._position

    def getX(self):
        """Returns the X position which is an int"""
        return self._position[0]

    def getY(self):
        """Returns the X position which is an int"""
        return self._position[1]

    def getSize(self):
        """Returns the size of the surface the orb is on"""
        return self._image.get_size()

    def getWidth(self):
        """Returns the width of the surface as an int"""
        return self._image.get_width()

    def getHeight(self):
        """Returns the width of the surface as an int"""
        return self._image.get_height()

    def update(self, worldInfo, seconds):
        """Either just updates the posiiton of the orb based on
           the velocity or switches the velocity and adds some
           randomness to the the trajectory if it hits the edge"""
        newPosition = self._position + self._velocity
        # We've gone beyond the borders
        if newPosition[0] < 0 or \
           (newPosition[0] + self.getWidth()) > worldInfo[0] or \
           newPosition[1] < 0 or \
           (newPosition[1] + self.getHeight()) > worldInfo[0]:

            # Add some random noise to change the angle at which it bounces
            # and a bound from (-10,10) so that the orb doesn't
            # go flying really fast all over the place
            newXVelocity = max(min(self._velocity[0] * -1 +
                                   randint(-5, 5), 10), -10)
            newYVelocity = max(min(self._velocity[1] * -1 +
                                   randint(-5, 5), 10), -10)

            self._velocity[0] = newXVelocity
            self._velocity[1] = newYVelocity

            newPosition = self._position + self._velocity

        # Whatever the case may be, set the position
        # to the new calculated position
        self._position = newPosition


def main():
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    pygame.display.set_caption("Nicholas Nguyen Project 1")

    screen = pygame.display.set_mode(list(SCREEN_SIZE))

    # Let's make a background so we can see if we're moving
    background = pygame.image.load(os.path.join("background.png")).convert()

    # Orb images
    orb = Orb()
    orb._image.convert()
    orb._image.set_colorkey(orb._image.get_at((0, 0)))

    # The offset of the window into the world
    offset = Vector2(0, 0)

    gameClock = pygame.time.Clock()

    # define a variable to control the main loop
    RUNNING = True

    # main loop
    while RUNNING:

        # Draw everything, adjust by offset
        screen.blit(background, (-offset.x, -offset.y))
        orb.draw(screen, offset)

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

        gameClock.tick(60)

        ticks = gameClock.get_time() / 1000

        # Update everything
        orb.update(WORLD_SIZE, ticks)

        # Recalculate the offest based on the new position
        offset = Vector2(max(0,
                             min(orb.getX() + (orb.getWidth() // 2) -
                                 (SCREEN_SIZE[0] // 2),
                                 WORLD_SIZE[0] - SCREEN_SIZE[0])),
                         max(0,
                             min(orb.getY() + (orb.getHeight() // 2) -
                                 (SCREEN_SIZE[1] // 2),
                                 WORLD_SIZE[1] - SCREEN_SIZE[1])))

    pygame.quit()


if __name__ == "__main__":
    main()
