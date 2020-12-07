from pygame.math import Vector2


class Rocket:
    position = Vector2(500, 500+(147100000/500000))
    velocity = Vector2((30.29/500000), 0)
    acceleration = Vector2(0,0)
    mass = 500000