# Demonstrate how scenes can be made

from scene import Scene
from constants import Signal
from pygame.locals import *
import pygame


class DummyScene(Scene):
	
	def __init__(self):
		super().__init__('dummy')
		self.headcrabImage = pygame.image.load('headcrab.jpg').convert()


	@property
	def status(self):
		while True:
			yield Signal.CONTINUE
	
	def handle_event(self, event):
		if event.type == KEYDOWN:
			print('Key code "{}" has been pressed down (KEYDOWN)'.format(event.key))
	

	def draw_scene(self, screen):
		screen.blit(self.headcrabImage, (0,0))
		#print('drawing headcrab...')
	


if __name__ == '__main__':
	pass
