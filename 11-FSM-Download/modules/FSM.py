
class BasicState(object):
   def __init__(self, facing="none"):
      self._facing = facing
      
   def getFacing(self):
      return self._facing

   def _setFacing(self, direction):
      self._facing = direction
      
class KirbyState(object):
   def __init__(self, state="standing"):
      self._state = state
      self._movement = {
         "up" : False,
         "down" : False,
         "left" : False,
         "right" : False
      }
      
      self._lastFacing = "right"
      self._inWater = False

   def getFacing(self):
      if self._movement["left"] == True:
         self._lastFacing = "left"
      elif self._movement["right"] == True:
         self._lastFacing = "right"
      
      return self._lastFacing

   def manageState(self, action, kirby):
      if action in self._movement.keys():
         if self._movement[action] == False:
            self._movement[action] = True
            if self._state == "standing":
               self._state = "walking"
               if self._inWater:
                  kirby.transitionState("swimming")
               else:
                  kirby.transitionState(self._state)
            
      elif action.startswith("stop") and action[4:] in self._movement.keys():
         direction = action[4:]
         if self._movement[direction] == True:            
            self._movement[direction] = False
            allStop = True
            for move in self._movement.keys():
               if self._movement[move] == True:
                  allStop = False
                  break
               
            if allStop:
               self._state = "standing"
               if not self._inWater:
                  kirby.transitionState(self._state)

      elif action.endswith("water"):
         if action.startswith("start"):
            if not self._inWater:
               self._inWater = True
               kirby.transitionState("swimming")

         elif action.startswith("stop"):
            if self._inWater:
               self._inWater = False
               kirby.transitionState("walking")
    
     
   def getState(self):
      return self._state
      
   
