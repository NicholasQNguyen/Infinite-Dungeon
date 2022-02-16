from .drawable import Drawable
from .vector2D import Vector2
import random
import pygame
import math

"""A basic particle class from which all particles inherit. Applys linear movement."""
class Particle(Drawable):
   
   """Initializes a particle at the startPosition, making a copy of the startPosition
       to prevent cloning of the Vector2. Creates the pygame surface for drawing."""
   def __init__(self, startPosition, particleSize=(10,10)):
      super().__init__("", Vector2(*startPosition))
      
      self._startPosition = Vector2(*startPosition)
      self._image = pygame.Surface(particleSize, pygame.SRCALPHA)
      
      self.timer = 0
      self.velocity = Vector2(0,0)
      
   """Update the particle based on the given velocity and seconds"""
   def update(self, seconds, velX, velY):
      self.timer += seconds
      
      self._position.x += velX * seconds
      self._position.y += velY * seconds
      
   """Dummy method so that all particles are considered "done" unless they are lingering."""
   def done(self):
      return True
   
   """Reuse the particle by returning to the start position."""
   def restart(self):
      self._position.x = self._startPosition.x
      self._position.y = self._startPosition.y
   
   """General setVelocity to force a small amount of jitter to any values.
       Less jitter means that the particles may "line up" eventually."""
   def setVelocity(self, velocity, jitter=0.1):
      self.velocity.x = velocity.x * ((random.random() * jitter * 2 - jitter) + 1 - jitter)
      self.velocity.y = velocity.y * ((random.random() * jitter * 2 - jitter) + 1 - jitter)
      
"""A particle which does not reset immidiately, but waits for a death timer."""
class LingeringParticle(Particle):
   """Adds a death timer to the particle."""
   def __init__(self, startPosition, lingerTime):
      super().__init__(startPosition)
      self._deathTimerStart = self._deathTimer = lingerTime
   
   """Only done if the death timer is less than or equal to zero."""
   def done(self):
      return self._deathTimer <= 0

   """Special update to let the death timer tick down."""
   def updateLinger(self, seconds):
      self._deathTimer -= seconds

   """When restarting the death timer must also be reset."""
   def restart(self, initialVelocity=Vector2(0,0), newPosition=None):
      super().restart()
      self._deathTimer = self._deathTimerStart
      
   
"""A particle which gains speed as it falls."""
class Shower(Particle):
   def __init__(self, startPosition, initialVelocity=Vector2(0,0)):
      super().__init__(startPosition)
      
      self.restart()
      
      pygame.draw.circle(self._image, pygame.Color(200, 200, 255, 150), (5,5), 3)
      
   """Set x velocity to a random direction between -1 and 1 of the initial velocity."""
   def restart(self, initialVelocity=Vector2(0,0), newPosition=None):
      if newPosition != None:
         self._position=Vector2(*newPosition)
         
      self.setVelocity(Vector2(initialVelocity.x * (random.random() * 2 - 1), initialVelocity.y))
      self.timer = 0
      super().restart()
      
      
      
"""A linear particle which draws a line for its visualization relative to its speed."""
class Rain(Particle):
   def __init__(self, startPosition, initialVelocity=Vector2(0,0)):
      super().__init__(startPosition, (15, 15))
      self.setVelocity(initialVelocity)
      self._length = Vector2(self.velocity.x, self.velocity.y)
      self._length.scale(10)
      
      
      pygame.draw.line(self._image, pygame.Color(200, 200, 255, 150), (0,0),
                       list(map(int, self._length)), 2)
   
   """Only changes position if a new position was provided."""
   def restart(self, initialVelocity=Vector2(0,0), newPosition=None):
      if newPosition != None:
         self._position=Vector2(*newPosition)
      
      super().restart()
     
      
"""An oscillating particle which starts from a single point. Color becomes fainter as
    it gets further up the screen."""
class Smoke(Particle):
   def __init__(self, startPosition, initialVelocity=Vector2(0,0)):
      super().__init__(startPosition)
      self.restart(initialVelocity)
      
   """Update changes the alpha aspect of the color of the circle."""
   def update(self, seconds, velX, velY):
      super().update(seconds, velX, velY)
      
      self._color[3] = max(0,int((self._position.y / self._startPosition.y) ** 3 * 255))
      pygame.draw.circle(self._image, self._color, (5,5), self._radius)

   """Set octave, amplitude to random values. Set color to a gray color between 128 and 180."""
   def restart(self, initialVelocity, newPosition=None):
      color = random.randint(128,180)
      self.octave = random.random() * 0.5 + 0.05
      self.amplitude = random.random() * 30
      self.timer = (math.pi * self.octave) / 2 
      self._radius = random.randint(2,4)
      if random.randint(0,1):
         self.timer += math.pi * self.octave
      
      self._startTimer = self.timer
      self._color = [color, color, color, 255]
      
      self.setVelocity(initialVelocity, 0.25)
      
      super().restart()
      
"""An oscillating particle which falls faster if its larger."""
class Snow(LingeringParticle):
   def __init__(self, startPosition, initialVelocity=Vector2(0,0)):
      super().__init__(startPosition, 0.5)
      
      self.restart(initialVelocity, startPosition)
      
   """Set the radius of the circle to a random value between 1 and 4 and then update the y-velocity based
       on that size."""
   def restart(self, initialVelocity, newPosition=None):
      
      self._radius = random.randint(1,4)
      
      color = random.randint(200,255)
      self._image.fill(pygame.Color(0,0,0,0))
      pygame.draw.circle(self._image, pygame.Color(color, color, 255, 250), (5,5), self._radius)
      
      if newPosition != None:
         self._position=Vector2(*newPosition)
         
      
      self.setVelocity(Vector2(initialVelocity.x, self._radius * 20 + initialVelocity.y))
      
      super().restart(initialVelocity, newPosition)
      
   
   
