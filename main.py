import pygame
from pygame.math import Vector2

from calculations import denormalize_distance, normalize_distance
from globals import FPS, planetsList, SUN_POS
from celestial_body import CelestialBody
from textbox import InputBox
pygame.init()

# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20)

# Adding Planets
#earth
planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(147100000)), 5.97219e24, 0, (0, 0, 255), normalize_distance(30.29), 0, 5))
#moon
#planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(147100000 + 384400)), 7.34767309e22, 1, (255, 255, 255), normalize_distance(30.29+1.022), 0, 1))
#mercury
planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(68492000)), 3.285e23, 1, (200, 100, 30), normalize_distance(48), 0, 3))
#venus
planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(107860000)), 4.867e24, 2, (200, 20, 20), normalize_distance(35.02), 0, 4))
#mars
planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(222480000)), 6.39e23, 3, (200, 20, 20), normalize_distance(24.1), 0, 4))
#Init vel and angle text boxes
input_velx = InputBox(120, 850, 140, 32)  #x y w h
input_vely = InputBox(120, 900, 140, 32)
input_ang = InputBox(120, 950, 140, 32)
input_boxes = [input_velx, input_vely, input_ang] 

# Run until the user asks to quit
running = True

start = False  #simulation started or not
play = False  #simulation play or pause

rocket_acceleration = Vector2(0,0)  #save acceleration so display works when paused

while running:
    # Constant refresh instructions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if closed
            running = False
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #space play/pauses 
                if not start:
                    start = True 
                else:
                    play = not play
            #if event.key ==pygame.K_R: #restart

                
    screen.fill((0, 0, 0))  # Fill the background with black

    pygame.draw.line(screen,(50,50,50),(500,0),(500,1000))
    pygame.draw.line(screen,(50,50,50),(0,500),(1000,500))

    pygame.draw.circle(screen, (255, 255, 0), SUN_POS, 64)  # Draw the Sun
    

    if play:  #after start
        for planet in planetsList:
            planet.update_acceleration()
        for planet in planetsList:
            planet.update()
      
        time = round(pygame.time.get_ticks()/1000)
    else:
        #keep time at zero before starting
        if not start:  #init values in text boxes
            time = 0

    # TODO: Properly determine the denormalized values
    info0 = font.render('Time Elapsed: ' + str(time)+ " seconds", True, (255,0,255))
    #info1 = font.render('X Position: ' + str(round(denormalize_distance(rocket.position.x-SUN_POSITION.x)))+ " km", True, (255, 0, 255))
    #info2 = font.render('Y Position: ' + str(round(-denormalize_distance(rocket.position.y-SUN_POSITION.y)))+ " km", True, (255, 0, 255))
    #info3 = font.render('X Velocity: ' + str(round(denormalize_distance(rocket.velocity.x),3))+ " km/s", True, (255, 0, 255))
    #info4 = font.render('Y Velocity: ' + str(round(denormalize_distance(rocket.velocity.y),3))+ " km/s", True, (255, 0, 255))
    #info5 = font.render('X Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.x)*1000,6)) + " m/s/s", True, (255, 0, 255))
    #info6 = font.render('Y Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.y)*1000,6)) + " m/s/s", True, (255, 0, 255))


    # Draw to the display
    #pygame.draw.circle(screen, (0, 0, 255),rocket.position, 5)
    for planet in planetsList:
        planet.draw(screen)
 
    screen.blit(info0, (20, 0))
    #screen.blit(info1, (20, 20))
    #screen.blit(info2, (20, 40))
    #screen.blit(info3, (20, 60))
    #screen.blit(info4, (20, 80))
    #screen.blit(info5, (20, 100))
    #screen.blit(info6, (20, 120))

    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
