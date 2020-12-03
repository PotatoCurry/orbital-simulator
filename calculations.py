from math import atan2, sin, cos

from pygame import Vector2

REAL_EARTH_RADIUS = 6371  # 6,371 km
REAL_EARTH_MASS = 5.972e24  # 5.972 * 10^24 kg
GRAVITATIONAL_CONSTANT = 6.67408e-11
NORMALIZATION_CONSTANT = 0.1 / REAL_EARTH_RADIUS


def gravitational_acceleration(rocket_position: Vector2, earth_position):
    distance = rocket_position.distance_to(earth_position)
    angle = angle_to_earth(rocket_position, earth_position)
    magnitude = (GRAVITATIONAL_CONSTANT * REAL_EARTH_MASS) / pow(denormalize_distance(distance), 2)
    return Vector2(-magnitude * cos(angle), magnitude * sin(angle))


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
