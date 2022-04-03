
      
class KirbyState(object):
   def __init__(self, state="falling"):
      self._state = state
      
      self._movement = {
         "left" : False,
         "right" : False
      }
      
      self._lastFacing = "right"      
   
   def isMoving(self):
      return True in self._movement.values()
   
   def isGrounded(self):
      return self._state != "jumping" and self._state != "falling"
      
   def getState(self):
      return self._state
   
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
               
            if allStop and self.isGrounded():
               self._state = "standing"
               kirby.transitionState(self._state)
      
      elif action == "jump" and self.isGrounded():
         self._state = "jumping"
         kirby.transitionState(self._state)
         
      elif action == "fall" and self._state != "falling":
         self._state = "falling"
         kirby.transitionState(self._state)
         
      elif action == "ground" and not self.isGrounded():         
         if self.isMoving():
            self._state = "walking"
         else:
            self._state = "standing"
         kirby.transitionState(self._state)        

