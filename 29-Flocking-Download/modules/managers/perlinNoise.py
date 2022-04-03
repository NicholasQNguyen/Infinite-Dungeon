import pygame, math, random

class PerlinNoise(object):
   
   def __init__(self, screenSize):
      self._displayType = "landmap"
      self._levels = 6
      self._chunk = 32
      self._tileSize = 64 * 2
      self._displayLevels = 1
      self._displayOne = False
      
      self._seed = 1337
      
      self._screenSize = screenSize
      
      self._surfaces = {
         "grayscale" : pygame.Surface(list(screenSize)),
         "landmap"   : pygame.Surface(list(screenSize))
      }
      
      self._tile = True
      self._tileLines = True
      
      
      
      self._primes = [37589, 39733, 43397, 47417, 51503, 54011, 58603, 61979,
                      69313, 70249, 73757, 73721, 80177, 82571, 83449, 85021,
                      87211, 89329, 91967, 94421, 96167, 98869, 99989, 101293]
      
      self.reset()
      
   
   def reset(self):
      
      self._data = [[[0 for x in range(self._screenSize.x)] for y in range(self._screenSize.y)] for l in range(self._levels)]
      
      self.fillData()
      self.fillSurfaces()
     
   def lerp(self, value, start, end):
      return (end - start) * value + start

   def sinusoidal(self, value, start, end):
      return self.lerp(1 - (math.cos(value * math.pi) / 2 + 0.5), start, end)
   
   def fillData(self):
      for level in range(self._levels):
         chunkSize = self._chunk / 2 ** level
         print("Filling octave", level + 1)
         prime = self._primes[((level + self._seed) * 5) % len(self._primes)]
         prime2 = self._primes[((level + self._seed) * 7) % len(self._primes)]
         for y in range(len(self._data[level])):
            for x in range(len(self._data[level][y])):
               
               startX = x
               startY = y
               nx = startX + chunkSize
               ny = startY + chunkSize
               
               if self._tile:
                  startX %= self._tileSize
                  startY %= self._tileSize
                  nx %= self._tileSize
                  ny %= self._tileSize
                  
                  
               startX = int(startX // chunkSize)
               startY = int(startY // chunkSize)
               nextX = int(nx // chunkSize)
               nextY = int(ny // chunkSize)
               
               
               
               topLeft = self.getValue(startX * prime, startY * prime2)
               topRight = self.getValue(nextX * prime, startY * prime2)
               bottomLeft = self.getValue(startX * prime, nextY  * prime2)
               bottomRight = self.getValue(nextX  * prime, nextY  * prime2)
               
               xPercent = x % chunkSize / chunkSize
               yPercent = y % chunkSize / chunkSize
               
               topValue = self.sinusoidal(xPercent, topLeft, topRight)
               bottomValue = self.sinusoidal(xPercent, bottomLeft, bottomRight)
               
               value = self.sinusoidal(yPercent, topValue, bottomValue)
               
               self._data[level][y][x] = value
         
         
   
   def fillSurfaces(self):
      for displayType in self._surfaces.keys():
         self._fillSurface(displayType)
         
      print("done filling")
      
   def _fillSurface(self, displayType):
      print("filling", displayType)
      for y in range(len(self._data[0])):
         for x in range(len(self._data[0][0])):
            if self._displayOne:
               colorValue = self._data[self._displayLevels - 1][y][x]
            else:
               colorValue = sum([self._data[l][y][x] / (2 ** l) for l in range(self._displayLevels)]) / sum([1/(2 ** l) for l in range(self._displayLevels)])
            self._surfaces[displayType].set_at((x, y), self.getColor(displayType,colorValue))
      
            
      
   def getColor(self, displayType, value):
      if displayType == "grayscale":
         return [int(value * 255) for x in range(3)]
      elif displayType == "landmap":
         if value > 0.5:
            return [self.lerp((value - 0.5) * 2,0,255),
                    self.lerp((value - 0.5) * 2,130,255),
                    self.lerp((value - 0.5) * 2,18,206)]
   
         else:
            return [self.lerp(value * 2, 42, 12),
                    self.lerp(value * 2, 8, 20),
                    self.lerp(value * 2, 65, 150)]
         
   def getValue(self, x, y):
      x *= self._seed
      y *= self._seed
      
      # mix around the bits in x:
      x = x * 3266489917 + 374761393
      x = (x << 17) | (x >> 15)
    
      # mix around the bits in y and mix those into x:
      x += y * 3266489917
    
      # Give x a good stir:
      x *= 668265263
      x ^= x >> 15
      x *= 2246822519
      x ^= x >> 13
      x *= 3266489917
      x ^= x >> 16
    
      #trim the result and scale it to a float in [0,1):
      return (x & 0x00ffffff) * (1.0 / 0x1000000)
   
   def draw(self, surface):
      surface.blit(self._surfaces[self._displayType], (0,0))
      
      if self._tile and self._tileLines:
         for x in range(0, self._screenSize[0], self._tileSize):
            pygame.draw.line(surface, (255,0,0), (x, 0), (x, self._screenSize[1]))
         
         for y in range(0, self._screenSize[1], self._tileSize):
            pygame.draw.line(surface, (255,0,0), (0, y), (self._screenSize[0], y))
            
            
      
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP and self._displayLevels < self._levels:
            self._displayLevels += 1
            self.fillSurfaces()
         elif event.key == pygame.K_DOWN and self._displayLevels > 1:
            self._displayLevels -= 1
            self.fillSurfaces()
            
         elif event.key == pygame.K_RETURN:
            self._seed = random.randint(1,1000000)
            self.reset()
         
         elif event.key == pygame.K_SPACE:
            if self._displayType == "landmap":
               self._displayType = "grayscale"
            else:
               self._displayType = "landmap"
            
         
         elif event.key == pygame.K_0:
            self._displayOne = not self._displayOne
            
            print("Display all:", self._displayOne == False)
            
            self.fillSurfaces()
         
         
         elif event.key == pygame.K_t:
            self._tile = not self._tile
            
            print("Tiled:", self._tile)
            
            self.reset()
            
            
            
         
      
      
       
         
   
   def update(self, seconds):
      pass
      
         
         
         