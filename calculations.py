from math import atan2, sin, cos

from pygame import Vector2

from globals import EARTH_MASS, GRAVITATIONAL_CONSTANT, ROCKET_MASS, NORMALIZATION_CONSTANT


# Find the acceleration of gravity on the rocket
def gravitational_acceleration(rocket, earth_position):
    distance = rocket.position.distance_to(earth_position)
    angle = angle_to_earth(rocket.position, earth_position)
    magnitude = (GRAVITATIONAL_CONSTANT * EARTH_MASS) / pow(denormalize_distance(distance)*1000, 2)
    return Vector2(magnitude * -cos(angle), magnitude * sin(angle))


# Find the acceleration of the rocket itself, burning fuel in the process
def fuel_to_acceleration(rocket):
    angle = 1.7
    total_rocket_mass = ROCKET_MASS + rocket.fuel_mass
    thrust_acceleration_magnitude = 0
    if rocket.fuel_mass > 0:
        rocket.fuel_mass -= 1000
        thrust_acceleration_magnitude = 25000000 / total_rocket_mass
    return Vector2(thrust_acceleration_magnitude * cos(angle), thrust_acceleration_magnitude * -sin(angle))


def angle_to_earth(rocket_position: Vector2, earth_position: Vector2):
    dx = rocket_position.x - earth_position.x
    dy = rocket_position.y - earth_position.y
    return atan2(-dy, dx)


# Adapt real-life distances to screen size lengths
def normalize_distance(distance):
    return distance * NORMALIZATION_CONSTANT


# Adapt screen size lengths to real-life distances
def denormalize_distance(distance):
    return distance / NORMALIZATION_CONSTANT
