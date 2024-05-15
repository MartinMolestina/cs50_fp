import pygame
import time
import math
from helpers import scale_image, blit_rotate_center


GRAVEL = scale_image(pygame.image.load("./images/gravel.jpg"),0.22)
TRACK = scale_image(pygame.image.load("./images/track.png"),0.85)

TRACK_BORDER = pygame.image.load("./images/track-border.png")
FINISH = pygame.image.load("./images/finish.png")

ORANGE_CAR = scale_image(pygame.image.load("./images/orange_car.png"),0.02)
BLUE_CAR = scale_image(pygame.image.load("./images/blue_car.png"),0.02)

WIDTH, HEIGHT = GRAVEL.get_width(), GRAVEL.get_height()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Race!")

FPS = 60

def draw(win, images, player_car):
	for img, pos in images:
		win.blit(img, pos)

	player_car.draw(win)
	pygame.display.update()

class AbstractCar:
	def __init__(self, max_vel, rotation_vel):
		self.img = self.IMG
		self.max_vel = max_vel
		self.vel = 0
		self.rotation_vel = rotation_vel
		self.angle = 90
		self.x, self.y = self.START_POS
		self.acceleration = 0.1

	def rotate(self, left=False, right=False):
		if left:
			self.angle += self.rotation_vel
		elif right:
			self.angle -= self.rotation_vel

	def draw(self, win):
		blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

	def move_forward(self):
		self.vel = min(self.vel + self.acceleration, self.max_vel)
		self.move()

	def move(self):
		self.y += self.vel

class PlayerCar(AbstractCar):
	IMG = BLUE_CAR
	START_POS = (180,200)

run = True
clock =pygame.time.Clock()
images = [(GRAVEL, (0,0)), (TRACK, (50,20)), (FINISH, (0,0))]
player_car = PlayerCar(4,4)

while run:
	clock.tick(FPS)

	draw(WINDOW, images, player_car)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			break

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		player_car.rotate(left=True)
	if keys[pygame.K_d]:
		player_car.rotate(right=True)
	if keys[pygame.K_w]:
		player_car.move_forward()

pygame.quit()