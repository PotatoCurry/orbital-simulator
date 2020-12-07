from pygame.math import Vector2


class Rocket:
    position = Vector2(500, 500+64+200)
    velocity = Vector2(3.87/100, 0) #velocity was in km/s, changed to pixel/s
    acceleration = Vector2(0,0)
    fuel_mass = 50000
    mass = 500000