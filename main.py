import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS


def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    shots = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    Asteroid.containers = ( asteroids, updatable, drawable,)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Create an asteroid field
    asteroid_field = AsteroidField()

    

    player = Player(x, y)
        
    dt = 0




 
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # Draw all objects in the drawable group
        for entity in drawable:
            entity.draw(screen)
        
        # Update all objects in the updatable group
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    break
    


        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        
        dt = clock.tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")











if __name__ == "__main__":
    main()

