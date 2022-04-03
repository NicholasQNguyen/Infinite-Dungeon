from ..gameObjects.vector2D import Vector2
from ..gameObjects.drawable import Drawable


SCREEN_SIZE = Vector2(400,400)

SCALE = 2
UPSCALED = SCREEN_SIZE * SCALE


def adjustMousePos(mousePos):
   return Vector2(*mousePos) // SCALE + Drawable.WINDOW_OFFSET

def distributeHorizontally(num, width, pad=10):
   return (SCREEN_SIZE.x - pad * 2 - width) // (num - 1)