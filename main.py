import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_KINDS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)  # Draw the player

        updatable.update(dt)  # Update the player

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                pygame.quit()
                return
            
            for bullet in bullets:
                if asteroid.is_colliding(bullet):
                    asteroid.split()
                    bullet.kill()

        pygame.display.flip()  # Update the display

        try:
            dt = clock.tick(60) / 1000.0  # Update the delta time
        except Exception as e:
            print(f"Error: {e}")
            pygame.quit()


if __name__ == "__main__":
    main()
