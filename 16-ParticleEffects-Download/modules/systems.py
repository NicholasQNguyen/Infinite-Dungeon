from .vector2D import Vector2
from .particles import *
import random

"""A basic particle system. Updates particles in a linear fashion based on the x
    and y velocity."""
class ParticleSystem(object):
   """System requires a single start position, the maximum number of particles allowed,
       and which particle type to create. Optionally the initial velocity and frequency
       at which the particles are created can be provided."""
   def __init__(self, position, particleType):
      self._particles = []
      self._position = Vector2(*position)
      self._maxParticles = 100
      self._initialVelocity = Vector2(0,0)
      self._frequency = 0.1
      self._particleType = particleType
      self._timer = (random.random() / 2 + 0.5) * self._frequency
      self._activeArea = pygame.Rect(0, 0, 100, 100)
      
      self._drawActiveArea = False
   
   def toggleActiveAreaDraw(self):
      self._drawActiveArea = not self._drawActiveArea
   
   def setMaxParticles(self, maxParticles):
      self._maxParticles = maxParticles
   
   def setInitialVelocity(self, initialVelocity):
      self._initialVelocity = initialVelocity
   
   def setFrequency(self, frequency):
      self._frequency = frequency
   
   def setActiveArea(self, xMin, yMin, xMax, yMax):
      self._activeArea = self._position + pygame.Rect(xMin, yMin, xMax, yMax)
   
   """Call update until the maximum number of particles is reached."""
   def simulate(self):
      while len(self._particles) < self._maxParticles:
         self.update(random.random() * self._frequency)
      
   """Update all existing particles. If enough time has passed, add another particle if
       there is room."""
   def update(self, seconds):
      self._timer -= seconds
      
      if len(self._particles) < self._maxParticles and self._timer < 0:
         self._timer = (random.random() / 2 + 0.5) * self._frequency
         self._particles.append(self._particleType(self.getPosition(), self._initialVelocity))
      
      for p in self._particles:
         self.updateParticle(p, seconds)
   
   """Update a particle based on the xMove and yMove of the system. Detects if a particle
       is outside the active area. Also invokes linger updates for lingering particles if
       the particle is not done."""
   def updateParticle(self, particle, seconds):
      
      if self._activeArea.collidepoint(*particle._position):
         velX = self._xMove(particle)
         velY = self._yMove(particle)
         
         particle.update(seconds, velX, velY)
      
      elif not particle.done():
         particle.updateLinger(seconds)
         
      else:
         particle.restart(self._initialVelocity, self.getPosition())
   
   """Invokes Drawable's draw for each particle in the system."""
   def draw(self, screen):
      for p in self._particles:
         p.draw(screen)
      
      if self._drawActiveArea:         

         pygame.draw.rect(screen, (0,255,0), self._activeArea, 1)
      
   """Standard x and y move are linear. Override these to make the movement behave differently."""
   def _yMove(self, particle):
      return particle.velocity.y
   
   def _xMove(self, particle):
      return particle.velocity.x
   
   """A basic getter method for the position. Allows overriding for random staring positions in
       inheritance."""
   def getPosition(self):
      return self._position
   
   
"""A basic particle system with a range of possible starting points. The starting position range is
    provided as a Rect to allow for 2D random starting points."""
class RangedParticleSystem(ParticleSystem):
   def __init__(self, position, particleType):
      super().__init__(position, particleType)
      
      self._height = 1
      self._width = 100
      
      self._setPositionRange()
   
   def _setPositionRange(self):      
      
      self._positionRangeX = Vector2(self._position.x, self._position.x + self._width)
      self._positionRangeY = Vector2(self._position.y, self._position.y + self._height)
   
   def setWidth(self, width=100):      
      self._width = width      
      self._setPositionRange()
   
   def setHeight(self, height):
      self._height = height
      self._setPositionRange()
      
      
   """Update the position to a random location within the position range any time the position is requested."""
   def getPosition(self):
      self._position = Vector2(random.randint(*self._positionRangeX), random.randint(*self._positionRangeY))
      
      return super().getPosition()
    
"""Accelerating particles in the y-axis."""
class ShowerSystem(ParticleSystem):
   def __init__(self, position):
      super().__init__(position, Shower)
      
      self.setInitialVelocity(Vector2(100,200))      
      self._activeArea = self._position + pygame.Rect(-200, 0, 400, 500)
   
   """Accelerates the y-speed of particles by 10% of the initial velocity."""
   def _yMove(self, particle):
      particle.velocity.y += 0.05 * particle.timer * self._initialVelocity.y      
      
      return particle.velocity.y     
   
   
    
"""Accelerating particles in the y-axis."""
class FountainSystem(ParticleSystem):
   def __init__(self, position):
      super().__init__(position, Shower)
      
      self.setInitialVelocity(Vector2(100,-200))      
      self._activeArea = self._position + pygame.Rect(-200, -480, 400, 500)
   
   """Accelerates the y-speed of particles by 10% of the initial velocity."""
   def _yMove(self, particle):
      particle.velocity.y += particle.timer * 5     
      
      return particle.velocity.y     
   
   
   
"""Linear rain system."""
class RainSystem(RangedParticleSystem):
   def __init__(self, position):
      super().__init__(position, Rain)
      
      self.setInitialVelocity(Vector2(50,1000))
      
      self._activeArea = self._position + pygame.Rect(-500, 0, 500*3, 500)

         
   
"""Oscillating snow ranged system. Active range must be larger than the world size so that left/right movement
    isn't cut off. If x-velocity is non-zero, this active range must increase as well."""
class SnowSystem(RangedParticleSystem):
   def __init__(self, position):
      super().__init__(position, Snow)
      
      
      
      self.setInitialVelocity(Vector2(0,150))
      
      self.octave = random.random() * 0.4 + 0.2
      self.amplitude = random.random() * 20 + 10
      
      self._activeArea = self._position + pygame.Rect(-500,0,500*3, 500)
   
   """Uses sine waves to oscillate xMovement."""
   def _xMove(self, particle):
      return (math.sin(particle.timer / self.octave) * self.amplitude + particle.velocity.x)
   
class CottonwoodSystem(RangedParticleSystem):
   def __init__(self, position):
      super().__init__(position, Snow)      
      
      self.setInitialVelocity(Vector2(50,-150))
      
      self.octave = random.random() * 0.4 + 0.2
      self.amplitude = random.random() * 20 + 10
      
      self._activeArea = self._position + pygame.Rect(-500,-800,500*3, 1500)
   
   """Uses sine waves to oscillate xMovement."""
   def _xMove(self, particle):
      return (math.sin(particle.timer / self.octave) * self.amplitude + particle.velocity.x)
   
   

"""Oscillating singular point system."""
class SmokeSystem(ParticleSystem):
   def __init__(self, position):
      super().__init__(position, Smoke)
      
      self.setInitialVelocity(Vector2(0, -200))
      self._activeArea = self._position + pygame.Rect(-100, -500, 200, 600)
      
   """Uses sine waves to oscillate xMovement."""
   def _xMove(self, particle):
      return math.sin(particle.timer / particle.octave) * particle.amplitude


         
   
