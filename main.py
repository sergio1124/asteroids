# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidField = AsteroidField()
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for obj in updatable:
			obj.update(dt)
		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()

		# limit the time frame to 60 FPS
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()