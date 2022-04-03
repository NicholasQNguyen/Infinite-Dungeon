
class MobileState(object):
   def __init__(self, state="standing"):
      self._state = state
      self._movement = {         
         "up" : False,
         "down" : False,
         "left" : False,
         "right" : False
      }
      
      self._lastFacing = "right"
      
   def getFacing(self):
      if self._movement["left"] == True:
         self._lastFacing = "left"
      elif self._movement["right"] == True:
         self._lastFacing = "right"
      
      return self._lastFacing
         
   def getState(self):
      return self._state
   
   def isMoving(self):
      return True in self._movement.values()
   
   
   def manageState(self, action, obj):
      if action in self._movement.keys():
         if self._movement[action] == False:
            self._movement[action] = True
            if self._state == "standing":
               self._state = "walking"
               obj.transitionState(self._state)
         
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
               obj.transitionState(self._state)
      elif action == "stopall":
         if self._state != "standing":
            for direction in self._movement.keys():
               self._movement[direction] = False
               
            self._state = "standing"
            obj.transitionState(self._state)
   
   
