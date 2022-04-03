from ..gameObjects.vector2D import Vector2
from ..gameObjects.drawable import Drawable


SCREEN_SIZE = Vector2(400,400)

SCALE = 3
UPSCALED = SCREEN_SIZE * SCALE


def adjustMousePos(mousePos):
   return Vector2(*mousePos) // SCALE + Drawable.WINDOW_OFFSET