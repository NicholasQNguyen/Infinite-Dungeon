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
from modules.gameObjects.tower import Tower
from modules.gameObjects.upgrade import DamageUpgrade,\
                                        SpeedUpgrade,\
                                        ProjectileSpeedUpgrade
from ..UI.items import Text


class GameManager(BasicManager):

    WORLD_SIZE = Vector2(1008, 1008)
    BEGINNING = Vector2(504, 600)
    ARROW_KEYS = [pygame.K_DOWN, pygame.K_UP,
                  pygame.K_LEFT, pygame.K_RIGHT]
    WASD_KEYS = [ord("s"), ord("w"), ord("a"), ord("d")]

    CENTER_OF_ROOM = Vector2(504, 504)

    def __init__(self, screenSize):
        # Stuff for the hero character
        self.archer = Archer(self.BEGINNING)

        # Generate the map
        atlas = Atlas()
        print(atlas)
        self.rooms = atlas.getRooms()
        self.currentRoom = 0

        clearMessage = "You have completed 1 floor!"
        self.clearText = Text(Vector2(404, 400), clearMessage, "default8")
        self.drawClearText = False
        self.floorsCleared = 1

        self.damageUpText = Text(Vector2(504, 400),
                                 "DAMAGE UP!",
                                 "default16")
        self.speedUpText = Text(Vector2(504, 400),
                                "SPEED UP!",
                                "default16")
        self.projectileUpText = Text(Vector2(504, 400),
                                     "PROJECTILE SPEED UP!",
                                     "default16")
        self.drawUpgradeText = False
        self.currentUpgradeText = None

        self.arrowCollisionRects = []
        self.enemyArrowCollisionRects = []
        self.seconds = 0
        self.slimeTimer = 5
        self.invincibilityTimer = 0
        self.fireTimer = 3

    def draw(self, drawSurf):

        # Blit the background
        drawSurf.fill((255, 255, 255))

        self.rooms[self.currentRoom].draw(drawSurf)

        if self.drawUpgradeText:
            self.currentUpgradeText.draw(drawSurf)

        for door in self.rooms[self.currentRoom].doors:
            door.draw(drawSurf)

        for rock in self.rooms[self.currentRoom].rocks:
            rock.draw(drawSurf)

        if self.drawClearText:
            self.clearText.draw(drawSurf)

        self.archer.draw(drawSurf)
        self.archer.drawStats(drawSurf)

        if self.rooms[self.currentRoom].getHasUpgrade():
            self.rooms[self.currentRoom].upgrade.draw(drawSurf)

        if self.rooms[self.currentRoom].getHasStairs():
            self.rooms[self.currentRoom].stairs.draw(drawSurf)

        for arrow in self.rooms[self.currentRoom].arrows:
            arrow.draw(drawSurf, Drawable.WINDOW_OFFSET)
        for arrow in self.rooms[self.currentRoom].enemyArrows:
            arrow.draw(drawSurf)

        for enemy in self.rooms[self.currentRoom].enemies:
            enemy.draw(drawSurf)

    def handleEvent(self, event, js):
        if event.type == pygame.KEYDOWN:
            # If the key is an arrow key, apply it to the player's arrows
            if event.key in GameManager.ARROW_KEYS:
                arrow = Arrow(deepcopy(self.archer.getPosition()))
                # Set the direction based on what arrow was hit
                arrow.changeDirection(event)
                self.rooms[self.currentRoom].arrows.append(arrow)

            elif event.key in GameManager.WASD_KEYS:
                self.archer.handleEvent(event)

            elif event.key == pygame.K_8:
                self.floorsCleared += 1

        elif event.type == pygame.KEYUP:
            if event.key in GameManager.WASD_KEYS:
                self.archer.handleEvent(event)

        if pygame.joystick.get_count() != 0:
            if event.type == pygame.JOYHATMOTION:
                self.archer.handleEvent(event, js.get_hat(0))

            elif event.type == pygame.JOYBUTTONDOWN:
                arrow = Arrow(deepcopy(self.archer.getPosition()))
                buttonList = []
                for i in range(4):
                    buttonList.append(js.get_button(i))
                # Set the direction based on what arrow was hit
                for i in range(4):
                    if buttonList[i]:
                        arrow.changeDirection(event, i)
                        self.rooms[self.currentRoom].arrows.append(arrow)

    def update(self, seconds, screenSize):
        if self.archer.getHP() <= 0:
            # Transition to game over screen
            Drawable.setWindowOffset(Vector2(0, 0))
            return ("dead", self.floorsCleared)

        # let others update based on the amount of time elapsed
        self.archer.update(0, seconds)
        self.archer.getStats().update(seconds)

        for enemy in self.rooms[self.currentRoom].enemies:
            if isinstance(enemy, Golem):
                enemy.changeDirection(deepcopy(self.archer.getPosition()))

        for arrow in self.rooms[self.currentRoom].arrows:
            arrow.update(seconds)
            self.arrowCollisionRects.append(arrow.getCollideRect())

        for arrow in self.rooms[self.currentRoom].enemyArrows:
            arrow.update(seconds)
            self.enemyArrowCollisionRects.append(arrow.getCollideRect())

        for enemy in self.rooms[self.currentRoom].enemies:
            if isinstance(enemy, Slime):
                enemy.update(seconds)
            elif isinstance(enemy, Golem):
                enemy.update(seconds)

        self.fireTimer -= seconds
        self.slimeTimer -= seconds
        self.invincibilityTimer -= seconds

        # Change the slime's movement direction every 5 seconds
        if self.slimeTimer <= 0:
            for enemy in self.rooms[self.currentRoom].enemies:
                if isinstance(enemy, Slime):
                    enemy.handleEvent()
            self.slimeTimer = 5

        # Fire an arrow from a tower every 2 seconds
        if self.fireTimer <= 0:
            for enemy in self.rooms[self.currentRoom].enemies:
                if isinstance(enemy, Tower):
                    enemy.fire(deepcopy(self.archer.getPosition()),
                               self.rooms[self.currentRoom].enemyArrows)
            self.fireTimer = 2

        # Check if the slimes are going beyond the borders
        # and bounce them back if so
        for enemy in self.rooms[self.currentRoom].enemies:
            if isinstance(enemy, Slime):
                if enemy.getX() + enemy.getWidth() >\
                   GameManager.WORLD_SIZE[0] or\
                   enemy.getX() < 0 or \
                   enemy.getY() > GameManager.WORLD_SIZE[1] or \
                   enemy.getY() < 0:
                    enemy.changeDirection()

        # Check if the player is going beyond the borders
        if self.archer.getX() > GameManager.WORLD_SIZE[0]:
            self.archer.setPosition(self.archer.getPosition() -
                                    Vector2(50, 0))
        elif self.archer.getX() < 0:
            self.archer.setPosition(self.archer.getPosition() -
                                    Vector2(-50, 0))
        if self.archer.getY() > GameManager.WORLD_SIZE[1]:
            self.archer.setPosition(self.archer.getPosition() -
                                    Vector2(0, 50))
        elif self.archer.getY() < 0:
            self.archer.setPosition(self.archer.getPosition() -
                                    Vector2(0, -50))

        # Check if arrows are beyond the border and delete them if they are
        for arrow in self.rooms[self.currentRoom].arrows:
            if arrow.getX() > GameManager.WORLD_SIZE[0] or arrow.getX() < 0 or\
               arrow.getY() > GameManager.WORLD_SIZE[1] or arrow.getY() < 0:
                arrow.isDead()

        self.archerCollisionRect = self.archer.getCollideRect()

        # Check for enemy arrow collisions
        for enemy in self.rooms[self.currentRoom].enemies:
            enemyCollisionRect = enemy.getCollideRect()
            if self.rooms[self.currentRoom].arrows != []:
                for arrow in self.rooms[self.currentRoom].arrows:
                    arrowCollisionRect = arrow.getCollideRect()
                    if enemyCollisionRect.colliderect(arrowCollisionRect):
                        arrow.kill()
                        enemy.takeDamage(arrow.getDamage())

        # Check for rock arrow collision
        for rock in self.rooms[self.currentRoom].rocks:
            rockCollisionRect = rock.getCollideRect()
            if self.rooms[self.currentRoom].arrows != []:
                for arrow in self.rooms[self.currentRoom].arrows:
                    arrowCollisionRect = arrow.getCollideRect()
                    if rockCollisionRect.colliderect(arrowCollisionRect):
                        arrow.kill()

        # Check for rock arrow collision
        for rock in self.rooms[self.currentRoom].rocks:
            rockCollisionRect = rock.getCollideRect()
            if self.rooms[self.currentRoom].enemyArrows != []:
                for arrow in self.rooms[self.currentRoom].enemyArrows:
                    arrowCollisionRect = arrow.getCollideRect()
                    if rockCollisionRect.colliderect(arrowCollisionRect):
                        arrow.kill()

        # Check for rock player/enemy collision
        for rock in self.rooms[self.currentRoom].rocks:
            rockCollisionRect = rock.getCollideRect()
            if self.archerCollisionRect.colliderect(rockCollisionRect):
                self.archer.collide(rock)
            for enemy in self.rooms[self.currentRoom].enemies:
                if isinstance(enemy, Golem):
                    if enemy.getCollideRect().colliderect(rockCollisionRect):
                        enemy.collide(rock)

        # Check if we get hit by an enemy arrow
        for arrow in self.rooms[self.currentRoom].enemyArrows:
            arrowCollisionRect = arrow.getCollideRect()
            if arrowCollisionRect.colliderect(self.archerCollisionRect):
                if self.invincibilityTimer < 0:
                    self.archer.takeDamage(arrow.getDamage())
                    self.archer.update(arrow.getDamage(), seconds)
                    arrow.kill()
                    # 2 seconds of invincibilty
                    self.invincibilityTimer = 2

        # Check for enemy collision for damage purposes
        for enemy in self.rooms[self.currentRoom].enemies:
            enemyCollisionRect = enemy.getCollideRect()
            if enemyCollisionRect.colliderect(self.archerCollisionRect) and\
               self.invincibilityTimer < 0:
                self.archer.takeDamage(enemy.getDamage())
                self.archer.update(enemy.getDamage(), seconds)
                # 2 seconds of invincibilty
                self.invincibilityTimer = 2

            # Hit a rock
            else:
                for rock in self.rooms[self.currentRoom].rocks:
                    rockCollisionRect = rock.getCollideRect()

                    if enemyCollisionRect.colliderect(rockCollisionRect):
                        if isinstance(enemy, Slime):
                            enemy.changeDirection()

        # Check to see if we entered a door
        for door in self.rooms[self.currentRoom].doors:
            doorCollisionRect = door.getCollideRect()
            if doorCollisionRect.colliderect(self.archerCollisionRect) and\
               self.rooms[self.currentRoom].isClear():
                # Change the index to change what room is drawn
                self.currentRoom = door.getDestination()
                # Invincible for 1 seconds entering a new room
                # to prevent cheap hits
                self.invincibilityTimer = 1
                # Move the archer to the corresponding door when moving rooms
                if door.getType() == "North":
                    self.archer.setPosition(Vector2(504, 800))
                elif door.getType() == "East":
                    self.archer.setPosition(Vector2(200, 504))
                elif door.getType() == "South":
                    self.archer.setPosition(Vector2(504, 200))
                elif door.getType() == "West":
                    self.archer.setPosition(Vector2(800, 504))

                # Set it so that we index to the last room in the list
                if self.currentRoom == 99:
                    self.currentRoom = -1

                self.drawUpgradeText = False

                # Kill any enemy that spawns on a rock to
                # prevent trapped enemies
                for enemy in self.rooms[self.currentRoom].enemies:
                    for rock in self.rooms[self.currentRoom].rocks:
                        if rock.getCollideRect().colliderect(
                                                 enemy.getCollideRect()):
                            enemy.kill()

        # Check to see if we hit stairs and reset the dungeon
        if self.rooms[self.currentRoom].getHasStairs():
            if self.archerCollisionRect.colliderect(
                                           self.rooms[self.currentRoom]
                                           .stairs.getCollideRect()):
                newAtlas = Atlas()
                self.atlas = newAtlas
                print(self.atlas)
                self.rooms = self.atlas.getRooms()
                self.currentRoom = 0
                self.archer.setPosition(self.BEGINNING)
                self.drawClearText = False
                self.floorsCleared += 1
                self.clearText.setText("You have cleared " +
                                       str(self.floorsCleared) +
                                       " floors!")

        # Check if we touch the upgrade
        if self.rooms[self.currentRoom].getHasUpgrade():
            if self.archerCollisionRect.colliderect(
                                                   self.rooms[self.currentRoom]
                                                   .upgrade.getCollideRect()):
                self.rooms[self.currentRoom].setHasUpgrade(False)

                self.rooms[self.currentRoom].setUpgradeGrabbed(True)

                # Apply projectile speed and damage upgrades to the arrow
                if isinstance(self.rooms[self.currentRoom].upgrade,
                              DamageUpgrade):
                    self.rooms[self.currentRoom].upgrade.upgrade(Arrow)
                    self.currentUpgradeText = self.damageUpText

                elif isinstance(self.rooms[self.currentRoom].upgrade,
                                ProjectileSpeedUpgrade):
                    self.rooms[self.currentRoom].upgrade.upgrade(Arrow)
                    self.currentUpgradeText = self.projectileUpText

                # Apply speed upgrades to the archer
                elif isinstance(self.rooms[self.currentRoom].upgrade,
                                SpeedUpgrade):
                    self.rooms[self.currentRoom].upgrade.upgrade(self.archer)
                    self.currentUpgradeText = self.speedUpText
                self.drawUpgradeText = True

        # Death checking
        for enemy in self.rooms[self.currentRoom].enemies:
            if enemy.isDead():
                self.rooms[self.currentRoom].enemies.remove(enemy)

        for arrow in self.rooms[self.currentRoom].arrows:
            if arrow.isDead():
                self.rooms[self.currentRoom].arrows.remove(arrow)
        for arrow in self.rooms[self.currentRoom].enemyArrows:
            if arrow.isDead():
                self.rooms[self.currentRoom].enemyArrows.remove(arrow)

        # If room is empty, place an upgrade or stairs if it's the last room
        if self.rooms[self.currentRoom].isClear()\
           and not self.rooms[self.currentRoom].getHasUpgrade()\
           and not self.rooms[self.currentRoom].getUpgradeGrabbed():
            if self.currentRoom == -1:
                self.rooms[self.currentRoom].setHasStairs(True)
                self.drawClearText = True
            else:
                self.rooms[self.currentRoom].setHasUpgrade(True)

        Drawable.updateWindowOffset(
                 self.archer, screenSize, GameManager.WORLD_SIZE)

        # Return a tuple to avoid error messages
        return (None, None)

    def updateMovement(self):
        self.archer.updateMovement()
