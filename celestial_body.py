from calculations import denormalize_distance, sun_gravity, normalize_distance
from globals import planetsList, GRAVITATIONAL_CONSTANT, SUN_MASS, SUN_POS
import pygame
from pygame.math import Vector2
from math import atan2, sin, cos, sqrt


class CelestialBody:
    def __init__(self, name, position: Vector2, mass, id, color, Xi, Yi, size):
        self.position = position  # pixel
        self.mass = mass  # kilogram
        self.id = id
        self.velocity = Vector2(0, 0)  # pixel/s
        self.color=color
        self.velocity.x = Xi  # pixel/s
        self.velocity.y = Yi
        self.size = size
        self.angle = 0
        self.f = 0
        self.name = name
        self.tEnergy = 0

    def update(self, time_constant):
        print(time_constant)
        #add velocities 
        self.velocity.x += (-cos(self.angle) * self.f) / time_constant
        self.velocity.y += (sin(self.angle) * self.f) / time_constant
        self.velocity.x += sun_gravity(self.position).x / time_constant
        self.velocity.y += sun_gravity(self.position).y / time_constant
        self.position += self.velocity / time_constant
        #energy calculation
        self.tEnergy = 0
        #energy with other planets
        for planet in planetsList: #loop through planets
            if self.id != planet.id: # check if planet is not itself
                dx = denormalize_distance(self.position.x - planet.position.x) * 1000  # pixels to 500000km to meters
                dy = denormalize_distance(self.position.y - planet.position.y) * 1000
                # calculate velocity^2
                velSquare = pow(denormalize_distance(self.velocity.x) * 1000, 2) + pow(denormalize_distance(self.velocity.y) * 1000, 2)
                self.tEnergy -= ( #second half of the equation - potential energy = GMm/r^2
                        (GRAVITATIONAL_CONSTANT*planet.mass*self.mass*(1/sqrt(dx**2+dy**2)))
                )
        #energy with sun
        dx = denormalize_distance(self.position.x - SUN_POS.x) * 1000 # pixels to 500000km to meters
        dy = denormalize_distance(self.position.y - SUN_POS.y) * 1000
        velSquare = pow(denormalize_distance(self.velocity.x)*1000,2)+pow(denormalize_distance(self.velocity.y)*1000,2)
        self.tEnergy += (
            ((self.mass / 2) * velSquare) - ((GRAVITATIONAL_CONSTANT*SUN_MASS*self.mass)*(1/sqrt(dx**2+dy**2))) #energy equation for the sun
        )

    def update_acceleration(self):
        for planet in planetsList:
            if self.id != planet.id:
                dx = denormalize_distance(self.position.x - planet.position.x)*1000  # pixels to 500000km to meters
                dy = denormalize_distance(self.position.y - planet.position.y)*1000  # pixels to 500000km to meters
                self.angle = atan2(dy, dx)  # Calculate angle between planets
                d = sqrt(pow(dx, 2) + pow(dy, 2))  # Calculate distance
                self.f = (
                    normalize_distance(GRAVITATIONAL_CONSTANT * planet.mass / pow(d, 2))/1000  # meters to km to pixels
                )  # Calculate gravitational force

    def draw(self, screen): #draw planet onto display
        pygame.draw.circle( 
            screen, self.color, self.position, self.size
        )
