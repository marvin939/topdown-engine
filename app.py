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
		self.__scenedude = SceneManager()
		self.signalSceneDict = {}
	

	def register_scene(self, scene, name=None, signal=None):
		if scene == None:
			raise TypeError('scene argument cannot be None!')
		'''
		if name == None and self.__scenedude[scene.name] is not None:
			raise TypeError('A scene with the same name ({}) has already been registered!'.format(name))
		'''
		if name == None:
			# check if an instance of the same name is already registered
			tryScene = None
			try:
				tryScene = self.__scenedude[scene.name]
			except KeyError:
				pass
			finally:
				if tryScene != None:
					raise TypeError('A scene with the same name ({}) has already been registered!'.format(name))
				else:
					name = scene.name


		scene.set_screen_size((self.SCREENWIDTH, self.SCREENHEIGHT))
		self.__scenedude[name] = scene

		if signal is None:
			return

		if not isinstance(signal, Signal):
			raise TypeError('signal argument must be of type Signal!')
		else:
			self.signalSceneDict[signal] = scene
	

	def set_starting_scene(self, scene_name):
		pass
	

	def start(self):
		for signal in self.current_scene.status:
			if signal == Signal.CONTINUE:
				for event in pygame.event.get():
					if event.type == QUIT:
						self.quitgame()
					else:
						self.current_scene.handle_event(event)
				self.current_scene.draw_scene(self.screen)
				pygame.display.flip()
	

	def quitgame(self):
		pygame.quit()
		sys.exit()
	

	@property
	def screen(self):
		return self.__screensurf
	

	@property
	def title(self):
		return pygame.display.get_caption()[0]
	

	@property
	def scene_count(self):
		return self.__scenedude.count
	
	
	@property
	def current_scene(self):
		return self.__scenedude.current
