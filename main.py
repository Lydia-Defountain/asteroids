import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # set up container groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (Shots, updatable, drawable)

    # set up player and objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.crash(asteroid) == True:
                print("Game Over! Better Luck Next time!")
                sys.exit()
            for bullet in Shots:
                if bullet.crash(asteroid) == True:
                    bullet.kill()
                    asteroid.split()
        for drawn_things in drawable:
            drawn_things.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000
   


if __name__ == "__main__":
    main()
