from globals import planets, GRAVITATIONAL_CONSTANT
import pygame
from pygame.math import Vector2
from math import atan2, sin, cos, sqrt

class Planet:
    def __init__(self, x, y, radius, mass, id, color, Xi, Yi ):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.id = id
        self.velocity = Vector2(0, 0)
        self.color=color
        self.velocity.x = Xi
        self.velocity.y = Yi

    def update(self):
        self.getVelocity()
        self.x += self.velocity.x
        self.y += self.velocity.y
       
    def getVelocity(self):
        for planet in planets:
            if self.id != planet.id:
                dx = planet.x - self.x
                dy = planet.y - self.y
                angle = atan2(dy, dx)  # Calculate angle between planets
                d = sqrt((dx ** 2) + (dy ** 2))  # Calculate distance

                if d == 0:
                    d = 0.000001  # Prevent division by zero error

                f = (
                    GRAVITATIONAL_CONSTANT * self.mass * planet.mass / (d ** 2)
                )  # Calculate gravitational force

                self.velocity.x += (cos(angle) * f) / self.mass
                self.velocity.y += (sin(angle) * f) / self.mass
                print(self.velocity.x)

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(self.radius)
        )
      

