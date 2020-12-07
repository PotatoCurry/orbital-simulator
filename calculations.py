from math import atan2, sin, cos, sqrt

from pygame import Vector2

from globals import SUN_MASS, GRAVITATIONAL_CONSTANT, NORMALIZATION_CONSTANT, SUN_POS


# Find the acceleration of gravity on the rocket
def sun_gravity(location: Vector2):
    distance = sqrt(pow(location.x-SUN_POS.x,2)+pow(location.y-SUN_POS.y,2))
    angle = angle_to_sun(location, Vector2(500,500))
    magnitude = normalize_distance((GRAVITATIONAL_CONSTANT * SUN_MASS) / pow(denormalize_distance(distance)*1000, 2))/1000
    return Vector2(magnitude * -cos(angle), magnitude * sin(angle))


def angle_to_sun(rocket_position: Vector2, sun_position: Vector2):
    dx = rocket_position.x - sun_position.x
    dy = rocket_position.y - sun_position.y
    return atan2(-dy, dx)


# Adapt real-life distances to screen size lengths
def normalize_distance(distance):
    return distance * NORMALIZATION_CONSTANT


# Adapt screen size lengths to real-life distances
def denormalize_distance(distance):
    return distance / NORMALIZATION_CONSTANT
