#Imports
import pygame
import sys
import Particle
import colors
import constants
pygame.init()

# Window Settings
windowSize = (1080, 920)  # Window size (WIDTH, HEIGHT)
screen = pygame.display.set_mode(windowSize, pygame.RESIZABLE)  # Screen initiation
pygame.display.set_caption("Physics Simulation")  # Window Title

# CONSTANTS
FPS = 60  # Framerate
MIDDLEX = windowSize[0] / 2  # Middle point of the x axes
MIDDLEY = windowSize[1] / 2  # Middle point of the y axes

# Particle Initialization
particle1 = Particle.Particle2D(10, [0, MIDDLEY], [0, 0], [2, 12], True)
particle2 = Particle.Particle2D(10, [0, MIDDLEY + 10], [0, 0], [2, 9.1], True)

# Add particles to Array
particles = [particle1, particle2]


def update():  # Do the calculations
    for i in particles:  # Cycle through the particles
        i.move2D()  # Calculating position tuple of each particle


def draw():  # Render the sprites on the screen
    screen.fill(colors.WHITE)  # Erasing previous frame

    for i in particles:  # Cycling through the particles
        screen.blit(i.image, i.position)  # Display the particles in the given position on the screen

    pygame.display.update()  # Updating the screen


def debug():
    # print(f"{1 / FPS * frames + 1} seconds")
    print("G: ", constants.G)
    print("AccelrationY: ", particle1.acceleration[1])


frames = 0
while True:  # Game Loop
    frames += 1  # Keeping track of the current frame
    for event in pygame.event.get():  # Cycling through all the possible pygame events
        if event.type == pygame.QUIT:  # Checking if the close button was pressed
            sys.exit()  # Exit button event ( CLOSING THE PROGRAM )
        if event.type == pygame.VIDEORESIZE:  # Checking if the user resized the window
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)  # Changing width and height

    # Calling all the functions ( update and draw )
    update()
    draw()
    debug()

    # Managing a standard framerate
    pygame.time.Clock().tick(FPS)
