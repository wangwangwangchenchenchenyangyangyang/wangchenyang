import pygame
from pygame import display 
from pygame.locals import *

import sys

pygame.init()

screen = display.set_mode((1280,720))
display.set_caption("王晨阳")
clock = pygame.time.Clock()

class Shaking():
	def __init__(self):
		self.image = pygame.image.load("\\py_code\\fun\\shaking.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.pos = [100,100]

	def draw(self):
		screen.blit(self.image,self.pos)
	def uptate(self,event):
		self.event = event
		if self.event.type == pygame.KEYDOWN:
			if self.event.key == K_w:
				self.pos[0] += 1



shaking = Shaking()

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		shaking.uptate(event)
	screen.fill((255,255,255))
	shaking.draw()

	display.flip()
	clock.tick(60)