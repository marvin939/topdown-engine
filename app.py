import pygame
import sys
from pygame.locals import *
from scene import Scene, SceneManager
from constants import Signal


class GameWindow():

	def __init__(self, title="No-title Game Window", screen_size=(800, 600)):
		pygame.init()
		self.__screensurf = pygame.display.set_mode(screen_size)
		pygame.display.set_caption(title)
		self.SCREENWIDTH = screen_size[0]
		self.SCREENHEIGHT = screen_size[1]
		self.scenedude = SceneManager()
		self.signalSceneDict = {}
	

	def register_scene(self, scene, name, signal=None):
		if scene == None:
			raise TypeError('scene argument cannot be None!')
		if name == None:
			raise TypeError('name argument cannot be None!')

		self.scenedude[name] = scene

		if signal is None:
			return

		if not isinstance(signal, Signal):
			raise TypeError('signal argument must be of type Signal!')
		else:
			self.signalSceneDict[signal] = scene
	

	def set_starting_scene(self, scene_name):
		pass
	

	def start(self):
		pass
	

	def quitgame(self):
		pygame.quit()
		sys.exit()
	

	@property
	def screen(self):
		return self.__screensurf
	

	@property
	def title(self):
		return pygame.display.get_caption()[0]
