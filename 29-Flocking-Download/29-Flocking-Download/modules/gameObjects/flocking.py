from .rotated import Rotatable
from .vector2D import Vector2
from ..UI.screenInfo import adjustMousePos, SCREEN_SIZE, distributeHorizontally
from .items import TextItem
import pygame
import random
import math

class Flocky(Rotatable):
    # Weights for thinking
    WEIGHTS = {
        "cohesion" : 10,
        "separation" : 10,
        "alignment" : 10,
        "inside" : 10,
        "avoid" : 10
    }
    
    # For vizualization of the weights
    W_POSITION = distributeHorizontally(len(WEIGHTS), 8 * 5)
    
    WEIGHT_ITEMS = {
        "cohesion"   : TextItem(Vector2(10,                  SCREEN_SIZE.y - 20), "co:",  WEIGHTS["cohesion"],   font="default8"),
        "separation" : TextItem(Vector2(10 + W_POSITION,     SCREEN_SIZE.y - 20), "sep:", WEIGHTS["separation"], font="default8"),
        "alignment"  : TextItem(Vector2(10 + W_POSITION * 2, SCREEN_SIZE.y - 20), "al:",  WEIGHTS["alignment"],  font="default8"),
        "inside"     : TextItem(Vector2(10 + W_POSITION * 3, SCREEN_SIZE.y - 20), "in:",  WEIGHTS["inside"],     font="default8"),
        "avoid"      : TextItem(Vector2(10 + W_POSITION * 4, SCREEN_SIZE.y - 20), "av:",  WEIGHTS["avoid"],      font="default8")
    }
    
    # Inside area information
    AREA_RADIUS = int(SCREEN_SIZE.x * 0.4)
    AREA_CENTER = SCREEN_SIZE // 2
    
    @classmethod
    def drawAll(cls, surface):
        cls.drawWeights(surface)
        cls.drawArea(surface)
    
    @classmethod
    def drawWeights(cls, surface):
        for tItem in cls.WEIGHT_ITEMS.values():
            tItem.draw(surface)
    
    @classmethod
    def drawArea(cls, surface):
        """For debug drawing the area within which the flock will try to stay."""
        pygame.draw.circle(surface, (255,2,255), list(Flocky.AREA_CENTER), cls.AREA_RADIUS, 3)
    
    @classmethod
    def handleEventWeights(cls, event):
        """For adjusting the weights in the debug."""
        amt = 1
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                                          pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]:
            if event.key == pygame.K_1:
                key = "cohesion"
                amt = -amt
            elif event.key == pygame.K_2:
                key = "cohesion"
            elif event.key == pygame.K_3:
                key = "separation"
                amt = -amt
            elif event.key == pygame.K_4:
                key = "separation"
            elif event.key == pygame.K_5:
                key = "alignment"
                amt = -amt
            elif event.key == pygame.K_6:
                key = "alignment"
            elif event.key == pygame.K_7:
                key = "inside"
                amt = -amt
            elif event.key == pygame.K_8:
                key = "inside"
            elif event.key == pygame.K_9:
                key = "avoid"
                amt = -amt
            else:
                key = "avoid"
            
            cls.WEIGHTS[key] = max(0, cls.WEIGHTS[key] + amt)
            cls.WEIGHT_ITEMS[key].change(cls.WEIGHTS[key])
        
   
    def __init__(self, position):
        super().__init__("arrow.png", position)
        
        self._maxVelocity = 80
        self._sightDistance = 100
        self._personalDistance = 50
        self._acceleration = 200                      
        self._thinking = True        
        self._accelerateWhenAlone = False
                
        self._velocity = Vector2(random.randint(-100, 100),
                                 random.randint(-100, 100))
        self._velocity.scale(self._maxVelocity)

        
        self.setAngleFromVelocity()
        
        # Debug visualization properties
        self._debugDraw = False
        self._target = None  
        
    # Debug options
    def toggleDebugDraw(self):
        self._debugDraw = not self._debugDraw
    
    def draw(self, surface):
        super().draw(surface)
        
        if self._debugDraw:
            # Draw personal distance radius, sight distance radius, and velocity
            pygame.draw.circle(surface, (0,0,255),
                               self.getCollisionRect().center,
                               self._personalDistance,
                               2)
            pygame.draw.circle(surface, (0,0,255),
                               self.getCollisionRect().center,
                               self._sightDistance,
                               1)
            pygame.draw.line(surface, (0,255,0),
                             list(self.getCenter()),
                             list(self.getCenter() + self._velocity),
                             3)
            
            # If we have a target draw a circle and line
            if self._target != None:
                pygame.draw.line(surface, (255,0,0),
                                 list(self.getCenter()),
                                 list(map(int, self.getCenter() + self._target)),
                                 1)
                pygame.draw.circle(surface, (255,0,0),
                                   list(map(int, self.getCenter() + self._target)),
                                   3)
      
    # Some adjustment methods  
    def increasePersonalDistance(self):
        self._personalDistance = min(self._sightDistance - 10, self._personalDistance + 10)
     
    def decreasePersonalDistance(self):
        self._personalDistance = max(10, self._personalDistance - 10)
        
    def increaseSightDistance(self):
        self._sightDistance += 10
        
    def decreaseSightDistance(self):
        self._sightDistance = max(self._personalDistance + 10, self._sightDistance - 10)
    
    def getCenter(self):
        return self.getHiddenPosition() + self._image.get_rect().center    
    
    def setAngleFromVelocity(self):
        if self._velocity != Vector2(0,0):
            self.setAngle(self._velocity.getAngle())
       
    # Some thinking methods
    def inside(self):
        """Returns the position the flocking agent should move to in order to stay inside the flocking area.
           Returns None if inside the flocking area."""
        
        distance = (self.getCenter() - Flocky.AREA_CENTER).magnitude()
        
        if distance > Flocky.AREA_RADIUS:
            outsideDistProportion = (distance - Flocky.AREA_RADIUS) / (Flocky.AREA_CENTER.x - Flocky.AREA_RADIUS)
            
            return (Flocky.AREA_CENTER - self.getCenter()).normalized() * outsideDistProportion * self._maxVelocity + self.getCenter()
        
        return None
    
    def separation(self, flock):
        """Returns the position the flocking agent should move to in order to stay separate from others
           within personalDistance. Returns None if there are no neighbors."""
           
        avoidDirection = Vector2(0,0)
        tooClose = 0

        for neighbor in flock:
            distance = (neighbor.getCenter() - self.getCenter()).magnitude()
            if distance < self._personalDistance:
                temp = self.getCenter() - neighbor.getCenter()
                temp.scale(self._maxVelocity)
                temp /= (distance ** 2)
                avoidDirection += temp
                tooClose += 1
        
        if tooClose != 0:
            avoidDirection /= tooClose
            
            return avoidDirection.normalized() * self._maxVelocity + self.getCenter()
        
        return None
        
    def alignment(self, flock):
        """Returns the position the flocking agent should move to in order to remain aligned with others
           in the flock which are within the sightDistance. Returns None if no flocking agents are visible."""
        averageVelocity = Vector2(0,0)
        neighbors = 0
        
        for neighbor in flock:
            if (neighbor.getCenter() - self.getCenter()).magnitude() < self._sightDistance:
                averageVelocity += neighbor._velocity
                neighbors += 1
        
        if neighbors != 0:
            averageVelocity /= neighbors                  
        
            return self.getCenter() + averageVelocity
    
        return None
        
    def cohesion(self, flock):
        """Returns the position the flocking agent should move to in order to remain cohesive with the others
           in the flock which are within the sightDistance. Returns None if no flocking agents are visible."""
                
        averagePosition = Vector2(0,0)
        neighbors = 0        
        
        for neighbor in flock:
            if (neighbor.getCenter() - self.getCenter()).magnitude() < self._sightDistance:
                averagePosition += neighbor.getCenter()
                neighbors += 1
        
        if neighbors != 0:
            averagePosition /= neighbors
        
            return averagePosition
    
        return None
    
    def avoidTarget(self, target):       
        distance = (target.getCenter() - self.getCenter()).magnitude()
        if distance < self._sightDistance:
            velocity = self.getCenter() - target.getCenter()
            velocity.scale(self._maxVelocity)
            velocity /= (distance ** 2)
            return velocity.normalized() * self._maxVelocity + self.getCenter()
        
        return None
        
    def think(self, seconds, flock, kirby):
        """Calculate a moveToPosition based on all thinking methods."""
        moveToPosition = None
        
        others = [x for x in flock if not x is self]
        
        # If the flock is thinking
        if self._thinking:
            # Get moveToPositions for all thinking methods
            insidePosition = self.inside()
            separationPosition = self.separation(others)
            alignmentPosition = self.alignment(others)
            cohesionPosition = self.cohesion(others)
            avoidPosition = self.avoidTarget(kirby)
            
            # Calculate the weighted average of the moveToPositions
            totalWeight = 0
            moveToPosition = Vector2(0,0)
            
            if insidePosition != None:
                totalWeight += Flocky.WEIGHTS["inside"]
                moveToPosition += insidePosition * Flocky.WEIGHTS["inside"]
            
            if separationPosition != None:
                totalWeight += Flocky.WEIGHTS["separation"]
                moveToPosition += separationPosition * Flocky.WEIGHTS["separation"]
            
            if alignmentPosition != None:
                totalWeight += Flocky.WEIGHTS["alignment"]
                moveToPosition += alignmentPosition * Flocky.WEIGHTS["alignment"]
            
            if cohesionPosition != None:
                totalWeight += Flocky.WEIGHTS["cohesion"]
                moveToPosition += cohesionPosition * Flocky.WEIGHTS["cohesion"]
                
            if avoidPosition != None:
                totalWeight += Flocky.WEIGHTS["avoid"]
                moveToPosition += avoidPosition * Flocky.WEIGHTS["avoid"]
            
            # If any thinking methods returned a weight, divide by total weight,
            #   otherwise the moveToPosition is None
            if totalWeight != 0:
                moveToPosition /= totalWeight
            else:
                moveToPosition = None
        
        # If we have somewhere to move to
        if moveToPosition != None:
            # Debug draw option
            self._target = moveToPosition - self.getCenter()
            
            # Calculate a new velocity based on the moveToPosition
            newVelocity = moveToPosition - self.getCenter() 
            newVelocity.clip(self._maxVelocity)
            
            # If the difference between the current velocity and new velocity is less than
            #   the acceleration, then just snap to the new velocity
            if (newVelocity - self._velocity).magnitude() < seconds * self._acceleration:
                self._velocity = newVelocity
                
            # Otherwise, accelerate towards the new velocity
            else:
                newVelocity.clip(1)
                self._velocity += newVelocity * seconds * self._acceleration
                self._velocity.clip(self._maxVelocity)
            
            # Set the image's angle from the velocity's angle
            self.setAngleFromVelocity()
                        
        else:
            # Debug draw option
            self._target = None
            
            # If the flock should accelerate when left alone and the current velocity is less
            #   than the max velocity, accelerate in the current direction
            if self._velocity.magnitude() < self._maxVelocity and self._accelerateWhenAlone:
                self._velocity += self._velocity.normalized() * self._acceleration * seconds
                
            # If the flock should not accelerate when left alone, then slow down if alone
            elif not self._accelerateWhenAlone:
                # If we're moving
                if self._velocity.magnitude() != 0:
                    # If the magnitude is greater than the acceleration amount
                    if self._velocity.magnitude() > self._acceleration * seconds:
                        self._velocity -= self._velocity.normalized() * self._acceleration * seconds                        
                        self.setAngleFromVelocity()
                       
                    # Otherwise, just stop 
                    else:
                        self._velocity = Vector2(0, 0)
    
    def update(self, seconds, flock, kirby, boundaries):
        """Thinks to figure out the velocity and uses bounce behavior."""
        self.think(seconds, flock, kirby)
        
        newPosition = self.getTruePosition() + self._velocity * seconds
        
        # Set angle if we bounce
        if newPosition.x < 0 or newPosition.x > boundaries.x - self.getSize()[0]:
            self._velocity.x = -self._velocity.x
            self.setAngleFromVelocity()
        if newPosition.y < 0 or newPosition.y > boundaries.y - self.getSize()[1]:
            self._velocity.y = -self._velocity.y
            self.setAngleFromVelocity()
           
        newPosition = self.getTruePosition() + self._velocity * seconds
        
        self.setTruePosition(newPosition)
   