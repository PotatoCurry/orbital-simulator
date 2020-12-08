from calculations import denormalize_distance, sun_gravity, normalize_distance
from globals import planetsList, GRAVITATIONAL_CONSTANT, TIME_CONSTANT
import pygame
from pygame.math import Vector2
from math import atan2, sin, cos, sqrt


class Planet:
    def __init__(self, position: Vector2, mass, id, color, Xi, Yi, size):
        self.position = position #pixel
        self.mass = mass #kilogram
        self.id = id
        self.velocity = Vector2(0, 0) #pixel/s
        self.color=color
        self.velocity.x = Xi #pixel/s
        self.velocity.y = Yi
        self.size = size

    def update(self):
        self.getVelocity()
        self.position += self.velocity / TIME_CONSTANT


    def getVelocity(self):
        for planet in planetsList:
            if self.id != planet.id:
                dx = denormalize_distance(self.position.x - planet.position.x)*1000 #pixels to 500000km to meters
                dy = denormalize_distance(self.position.y - planet.position.y)*1000 #pixels to 500000km to meters
                angle = atan2(dy, dx)  # Calculate angle between planets
                d = sqrt(pow(dx,2) + pow(dy,2))  # Calculate distance

                f = (
                    normalize_distance(GRAVITATIONAL_CONSTANT * planet.mass / pow(d*1000,2))*1000 #meters to km to pixels
                )  # Calculate gravitational force

                self.velocity.x += (-cos(angle) * f) / TIME_CONSTANT
                self.velocity.y += (sin(angle) * f) / TIME_CONSTANT
        self.velocity.x += sun_gravity(self.position).x / TIME_CONSTANT
        self.velocity.y += sun_gravity(self.position).y / TIME_CONSTANT

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.color, self.position, self.size
        )
      

