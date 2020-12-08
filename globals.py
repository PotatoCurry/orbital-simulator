from pygame import Vector2

FPS = 60

TIME_CONSTANT = .00006  # Used to adjust

SUN_RADIUS = 695500  #km
SUN_MASS = 1.989e30  # 5.972 * 10^24 kg
SUN_POS = Vector2(500,500)
GRAVITATIONAL_CONSTANT = 6.67408e-11
NORMALIZATION_CONSTANT = 1 / 500000 #1 pixel / 500000 km

planetsList = []
