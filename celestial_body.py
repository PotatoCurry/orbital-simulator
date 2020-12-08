from calculations import denormalize_distance, sun_gravity, normalize_distance
from globals import planetsList, GRAVITATIONAL_CONSTANT, TIME_CONSTANT
import pygame
from pygame.math import Vector2
from math import atan2, sin, cos, sqrt


class CelestialBody:
    def __init__(self, name, position: Vector2, mass, id, color, Xi, Yi, size):
        self.position = position #pixel
        self.mass = mass #kilogram
        self.id = id
        self.velocity = Vector2(0, 0) #pixel/s
        self.color=color
        self.velocity.x = Xi #pixel/s
        self.velocity.y = Yi
        self.size = size
        self.angle = 0
        self.f = 0
        self.name = name

    def update(self):
        self.velocity.x += (-cos(self.angle) * self.f) / TIME_CONSTANT
        self.velocity.y += (sin(self.angle) * self.f) / TIME_CONSTANT
        self.velocity.x += sun_gravity(self.position).x / TIME_CONSTANT
        self.velocity.y += sun_gravity(self.position).y / TIME_CONSTANT
        self.position += self.velocity / TIME_CONSTANT

    def update_acceleration(self):
        for planet in planetsList:
            if self.id != planet.id:
                dx = denormalize_distance(self.position.x - planet.position.x)*1000 #pixels to 500000km to meters
                dy = denormalize_distance(self.position.y - planet.position.y)*1000 #pixels to 500000km to meters
                self.angle = atan2(dy, dx)  # Calculate angle between planets
                d = sqrt(pow(dx, 2) + pow(dy, 2))  # Calculate distance
                self.f = (
                    normalize_distance(GRAVITATIONAL_CONSTANT * planet.mass / pow(d,2))/1000 #meters to km to pixels
                )  # Calculate gravitational force

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.color, self.position, self.size
        )
      

