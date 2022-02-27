from ..gameObjects.vector2D import Vector2

SCREEN_SIZE = Vector2(800,800)

SCALE = 1
UPSCALED = SCREEN_SIZE * SCALE

def adjustMousePos(mousePos):
    return Vector2(*mousePos) // SCALE
