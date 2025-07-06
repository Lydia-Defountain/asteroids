import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            fling_angle = random.uniform(20, 50)
            fling_direction_1 = self.velocity.rotate(fling_angle)
            fling_direction_2 = self.velocity.rotate(-fling_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            x, y = self.position
            broken_asteroid_1 = Asteroid(x, y, radius)
            broken_asteroid_1.velocity = fling_direction_1 * 1.2
            broken_asteroid_2 = Asteroid(x, y, radius)
            broken_asteroid_2.velocity = fling_direction_2 * 1.2
            