import pygame
from pygame.math import Vector2

from calculations import denormalize_distance, normalize_distance
from globals import FPS, planetsList, SUN_POS
from planet import Planet
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
planetsList.append(Planet("Earth", Vector2(500, 500+normalize_distance(147100000)), 5.97219e24, 0, (0,0,255), normalize_distance(30.29), 0, 5))
#moon
planetsList.append(Planet("Moon", Vector2(500, 500+normalize_distance(147100000+384400)), 7.34767309e22, 1, (255,255,255), normalize_distance(30.59), 0, 1))
#murcury 
planetsList.append(Planet("Murcury", Vector2(500, 500+normalize_distance(42500000)), 3.285e23, 2, (200,100,30), normalize_distance(47.59), 0, 3))
#venus
planetsList.append(Planet("Venus", Vector2(500, 500+normalize_distance(100000000)), 4e24, 3, (200,20,20), normalize_distance(35.59), 0, 4))
#Init vel and angle text boxes
planetsList.append(Planet("Mars", Vector2(500, 500+normalize_distance(222e6)), 6.39e23, 1, (255,0,0), normalize_distance(24), 0, 4))

input_speed = InputBox(120, 850, 140, 32)  #x y w h
input_boxes = [input_speed] 

# Run until the user asks to quit
running = True

start = False #simulation started or not
play = False #simulation play or pause

rocket_acceleration = Vector2(0,0) #save acceleration so display works when paused

selected_planet = planetsList[0];

while running:
    # Constant refresh instructions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if closed
            running = False
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #space play/pauses 
                if(not start):
                    start = True 
                else:
                    play = (not play)
            #if event.key ==pygame.K_R: #restart

                
    screen.fill((0, 0, 0))  # Fill the background with black

    pygame.draw.line(screen,(50,50,50),(500,0),(500,1000))
    pygame.draw.line(screen,(50,50,50),(0,500),(1000,500))

    pygame.draw.circle(screen, (255, 255, 0), SUN_POS, 64)  # Draw the Sun
    

    if(play): #after start
        for planet in planetsList:
            planet.update()
      
        time = round(pygame.time.get_ticks()/1000)
    else:
        #keep time at zero before starting
        if(not start):  #init values in text boxes
            time = 0

    #text to display      
    #top left
    into_time = font.render('Time Elapsed: ' + str(time)+ " seconds", True, (255,0,255))

    #top right

    #bottom left

    #bottom right
    info_planet = font.render(selected_planet.name, True, (255, 0, 255))
    info1 = font.render('X Position: ' + str(round(denormalize_distance(selected_planet.position.x-SUN_POS.x)))+ " km", True, (255, 0, 255))
    info2 = font.render('Y Position: ' + str(round(-denormalize_distance(selected_planet.position.y-SUN_POS.y)))+ " km", True, (255, 0, 255))
    info3 = font.render('X Velocity: ' + str(round(denormalize_distance(selected_planet.velocity.x),3))+ " km/s", True, (255, 0, 255))
    info4 = font.render('Y Velocity: ' + str(round(denormalize_distance(selected_planet.velocity.y),3))+ " km/s", True, (255, 0, 255))
    #info5 = font.render('X Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.x)*1000,6)) + " m/s/s", True, (255, 0, 255))
    #info6 = font.render('Y Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.y)*1000,6)) + " m/s/s", True, (255, 0, 255))


    # Draw to the display
    #pygame.draw.circle(screen, (0, 0, 255),rocket.position, 5)
    for planet in planetsList:
        planet.draw(screen)
 
    screen.blit(into_time, (20, 0))
    screen.blit(info_planet, (700, 800))
    screen.blit(info1, (700, 820))
    screen.blit(info2, (700, 840))
    screen.blit(info3, (700, 860))
    screen.blit(info4, (700, 880))
    #screen.blit(info5, (20, 100))
    #screen.blit(info6, (20, 120))

    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
