from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_tow = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_son = Asteroid(self.position.x, self.position.y, new_radius)
        first_son.velocity = vector_one * 1.2
        second_son = Asteroid(self.position.x, self.position.y, new_radius)
        second_son.velocity = vector_tow * 1.2
            
