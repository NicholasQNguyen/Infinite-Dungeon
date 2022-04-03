from .rotated import Rotatable
from .vector2D import Vector2
from ..UI.screenInfo import adjustMousePos
import pygame
import random
import math

class Flocky(Rotatable):
    
   
    def __init__(self, position):
        super().__init__("arrow.png", position)
        
        self._maxVelocity = 40
        self._sightDistance = 100
        self._personalDistance = 50
        
        
        self._velocity = Vector2(random.randint(-100,100), random.randint(-100, 100))
        self._velocity.scale(self._maxVelocity)
        
        self._rotationalAcceleration = math.pi / 128
        
        self._unrotatedImage = pygame.transform.rotate(self._unrotatedImage, 180)
        
        
        self.setAngleFromVelocity()
        
        self._debugDraw = False
        self._target = None
        self._displayAveragePosition = Vector2(0,0)
        self._mousePos = Vector2(0,0)
    
    def draw(self, surface):
        super().draw(surface)
        
        if self._debugDraw:
            pygame.draw.circle(surface, (0,0,255), self.getCollisionRect().center, self._personalDistance, 2)
            pygame.draw.circle(surface, (0,0,255), self.getCollisionRect().center, self._sightDistance, 1)
            pygame.draw.line(surface, (0,255,0), list(self._position + self._image.get_rect().center), list(self._position + self._image.get_rect().center + self._velocity), 3)
            if self._target != None:
                pygame.draw.line(surface, (255,0,0), list(self._position + self._image.get_rect().center), list(self._position + self._image.get_rect().center + self._target), 1)
            pygame.draw.circle(surface, (255,0,0), list(self._displayAveragePosition), 3)
        
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self._velocity.rotate(math.pi / 16)
            print(self._velocity, self._velocity.getAngle())
            self.setAngleFromVelocity()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self._velocity.rotate(-math.pi / 16)
            print(self._velocity, self._velocity.getAngle())
            self.setAngleFromVelocity()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self._debugDraw = not self._debugDraw
        elif event.type == pygame.MOUSEMOTION:
            self._mousePos = adjustMousePos(event.pos)
    
    
    def setAngleFromVelocity(self):
        self.setAngle(self._velocity.getAngle())
    
    def correctAngleSteering(self, angle):
        
        if angle > math.pi:
            angle -= math.pi * 2
        elif angle < -math.pi:
            angle += math.pi * 2
            
        return angle
        
    def separation(self, flock):
        steering = Vector2(0,0)
        tooClose = 0
        
        # for neighbor in flock:
        #     distance = (neighbor.getTruePosition() - self.getTruePosition()).magnitude()
        #     if distance < self._personalDistance:
        #         avoidAngle = self.correctAngleSteering(self.getTruePosition().getAngle() - neighbor.getTruePosition().getAngle())
        #         # temp = self.getTruePosition() - neighbor.getTruePosition().getAngle()
        #         avoidAngle /= distance ** 2
        #         steering.rotate(avoidAngle)
        #         tooClose += 1
        distance = (self._mousePos - self.getTruePosition()).magnitude()
        if distance < self._personalDistance:
            avoidAngle = self.correctAngleSteering(self.getTruePosition().getAngle() - self._mousePos.getAngle())
            # temp = self.getTruePosition() - neighbor.getTruePosition().getAngle()
            avoidAngle /= distance ** 2
            steering.rotate(avoidAngle)
            tooClose += 1
        
        # if tooClose != 0:
            # steering /= tooClose
            # steering -= self._velocity
            return (steering - self._velocity).getAngle()
    
        return 0
        
    def alignment(self, flock):        
        averageVelocity = Vector2(0,0)
        neighbors = 0
        
        
        for neighbor in flock:
            if (neighbor.getTruePosition() - self.getTruePosition()).magnitude() < self._sightDistance:
                averageVelocity += neighbor._velocity
                neighbors += 1
        
        if neighbors != 0:
            averageVelocity /= neighbors
        
            steering = averageVelocity - self._velocity            
        
            return self.correctAngleSteering(steering.getAngle())
    
        return 0
        
    def cohesion(self, flock):
        
        # vecToMouse = self._mousePos - self._position
        # 
        # if vecToMouse.magnitude() < self._sightDistance:
        #     
        #     angleDiff = self._velocity.getAngle() - vecToMouse.getAngle()
        #     return self.correctAngleSteering(angleDiff)
        
        averagePosition = Vector2(0,0)
        neighbors = 0
        
        
        for neighbor in flock:
            if (neighbor.getTruePosition() - self.getTruePosition()).magnitude() < self._sightDistance:
                averagePosition += neighbor.getTruePosition()
                neighbors += 1
        
        if neighbors != 0:
            averagePosition.x /= neighbors
            averagePosition.y /= neighbors
            self._displayAveragePosition = Vector2(*averagePosition)
        
            steering = self._displayAveragePosition - self.getTruePosition()
            
            angle = self._velocity.getAngle() - steering.getAngle()
        
            return self.correctAngleSteering(angle)
    
        return 0
    
        
        
    def think(self, flock):
        steer = 0
        
        others = [x for x in flock if not x is self]
        
        steer = self.cohesion(others)
               
        # if self._velocity.getAngle()
        
        # neighbors = self.getCollisionRect().inflate(self._sightDistance, self._sightDistance).collidelistall([x.getCollisionRect() for x in flock])
        # 
        # if len(neighbors) > 0:
        #     tooClose = self.getCollisionRect().inflate(self._personalDistance, self._personalDistance).collidelistall([x.getCollisionRect() for x in flock])            
        #                 
        #     neighborPositions = [flock[x].getTruePosition() for x in neighbors if x not in tooClose and flock[x] is not self]
        #     
        #     averagePosition = Vector2(0,0)
        #     for np in neighborPositions:
        #         averagePosition += np
        #     
        #     averagePosition /= len(neighbors)
        # 
        #     vecToAveragePosition = averagePosition - self.getTruePosition() 
        #     
        #     angleDiff = self._velocity.getAngle() - vecToAveragePosition.getAngle()            
        #     
        #     steer += angleDiff
            
            
        #     
        #     neighborVelocities = [flock[x]._velocity for x in neighbors]            
        #     
        #     averageVelocity = Vector2(0,0)
        #     for nv in neighborVelocities:
        #         averageVelocity += nv
        #         
        #     averageVelocity /= len(neighbors)
        #     
        #     angleDiff = self._velocity.getAngle() - averageVelocity.getAngle()
        #     
        #     velocitySteering = min(self._rotationalAcceleration, max(-self._rotationalAcceleration, angleDiff))
        #     
        #     steer += velocitySteering
                
            # print(tooClose)
            # if len(tooClose) != 0:
            #     for n in tooClose:
            #         if flock[n] is not self:
            #             vecToNeighbor = flock[n].getTruePosition() - self.getTruePosition() 
            #             
            #             angleDiff = vecToNeighbor.getAngle() - self._velocity.getAngle()               
            #             
            #             steer -= angleDiff
            #             
            #             if steer > math.pi * 2:
            #                 steer -= math.pi * 2
            #             elif steer < -math.pi * 2:
            #                 steer += math.pi * 2
                        
        if steer != 0:
            self._target = Vector2(*self._velocity)
            self._target.rotate(steer)
        else:
            self._target = None
        
        steer = min(self._rotationalAcceleration, max(-self._rotationalAcceleration, steer))
        
        self._velocity.rotate(steer)
        self.setAngleFromVelocity()
    
    def update(self, seconds, flock, boundaries):
        
        self.think(flock)
        
        newPosition = self.getTruePosition() + self._velocity * seconds
        
        if newPosition.x < 0 or newPosition.x > boundaries.x - self.getSize()[0]:
            self._velocity.x = -self._velocity.x
        if newPosition.y < 0 or newPosition.y > boundaries.y - self.getSize()[1]:
            self._velocity.y = -self._velocity.y
           
           
        newPosition = self.getTruePosition() + self._velocity * seconds
        
        self.setTruePosition(newPosition)
        self.setAngleFromVelocity()
        # self.setAngle(-self._velocity.getAngle())
        # self.setPosition(newPosition)
   