import pygame
from pygame.math import Vector2

from calculations import denormalize_distance, normalize_distance
from globals import FPS, planetsList, SUN_POS
from celestial_body import CelestialBody
from textbox import InputBox

pygame.init()
pygame.display.set_caption("Launch Simulator")

# Set up the drawing window
WIDTH = 1000
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA) #alpha surface for trails
FramePerSec = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20)

# Adding Planets
#earth
planetsList.append(CelestialBody("Earth", Vector2(500, 500 + normalize_distance(147100000)), 5.97219e24, 0, (0, 0, 255), normalize_distance(30.29), 0, 5))
#moon
#planetsList.append(CelestialBody(Vector2(500, 500 + normalize_distance(147100000 + 384400)), 7.34767309e22, 1, (255, 255, 255), normalize_distance(30.29+1.022), 0, 1))
#mercury
planetsList.append(CelestialBody("Mercury", Vector2(500, 500 + normalize_distance(46000000)), 3.285e23, 1, (200, 100, 30), normalize_distance(58.98), 0, 3))
#venus
planetsList.append(CelestialBody("Venus", Vector2(500, 500 + normalize_distance(107476000)), 4.867e24, 2, (234,213,191), normalize_distance(35.26), 0, 4))
#mars
planetsList.append(CelestialBody("Mars", Vector2(500, 500 + normalize_distance(206600000)), 6.39e23, 3, (200, 20, 20), normalize_distance(26.50), 0, 4))
#Time Scale text box
input_speed = InputBox(184, 40, 40, 32)  #x y w h


# Run until the user asks to quit
running = True

start = False  #simulation started or not
play = False  #simulation play or pause

selected_planet = planetsList[0];

time = 0
while running:
    # Constant refresh instructions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit if closed
            running = False
        input_speed.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #space play/pauses 
                if not start:
                    start = True 
                else:
                    play = not play
        if event.type == pygame.MOUSEBUTTONDOWN: #planet buttons
            if 60-15 <= mouse[0] <= 60+15 and 750-15 <= mouse[1] <= 750+15: 
                selected_planet = planetsList[1]
            if 60-30 <= mouse[0] <= 60+30 and 800-30 <= mouse[1] <= 800+30: 
                selected_planet = planetsList[2]
            if 60-40 <= mouse[0] <= 60+40 and 875-40 <= mouse[1] <= 875+40: 
                selected_planet = planetsList[0]
            if 60-30 <= mouse[0] <= 60+30 and 950-30 <= mouse[1] <= 950+30: 
                selected_planet = planetsList[3]
            #if event.key ==pygame.K_R: #restart

    #pygame.draw.circle(screen, (200,100,30), (60, 750), 15)
    #pygame.draw.circle(screen, (234,213,191), (60, 800), 30)
    #pygame.draw.circle(screen, (0,100,255), (60, 875), 40)
    #pygame.draw.circle(screen, (200,0,0), (60, 950), 30)

    mouse = pygame.mouse.get_pos() 

 
    screen.fill((0, 0, 0))  # Fill the background with black
    

    pygame.draw.line(screen,(50,50,50),(500,0),(500,1000))
    pygame.draw.line(screen,(50,50,50),(0,500),(1000,500))

    pygame.draw.circle(screen, (255, 255, 0), SUN_POS, 64)  # Draw the Sun
    

    if play:  #after start
        for planet in planetsList:
            planet.update_acceleration()

        for planet in planetsList:
            planet.update(input_speed.time_constant)
        
        time = round(pygame.time.get_ticks()/1000)
    else:
        #keep time at zero before starting
        if not start:  #init values in text boxes
            time = 0

    input_speed.updatetext()

    #print(TIME_CONSTANT)
    #Ui Elements 
    input_speed.update()
    input_speed.draw(screen)   
    #top left
    into_time = font.render('Time Elapsed: ' + str(time)+ " seconds", True, (255,0,255))
    speed_text = font.render('Simulation Speed:                                   x', True, (255, 0, 255))

    #top right

    #bottom left
    pygame.draw.circle(screen, (200,100,30), (60, 750), 15)
    pygame.draw.circle(screen, (234,213,191), (60, 800), 30)
    pygame.draw.circle(screen, (0,100,255), (60, 875), 40)
    pygame.draw.circle(screen, (200,0,0), (60, 950), 30)
    #bottom right
    info_planet = font.render(selected_planet.name, True, (255, 0, 255))
    info1 = font.render('X Position: ' + str(round(denormalize_distance(selected_planet.position.x-SUN_POS.x)))+ " km", True, (255, 0, 255))
    info2 = font.render('Y Position: ' + str(round(-denormalize_distance(selected_planet.position.y-SUN_POS.y)))+ " km", True, (255, 0, 255))
    info3 = font.render('X Velocity: ' + str(round(denormalize_distance(selected_planet.velocity.x),3))+ " km/s", True, (255, 0, 255))
    info4 = font.render('Y Velocity: ' + str(round(denormalize_distance(selected_planet.velocity.y),3))+ " km/s", True, (255, 0, 255))
    #info5 = font.render('X Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.x)*1000,6)) + " m/s/s", True, (255, 0, 255))
    #info6 = font.render('Y Acceleration: ' + str(round(denormalize_distance(rocket_acceleration.y)*1000,6)) + " m/s/s", True, (255, 0, 255))
    info7 = font.render('Total Energy: ' + str(round(selected_planet.tEnergy*(10**-32),2)) + "e32 Joules", True, (255, 0, 255))

    # Draw to the display
    #pygame.draw.circle(screen, (0, 0, 255),rocket.position, 5)
    for planet in planetsList:
        planet.draw(screen)
        pygame.draw.circle(alpha_surf, planet.color, (planet.position.x,planet.position.y),1)
    
    pygame.draw.circle(alpha_surf, (255,255,255), (100,100),1)

    screen.blit(speed_text, (20, 40))
    screen.blit(into_time, (20, 10))
    screen.blit(info_planet, (700, 800))
    screen.blit(info1, (700, 830))
    screen.blit(info2, (700, 850))
    screen.blit(info3, (700, 870))
    screen.blit(info4, (700, 890))
    screen.blit(info7, (700, 910))

    screen.blit(alpha_surf, (0, 0))
    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
