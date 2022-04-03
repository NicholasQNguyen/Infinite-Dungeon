

class ScreenState(object):
   def __init__(self, state="mainMenu"):
      self._state = state
      self._paused = False
   
   def manageState(self, action, screenManager):
      if action == "pause" and self._state == "game":
         self._paused = not self._paused
         screenManager.transitionState(self._state)
      
      elif action == "mainMenu" and not self._paused and self._state != "mainMenu":
         self._state = "mainMenu"
         screenManager.transitionState(self._state)
      
      elif action == "startGame" and self._state != "game":
         self._state = "game"
         screenManager.transitionState(self._state)
      
      elif action == "gameOver" and self._state != "gameOver":
         self._state = "gameOver"
         screenManager.transitionState(self._state)
      
      elif action in ["cursor", "event", "hoverclick"] and self._state != "mainMenu":
         self._state = "mainMenu"
         screenManager.setMainMenu(action)
         screenManager.transitionState(self._state)
      
         
   
   def __eq__(self, other):
      return self._state == other

   def isPaused(self):
      return self._paused
   
   def menuType(self):
      return self._menuType
