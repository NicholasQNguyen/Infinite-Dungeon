from ..gameObjects.vector2D import Vector2


SCREEN_SIZE = Vector2(300,200)

SCALE = 3
UPSCALED = SCREEN_SIZE * SCALE


def adjustMousePos(mousePos):
   return Vector2(*mousePos) // SCALE