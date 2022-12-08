import constants
import pygame


class Particle2D:
    image = pygame.image.load("Assets/Particle1.png")  # Particle Sprite

    def __init__(self, mass=10.0, position=None, velocity=None, acceleration=None, gravityEnabled=False):
        if velocity is None:
            velocity = [0, 0]
        if position is None:
            position = [0, 0]
        if acceleration is None:
            acceleration = [0, 0]
        self.position = position
        self.velocity = [velocity[0] * constants.PIXELSPERCENT / 60, velocity[1] * constants.PIXELSPERCENT / 60]
        self.mass = mass
        self.acceleration = [acceleration[0] / constants.PIXELSPERCENT, acceleration[1] / constants.PIXELSPERCENT]
        self.gravityEnabled = gravityEnabled
        if self.gravityEnabled:
            self.acceleration[1] = self.acceleration[1] + constants.G

    def __str__(self):
        return f"mass: {self.mass}, position: ({self.position[0]}, {self.position[1]}), velocity: ({self.velocity[0]}, {self.velocity[1]})\n"

    def noAccelerationMovement2D(self):
        self.position[0] += self.velocity[0]
        self.position[1] -= self.velocity[1]
        if self.gravityEnabled:
            self.velocity[1] += constants.G

    def acceleratedMovement2D(self):
        self.position[0] += self.velocity[0]
        self.position[1] -= self.velocity[1]
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

    def move2D(self):
        if self.acceleration == [0, 0]:
            self.noAccelerationMovement2D()
        else:
            self.acceleratedMovement2D()


class Particle:
    def __init__(self, mass=10.0, positionX=0, velocityX=0):
        self.positionX = positionX
        self.velocityX = velocityX / 60
        self.mass = mass

    def __str__(self):
        return f"mass: {self.mass}, positionX: (self.positionX), velocity: (self.velocityX)\n"
