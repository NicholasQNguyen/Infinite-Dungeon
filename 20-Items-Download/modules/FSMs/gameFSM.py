

class GameState(object):
   def __init__(self, state="running"):
      self._state = state
   
   def manageState(self, action):
      if action == "mainMenu" and self._state != "mainMenu":
         self._state = "mainMenu"
         
      elif action == "cursorMenu" and self._state != "cursorMenu":
         self._state = "cursorMenu"
         
      elif action == "start" and self._state != "running":
         self._state = "running"
         
   
   def __eq__(self, other):
      return self._state == other