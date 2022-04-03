

class LevelState(object):
   def __init__(self, state="running"):
      self._state = state
   
   def manageState(self, action, levelManager):
      if action == "nextLevel" and self._state == "running":
         self._state = "startLoading"
         levelManager.transitionState("nextLevel")
            
      elif action == "doneLoading" and self._state == "startLoading":
         self._state = "running"
      
      elif action == "restart" and self._state == "running":
         self._state = "startLoading"
         levelManager.transitionState("restart")
   
   def __eq__(self, other):
      return self._state == other

class LevelStateThreaded(LevelState):
   def manageState(self, action, levelManager):
      if action == "load" and self._state == "startLoading":
         self._state = "loading"
      elif action == "doneLoading" and self._state == "loading":
         self._state = "running"
      else:
         super().manageState(action, levelManager)
