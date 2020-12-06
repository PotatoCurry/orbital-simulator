import pygame
from pygame.math import Vector2

from calculations import gravitational_acceleration, fuel_to_acceleration
from globals import TIME_CONSTANT, FPS
from rocket import Rocket

pygame.init()

# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
GAME_EARTH_POSITION = Vector2(WIDTH / 2, HEIGHT / 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20)

# Rocket movement
rocket = Rocket()

# Run until the user asks to quit
running = True
while running:
    # Constant refresh instructions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if closed
            running = False
    screen.fill((0, 0, 0))  # Fill the background with black
    pygame.draw.circle(screen, (0, 0, 255), GAME_EARTH_POSITION, 100)  # Draw the Earth

    # Define the rocket
    rocket_surface = pygame.Surface((50, 50))
    rocket_surface.fill((255, 255, 255))
    rocket_rect = rocket_surface.get_rect()

    # Rocket calculations
    rocket_acceleration = gravitational_acceleration(rocket, GAME_EARTH_POSITION) + fuel_to_acceleration(rocket)
    # fuel_mass -= 10 / TIME_CONSTANT
    # rocket_acceleration = fuel_to_acceleration(rocket_position, GAME_EARTH_POSITION)
    rocket.velocity += rocket_acceleration / TIME_CONSTANT
    rocket.position += rocket.velocity / TIME_CONSTANT

    # TODO: Denormalize to real values
    info0 = font.render('Time Elapsed: ' + str(round(pygame.time.get_ticks()/1000)), True, (255,0,255))
    info1 = font.render('X Position: ' + str(rocket.position.x), True, (255, 0, 255))
    info2 = font.render('Y Position: ' + str(rocket.position.y), True, (255, 0, 255))
    info3 = font.render('X Velocity: ' + str(rocket.velocity.x), True, (255, 0, 255))
    info4 = font.render('Y Velocity: ' + str(rocket.velocity.y), True, (255, 0, 255))
    info5 = font.render('X Acceleration: ' + str(rocket_acceleration.x), True, (255, 0, 255))
    info6 = font.render('Y Acceleration: ' + str(rocket_acceleration.y), True, (255, 0, 255))
    info7 = font.render('Fuel Mass: ' + str(rocket.fuel_mass), True, (255, 0, 255))

    # Draw to the display
    screen.blit(rocket_surface, rocket.position)
    screen.blit(info0, (20, 0))
    screen.blit(info1, (20, 20))
    screen.blit(info2, (20, 40))
    screen.blit(info3, (20, 60))
    screen.blit(info4, (20, 80))
    screen.blit(info5, (20, 100))
    screen.blit(info6, (20, 120))
    screen.blit(info7, (20, 140))
    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
