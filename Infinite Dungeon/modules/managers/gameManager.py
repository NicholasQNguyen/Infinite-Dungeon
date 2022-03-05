import pygame
from copy import deepcopy

from .basicManager import BasicManager
from modules.gameObjects.vector2D import Vector2
from modules.gameObjects.drawable import Drawable
from modules.gameObjects.archer import Archer
from modules.gameObjects.arrow import Arrow
from modules.gameObjects.slime import Slime
from modules.gameObjects.atlas import Atlas
from modules.gameObjects.golem import Golem
from modules.gameObjects.upgrade import DamageUpgrade,\
                                        SpeedUpgrade,\
                                        ProjectileSpeedUpgrade
from ..UI.items import Text


class GameManager(BasicManager):

    WORLD_SIZE = Vector2(1008, 1008)
    BEGINNING = Vector2(-600, -600)
    ARROW_KEYS = [pygame.K_DOWN, pygame.K_UP,
                  pygame.K_LEFT, pygame.K_RIGHT]
    WASD_KEYS = [ord("s"), ord("w"), ord("a"), ord("d")]

    CENTER_OF_ROOM = Vector2(504, 504)

    def __init__(self, screenSize):
        # Stuff for the hero character
        self.archer = Archer(Vector2(500, 500))

        # Generate the map
        atlas = Atlas.getInstance()
        print(atlas)
        self.rooms = atlas.getRooms()
        self.currentroom = 0

        self.mapText = Text(Vector2(600, 600), str(atlas), "default8")

        self.arrowCollisionRects = []

        self.seconds = 0
        self.slimeTimer = 5
        self.invincibilityTimer = 0

    def draw(self, drawSurf):

        # Blit the background
        drawSurf.fill((255, 255, 255))

        self.rooms[self.currentroom].draw(drawSurf)

        for door in self.rooms[self.currentroom].doors:
            door.draw(drawSurf)

        self.archer.draw(drawSurf)
        self.archer.drawStats(drawSurf)

        if self.rooms[self.currentroom].getHasUpgrade():
            self.rooms[self.currentroom].upgrade.draw(drawSurf)

        for arrow in self.rooms[self.currentroom].arrows:
            arrow.draw(drawSurf, Drawable.WINDOW_OFFSET)

        for enemy in self.rooms[self.currentroom].enemies:
            enemy.draw(drawSurf)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            # If the key is an arrow key, apply it to the player's arrows
            if event.key in GameManager.ARROW_KEYS:
                arrow = Arrow(deepcopy(self.archer.getPosition()))
                # Set the direction based on what arrow was hit
                arrow.changeDirection(event)
                self.rooms[self.currentroom].arrows.append(arrow)

            elif event.key in GameManager.WASD_KEYS:
                self.archer.handleEvent(event)

        elif event.type == pygame.KEYUP:
            if event.key in GameManager.WASD_KEYS:
                self.archer.handleEvent(event)

    def update(self, seconds, screenSize):
        if self.archer.getHP() <= 0:
            print("RIP")
            # Transition to game over screen
            return "dead"
        # let others update based on the amount of time elapsed
        self.archer.update(0, seconds)
        self.archer.getStats().update(seconds)

        for enemy in self.rooms[self.currentroom].enemies:
            if isinstance(enemy, Golem):
                enemy.changeDirection(enemy,
                                      deepcopy(self.archer.getPosition()))

        for arrow in self.rooms[self.currentroom].arrows:
            arrow.update(seconds)
            self.arrowCollisionRects.append(arrow.getCollideRect())

        for enemy in self.rooms[self.currentroom].enemies:
            if isinstance(enemy, Slime):
                enemy.update(seconds)
            elif isinstance(enemy, Golem):
                enemy.update(seconds)

        self.slimeTimer -= seconds
        self.invincibilityTimer -= seconds

        # Change the slime's movement direction every 5 seconds
        if self.slimeTimer <= 0:
            for enemy in self.rooms[self.currentroom].enemies:
                if isinstance(enemy, Slime):
                    enemy.handleEvent()
            self.slimeTimer = 5

        # Check if the slimes are going beyond the borders
        # and bounce them back if so
        for enemy in self.rooms[self.currentroom].enemies:
            if isinstance(enemy, Slime):
                if enemy.getX() + enemy.getWidth() >\
                   GameManager.WORLD_SIZE[0] or\
                   enemy.getX() < 0 or \
                   enemy.getY() > GameManager.WORLD_SIZE[1] or \
                   enemy.getY() < 0:
                    enemy.changeDirection()

        # Check if arrows are beyond the border and delete them if they are
        for arrow in self.rooms[self.currentroom].arrows:
            if arrow.getX() > GameManager.WORLD_SIZE[0] or arrow.getX() < 0 or\
               arrow.getY() > GameManager.WORLD_SIZE[1] or arrow.getY() < 0:
                arrow.isDead()

        self.archerCollisionRect = self.archer.getCollideRect()

        # Check for enemy arrow collisions
        for enemy in self.rooms[self.currentroom].enemies:
            enemyCollisionRect = enemy.getCollideRect()
            if self.rooms[self.currentroom].arrows != []:
                for arrow in self.rooms[self.currentroom].arrows:
                    arrowCollisionRect = arrow.getCollideRect()
                    if enemyCollisionRect.colliderect(arrowCollisionRect):
                        arrow.kill()
                        enemy.takeDamage(arrow.getDamage())

        # Check for enemy collision for damage purposes
        for enemy in self.rooms[self.currentroom].enemies:
            enemyCollisionRect = enemy.getCollideRect()
            if enemyCollisionRect.colliderect(self.archerCollisionRect) and\
               self.invincibilityTimer < 0:
                self.archer.takeDamage(enemy.getDamage())
                self.archer.update(enemy.getDamage(), seconds)
                # 2 seconds of invincibilty
                self.invincibilityTimer = 2
                print(self.archer.getHP())

        # Check to see if we entered a door
        for door in self.rooms[self.currentroom].doors:
            doorCollisionRect = door.getCollideRect()
            if doorCollisionRect.colliderect(self.archerCollisionRect):
                # Change the index to change what room is drawn
                self.currentroom = door.getDestination()
                # Move the archer to the corresponding door when moving rooms
                if door.getType() == "North":
                    self.archer.setPosition(Vector2(504, 800))
                elif door.getType() == "East":
                    self.archer.setPosition(Vector2(200, 504))
                elif door.getType() == "South":
                    self.archer.setPosition(Vector2(504, 200))
                elif door.getType() == "West":
                    self.archer.setPosition(Vector2(800, 504))

                if self.currentroom == 99:
                    self.currentroom = -1

        # Check if we touch the upgrade
        if self.rooms[self.currentroom].getHasUpgrade():
            if self.archerCollisionRect.colliderect(
                                                   self.rooms[self.currentroom]
                                                   .upgrade.getCollideRect()):
                self.rooms[self.currentroom].setHasUpgrade(False)

                self.rooms[self.currentroom].setUpgradeGrabbed(True)

                # Apply projectile speed and damage upgrades to the arrow
                if isinstance(self.rooms[self.currentroom].upgrade,
                              DamageUpgrade)\
                   or isinstance(self.rooms[self.currentroom].upgrade,
                                 ProjectileSpeedUpgrade):
                    self.rooms[self.currentroom].upgrade.upgrade(Arrow)
                # Apply speed upgrades to the archer
                elif isinstance(self.rooms[self.currentroom].upgrade,
                                SpeedUpgrade):
                    self.rooms[self.currentroom].upgrade.upgrade(self.archer)

        # Death checking
        for enemy in self.rooms[self.currentroom].enemies:
            if enemy.isDead():
                self.rooms[self.currentroom].enemies.remove(enemy)

        for arrow in self.rooms[self.currentroom].arrows:
            if arrow.isDead():
                self.rooms[self.currentroom].arrows.remove(arrow)

        # If the room is empty, place an upgrade
        if self.rooms[self.currentroom].isClear()\
           and not self.rooms[self.currentroom].getHasUpgrade()\
           and not self.rooms[self.currentroom].getUpgradeGrabbed():
            self.rooms[self.currentroom].setHasUpgrade(True)

        Drawable.updateWindowOffset(
                 self.archer, screenSize, GameManager.WORLD_SIZE)

    def updateMovement(self):
        self.archer.updateMovement()
