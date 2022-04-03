from .drawable import Drawable


class Goal(Drawable):
   
   def __init__(self, position):
      super().__init__("star.png", position)